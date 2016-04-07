#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: mithril
# @Date:   2015-12-08 13:17:04
# @Last Modified by:   mithril
# @Last Modified time: 2015-12-08 13:17:04


from pyspider.libs.base_handler import every, config
from udbswp.handler.search_handler import SearchHandler as MyHandler
from datetime import datetime
from pyspider.libs.utils import md5string
from udbswp.config import OCR_ACCOUNT, OCR_PWD,OCR_SOFTID,OCR_SOFTKEY
from user_agent import generate_user_agent
import requests
import time
from udbswp.utils.common_utils import *
from pyquery import PyQuery as pq
from lxml import etree
import re

GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'

proxies = ''

class WeixinHandler(MyHandler):

    crawl_config = {
        'headers': {
            'User-Agent':"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
        },

    }

    UPDATE_PROXIES_INTERVAL = 60
    MAX_PAGE = 1
    LIST_ANCHOR_SEL = '.txt-box>h4>a'
    NEXT_ANCHOR_SEL = 'a#sogou_next'
    PROXY_ON = False
    JS_ON = False
    
    ACCOUNT_TYPE = 'weixin'


    def crawl(self, url, **kwargs):

        if 'retries' not in kwargs:
            kwargs['retries'] = 0

        return super(WeixinHandler, self).crawl(url, **kwargs)

    
    def check_update(self):
        super(WeixinHandler, self).check_update()
        self.update_accounts()

    def update_accounts(self):
        self.accounts = self.api.get_accounts(tp=self.ACCOUNT_TYPE) or []
        self.last_update_accounts = time.time()

    def generate_account_urls(self):
        account_urls = dict()
        for account in self.accounts:
            url = self.build_account_url(account)
            context = {
                    'account': account
                }
            account_urls[url] = context
        return account_urls
    
    def build_account_url(self, account):
        return 'http://weixin.sogou.com/weixin?type=1&query=%s&ie=utf8' % account
        
    def build_url(self, keyword):
        return 'http://weixin.sogou.com/weixin?query=%s&type=2&ie=utf8' % keyword
        
    @every(60)
    def on_start(self):
        self.check_update()

        cookies = self.get_cookie() or {}
        
        print cookies
        
        # keyword
        urls = self.generate_urls().items()
        for url, context in urls:
            context['preurl'] = url
            context['isPublicAccount'] = 0
            self.crawl(url, callback=self.crawl_list_page, cookies=cookies, save=context, force_update=True)
            
        # account
        account_urls = self.generate_account_urls().items()
        for url, account_context in account_urls:
            account_context['isPublicAccount'] = 1
            self.crawl(url, callback=self.account_list_page, cookies=cookies, save=account_context, force_update=True)
            
    @config(priority=2)   
    def account_list_page(self, response):
        db_cookie = self.get_cookie() or {}
        r_cookie = response.cookies

        db_ctime = int(db_cookie.get('ctime', 0))
        r_ctime = int(r_cookie.get('ctime', 0))
        
        if self.check_captcha(response):
            if db_ctime <= r_ctime:
                db_cookie = self.verify_vcode(response)
                if not db_cookie:
                    raise Exception('sougou_weixin refresh cookies fail!')
            
            #self.crawl(response.url, callback=self.account_list_page, cookies=db_cookie, save=response.save, force_update=True)
        else:
            try:
                openid_url = 'http://weixin.sogou.com'+ response.doc('.wx-rb:first').attr.href
            except Exception as e:
                raise Exception('account_list_page error, can not get account!')
            OPENID_PT = re.compile(ur'.+openid=(?P<openid>.*)')
            m = OPENID_PT.match(openid_url)
            openid = m.groupdict().get('openid')
            api_url = 'http://weixin.sogou.com/gzhjs?openid=' + openid
            self.crawl(api_url, callback=self.account_api_page, cookies=response.cookies, save=response.save)

    @config(priority=3)
    def account_api_page(self, response):
        for item in response.json['items']:
            parser = etree.XMLParser(ns_clean=True, recover=True, encoding='utf-8')
            root = etree.fromstring(item.encode('utf-8'), parser=parser)
            url = 'http://weixin.sogou.com' + root.xpath('//url')[0].text
            self.crawl(url, callback=self.detail_page, save=response.save, cookies=response.cookies)

    
    @config(priority=3)
    def crawl_list_page(self, response):
        
        db_cookie = self.get_cookie() or {}
        r_cookie = response.cookies
        
        print db_cookie
        print r_cookie
        
        db_ctime = int(db_cookie.get('ctime', 0))
        r_ctime = int(r_cookie.get('ctime', 0))
        
        if self.check_captcha(response):
            if db_ctime <= r_ctime:
                db_cookie = self.verify_vcode(response)
                if not db_cookie:
                    raise Exception('sougou_weixin refresh cookies fail!')
            
            #self.crawl(response.url, callback=self.crawl_list_page, cookies=db_cookie, save=response.save, force_update=True)
        else:
            # response.cookies.update(cookies)
            # 更新cookies 会导致无法转跳到 detail页面

            for each in response.doc(self.LIST_ANCHOR_SEL).items():
                taskid = md5string(each.text())
                self.crawl(each.attr.href, taskid=taskid, callback=self.detail_page, save=response.save, cookies=response.cookies)

    @config(priority=10)
    def detail_page(self, response):
        #print cookies
        if self.check_captcha(response):
            cookie = self.verify_vcode(response)
            
            if cookie:
                raise Exception('sougou_weixin page need captcha, refresh success!')
            else:
                raise Exception('sougou_weixin page need captcha, break fail!')

        return {
            "type": 'weixin',
            "url": response.url,
            "title": response.doc('title').text().strip(),
            "text": response.doc('.rich_media_content').text().strip(),
            "authors": response.doc('#post-user').text().strip(),
            "publish_time": response.doc('#post-date').text(),
            'extra': response.save
        }


    def verify_vcode(self,response):
        success = 0
        db_cookie = self.get_cookie() or {}
        
        preurl = response.save.get('preurl')
        context = response.save
        session = requests.session()
        headers = {
            'User-Agent':"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36"
        }
        session.headers.update(headers)
        session.cookies.update(response.cookies)

        d = pq(response.doc('.p4'))
        fromid = d.find('input').eq(2).val()

        #------- 获取cookie SUV
        cookies = {}
        if "SUV" in response.cookies:
            cookies["SUV"] = response.cookies["SUV"]
        else:
            suv_url = 'http://pb.sogou.com/pv.gif?uigs_productid=webapp&type=antispider&subtype=seccodeFocus&domain=weixin&t=%d' % int(time.time())
            headers['Referer'] = response.url
            r = session.get(suv_url,headers=headers,proxies=proxies)
            #print suv_url
            #print response.url
            #print headers
            #print r.content
            #print r.status_code
            #return
            #if not cookies.has_key('SUV') and r.cookies.has_key('SUV'):
            cookies['SUV'] = r.cookies['SUV']

        #-------- 获取验证码

        url = 'http://weixin.sogou.com/antispider/util/seccode.php?tc={}'.format(int(time.time()))
        r = session.get(url,proxies=proxies)
        if r.status_code == requests.codes.ok:
            ocr_json = ysdm_ocr_buf(r.content, OCR_ACCOUNT, OCR_PWD,OCR_SOFTID,OCR_SOFTKEY)
            if 'Error' in ocr_json:
                raise Exception(ocr_json['Error'].encode('utf-8'))
            else:
                playound = {
                    'v':5,
                    'c':ocr_json['Result'],
                    'r':fromid
                }

                #-------- 提交验证码
                posturl = 'http://weixin.sogou.com/antispider/thank.php'

                r = session.post(posturl,data=playound,proxies=proxies)
                if r.status_code == requests.codes.ok:
                    res_json = r.json()
                    print res_json
                    if res_json['code'] == 3:
                        ysdm_rep_err(ocr_json['Id'],OCR_ACCOUNT, OCR_PWD,OCR_SOFTID)
                    elif res_json['code'] == 0:# ok
                        print 'ok'
                        #print response.cookies

                        cookies['SNUID'] = res_json['id']
                        cookies['successCount']='1|'+datetime.utcnow().strftime(GMT_FORMAT)
                        cookies['ctime']= str(int(time.time()))
                        self.set_cookie(cookies)
                        print cookies
                        success = 1

        return cookies if success else None
            
            
    def check_captcha(self, response):
        return True if response.doc('#seccodeImage') else False


    def try_refresh_cookie(self, response, db_cookie):
        
        db_cookie = self.get_cookie() or {}
        r_cookie = response.cookies
        
        db_ctime = int(db_cookie.get('ctime', 0))
        r_ctime = int(r_cookie.get('ctime', 0))
        
        if self.check_captcha(response):
            if db_ctime <= r_ctime:
                db_cookie = self.verify_vcode(response)
                if not db_cookie:
                    raise Exception('sougou_weixin refresh cookies fail!')           
            
        return db_cookie
     

    def raise_on_error(self, response):
        if self.check_captcha(response):
            raise Exception('sougou_weixin page need captcha, break!')

