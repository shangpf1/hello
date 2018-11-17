
from selenium import webdriver
driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

# driver.find_element_by_id('kw').send_keys("上海")
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('西安')
driver.find_element_by_id('su').click()