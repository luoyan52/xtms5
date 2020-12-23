import  pytest

import selenium
import time

import yaml
from  selenium import  webdriver
from selenium.webdriver.common.by import By


class TestWework:

   def test_demo1(self):
      opt = webdriver.ChromeOptions()
      # 设置debug地址
      opt.debugger_address = "127.0.0.1:9222"
      driver = webdriver.Chrome(options=opt)
      driver.implicitly_wait(5)
      driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
      driver.find_element_by_id("menu_contacts").click()
      print(driver.get_cookies())

# 使用cookies登录

def test_cookie():
   driver = webdriver.Chrome()
   driver.implicitly_wait(10)
   driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
   driver.implicitly_wait(5)
   cookies = [{'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.vid', 'path': '/', 'secure': False,
               'value': '1688850732084879'},
              {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.vst', 'path': '/', 'secure': False,
               'value': '9ssndgJd_SKHUUf5EuS1mfqTRPvqR-QP39fEgJ4PjHd3woxb-RpcJjdOq2pDsUeJV4zYag7vG99TjR1ooavfXHaonJCBx7t1ixSaMAsRjTR_d6QiKW4B-TnlshklbYtTVd8XDcloNO7X56qQn4RSumDdzoxJbyy995GY7asBgKnGky_ImnvTi9qjvNNli9BBcVZn0xSTggPKRxjx4ng710TTX4hUsrov3RPyt7MB9XOUe5-gOlXA_zc9AItRYWlAiX3cbvot0nEZJ9pTasFjIg'},
              {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.vid', 'path': '/', 'secure': False,
               'value': '1688850732084879'},
              {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wxpay.corpid', 'path': '/', 'secure': False,
               'value': '1970325134205314'}, {'domain': '.work.weixin.qq.com', 'expiry': 1640240823, 'httpOnly': False,
                                              'name': 'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d', 'path': '/',
                                              'secure': False, 'value': '1608693168,1608694936,1608704823'},
              {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ref', 'path': '/', 'secure': False,
               'value': 'direct'},
              {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.ltype', 'path': '/', 'secure': False,
               'value': '1'},
              {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwrtx.d2st', 'path': '/', 'secure': False,
               'value': 'a272184'},
              {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'Hm_lpvt_9364e629af24cb52acc78b43e8c9f77d',
               'path': '/', 'secure': False, 'value': '1608704823'},
              {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.refid', 'path': '/', 'secure': False,
               'value': '14745227371622883'},
              {'domain': 'work.weixin.qq.com', 'expiry': 1608724703.003491, 'httpOnly': True, 'name': 'ww_rtkey',
               'path': '/', 'secure': False, 'value': '29eta46'},
              {'domain': '.work.weixin.qq.com', 'httpOnly': True, 'name': 'wwrtx.sid', 'path': '/', 'secure': False,
               'value': 'NJLtMh11gYja7vB9GnpRqiTeFS0BR8zF7TamposTvBxitQ6wJHYG1yuLPzqKe6Kw'},
              {'domain': '.work.weixin.qq.com', 'expiry': 1640229167.003518, 'httpOnly': False, 'name': 'wwrtx.c_gdpr',
               'path': '/', 'secure': False, 'value': '0'},
              {'domain': '.work.weixin.qq.com', 'expiry': 1611296852.082937, 'httpOnly': False,
               'name': 'wwrtx.i18n_lan', 'path': '/', 'secure': False, 'value': 'zh'}]
   for cookie in cookies:
      driver.add_cookie(cookie)
   driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
   driver.find_element_by_id("menu_contacts").click()
   time.sleep(5)
   driver.quit()

def test_get_cookie():
   opt = webdriver.ChromeOptions()
   # 设置debug地址
   opt.debugger_address = "127.0.0.1:9222"
   driver = webdriver.Chrome(options=opt)
   driver.implicitly_wait(5)
   driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
   cookie =driver.get_cookies()
   print(cookie)
   with open("data.yaml","w",encoding="UTF-8") as f:
      yaml.dump(cookie,f)
# 使用序列化cookies的方法进行登录

def test_login(js_contacts47=None):
   driver = webdriver.Chrome()
   driver.implicitly_wait(5)
   driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
   with open("data.yaml", encoding="UTF-8") as f:
      yaml_data = yaml.safe_load(f)
      for cookie in yaml_data:
         if "expiry" in cookie:
             del cookie["expiry"]
         driver.add_cookie(cookie)
   driver.get("https://work.weixin.qq.com/wework_admin/frame")
   driver.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
   driver.implicitly_wait(5)
   driver.find_element_by_link_text("添加成员").click()
   driver.find_element_by_id("username").send_keys("李四")
   driver.find_element_by_id("memberAdd_acctid").send_keys("lisi123456")
   driver.find_element_by_id("memberAdd_phone").send_keys("13530077575")
   driver.find_element_by_link_text("保存").click()
   time.sleep(10)
   name1 =driver.find_element_by_xpath("//tbody/tr/td[2]")
   print(name1.text)
   assert name1.text =="李四"
