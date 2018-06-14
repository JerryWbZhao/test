#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, os
import HTMLTestRunner
class Teacher2(unittest.TestCase):
    def setUp(self):
        chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)
        self.driver.implicitly_wait(30)
        self.base_url = "https://t.qa.bingotalk.cn/#/login"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    #教师登录用例
    def test_teacher_order(self):
        u"""教师排课用例"""
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        try:
        #是一个无法找到的元素id
            driver.find_element_by_xpath("//*[@id='app']/div/div[1]/form/div/div[1]/div/div/div/input").send_keys("zhaoweibo@bingotalk.cn")
        except:
            driver.get_screenshot_as_file("D:\\selenium_use_case\\error_png\\t_username.png")
        #如果没有找到上面的元素就截取当前页面。
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/form/div/div[2]/div/div/div/input").send_keys("Pass1234")
        driver.find_element_by_xpath("//*[@id='app']/div/div[1]/form/div/button").click()
        driver.find_element_by_xpath("//*[@id='app']/div/div[4]/div/div[1]/div").click()
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[3]/div/div[1]/div").click()
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[3]/div/div[2]/div").click()        
        time.sleep(2)
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[1]/ul/li[2]").click()
        #选择一个时间，排课
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div/div[3]/div[2]/div/div[3]/table/tbody/tr[1]/td[8]/div/div").click()
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div/div[2]/div").click()
        time.sleep(2)
        #选择一个时间，取消排课
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div/div[3]/div[2]/div/div[3]/table/tbody/tr[1]/td[8]/div/div[2]/label/span[2]").click()
        driver.find_element_by_xpath("//*[@id='app']/div/div[2]/div[2]/div/div[2]/div").click()        
        time.sleep(2)
        driver.close()
        
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(Teacher2("test_teacher_order"))
    results = unittest.TextTestRunner().run(suite)