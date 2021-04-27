from selenium import webdriver
import time


url = 'https://www.chosun.com/politics/'
driver = webdriver.Chrome(executable_path='./driver/chromedriver')
driver.get(url)

driver.implicitly_wait(time_to_wait=5)

more = driver.find_element_by_id('load-more-stories')

for _ in range(100):
    more.click()
    time.sleep(1)

#time.sleep(10)
selector = '#artwrapper > div > figure > div > div > div'
a = driver.find_elements_by_css_selector(selector)
print(a)

href = []
for item in a:
    href.append(item.find_element_by_tag_name('a').get_attribute('href'))
print(href)
print(len(href))