#!/usr/bin/env python
#coding:GBK

import unittest

import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

import time

url='http://shenzhen.dld.com'
#browser=webdriver.Chrome()
#browser=webdriver.Ie()
browser=webdriver.Firefox()
action=ActionChains(browser)
class mytest(unittest.TestCase):
    

    def setUp(self):
        pass
    

    def tearDown(self):
        pass
  #注册测试  
    def testRegister(self):
        browser.get(url)   
        browser.implicitly_wait(30)
        # browser.find_element_by_link_text('深圳').click()
        #点击注册
        browser.find_element_by_link_text(u'注册').click()

        #点击个人注册
        browser.find_element_by_xpath('/html/body/div[2]/div[3]/div/div[2]/div/div/input').click()
        browser.switch_to_frame('personIframe')
        user=browser.find_element_by_xpath('/html/body/div/div/form/div/dl/dd/div/input')
        
        user.send_keys('sdfdsfs')
        email=browser.find_element_by_xpath('/html/body/div/div/form/div/dl[2]/dd/div/input')
        email.send_keys('sdfdsfs@126.com')
        password=browser.find_element_by_xpath('/html/body/div/div/form/div/dl[3]/dd/div/input[5]')
        password.send_keys('123456789a')
        reg=browser.find_element_by_xpath('/html/body/div/div/form/div/div[2]/input')


        action=ActionChains(browser)
        action.move_to_element(reg).perform()
        action.send_keys(Keys.ENTER).perform()
        time.sleep(10)
        if browser.current_url != 'http://shenzhen.dld.com/':
            browser.get_screenshot_as_file('regErr.png')
            self.fail('-注册失败|regErr.png-')
         # print browser.current_url
    #搜索测试
    def testSearchCheck(self):
        browser.get(url)   
        browser.implicitly_wait(30)
     
        searchInpu=browser.find_element_by_xpath('//*[@id="searchInput"]')
                                                 
        action.move_to_element(searchInpu).perform()
        action.click().perform()
        searchInpu.send_keys(u'酒店')
        browser.find_element_by_id('mainSearchButton').click()
        result=browser.find_element_by_xpath('//div[@class="tipMessageWrap marginTop10 gray3"]//span[2]').text

        if int(result) !=20 :
            browser.get_screenshot_as_file('SearchCheckErr.png')
            self.fail('-搜索与预期结果20不匹配|SearchCheckErr.png-')
     
if __name__ =='__main__':
    filename ="result.html"
    fp = file(filename,"wb")
    suit = unittest.TestSuite()
    suit.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(mytest))
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="testing result",description="trying")
    runner.run(suit)


