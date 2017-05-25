from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
from random import randint
import time
import json_data

print('Start Program...')

caps = DesiredCapabilities.FIREFOX
caps['marionette'] = True
caps['executable_path'] = 'C:\\Develop\\driver\\geckodriver\\geckodriver.exe'
caps['binary'] = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
print('Setting Driver')

browser = webdriver.FirefoxProfile().set_preference("browser.privatebrowsing.autostart", True)
browser = webdriver.Firefox(capabilities=caps)
print('Setting Browser')

browser.get('http://www.test.com')
time.sleep(5)
elem = browser.find_element_by_xpath("//ul[@id='nav-main']/li[5]/a")
time.sleep(5)
elem.click()
time.sleep(5)
elem = browser.find_element_by_xpath("//input[@id='username']")
elem.send_keys('usertest')
elem = browser.find_element_by_xpath("//input[@id='password']")
elem.send_keys('passtest')
elem = browser.find_element_by_xpath("//input[@name='login']")
elem.click()
time.sleep(30)
print("Login")

data = json_data.Json_data_cls()
data = data.get_value()
for data_list in data:
    if( data[data_list]['action'] == 0 ) : continue
    browser.get(data[data_list]['link'])
    elem = browser.find_element_by_xpath("//div[@id='message-box']/textarea")
    time.sleep(5)
    elem.click()
    elem.send_keys(data[data_list]['post'])
    time.sleep(5)
    elem = browser.find_element_by_xpath("//input[@name='post']")
    elem.click()
    print('Post '+data[data_list]['name'])
    wait_time = randint(300,360)
    print("Wait " + str(wait_time) + " Second")
    time.sleep(wait_time)
browser.quit()
print('End Program')


