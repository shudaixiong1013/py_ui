from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep, ctime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time, unittest, os,sys
from Util.tools import *



# 获取到driver
class open_url():
    def get(self, url):
        # chrome路径
        chromedriver = 'chromedriver.exe'
        # 判断是否存在
        isexists = os.path.exists(chromedriver)
        if isexists is False:
            print('chromedriver.exe 不存在')
        os.environ['webdriver.chrome.driver'] = chromedriver
        driver = webdriver.Chrome(chromedriver)
        driver.maximize_window()
        driver.implicitly_wait(5)
        print('启动浏览器:%s' % url)
        driver.get(url)
        print(driver.title)
        return driver


# 所选元素高亮dfs
def highlight(driver, element):
    driver = element._parent

    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)

    original_style = element.get_attribute('style')
    apply_style("background: yellow; border: 2px solid red;")
    apply_style(original_style)


# 点击操作
class click():
    def action(self, driver, location, str):
        try:
            print('点击操作:%s' % location)
            if location == 'xpath':
                self.driver = driver
                element1 = driver.find_element_by_xpath(str)
                highlight(driver, element1)
                element = driver.find_element_by_xpath(str).click()
                return element
            elif location == 'id':
                self.driver = driver
                elemen1 = driver.find_element_by_id(str)
                highlight(driver, elemen1)
                element = driver.find_element_by_id(str).click()
                return element
            else:
                print('不支持除xpaht,id之外的定位方式!!!')
        except NoSuchElementException as  Nee:
            print('未找到匹配的元素:%s'%Nee)
            shotPic(driver)
            driver.quit()



# 输入操作
class input():
    def text(self, driver, location, str, text):
        try:
            print('输入操作:%s' % location)
            if location == 'xpath':
                self.driver = driver
                element1 = driver.find_element_by_xpath(str)
                highlight(driver, element1)
                element = driver.find_element_by_xpath(str).send_keys(text)
                return element
            elif location == 'id':
                self.driver = driver
                element1 = driver.find_element_by_id(str)
                highlight(driver, element1)
                element = driver.find_element_by_id(str).send_keys(text)
                return element
            else:
                print('不支持除xpaht,id之外的定位方式!!!')
        except NoSuchElementException as nee:
            print('未找到匹配的元素:%s'%nee)
            shotPic(driver)
            driver.quit()


if __name__ == '__main__':
    driver = open_url().get('http://oms-test.zring.sz/admin/login')
    shotPic(driver)
    input().text(driver, 'xpath', "//input[@placeholder='请输入账号1']", 'admin')
    input().text(driver, 'id', 'password', '12345678')
    click().action(driver, 'id', 'login-btn')
