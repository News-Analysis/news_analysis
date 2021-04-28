from selenium import webdriver
import time
import pandas as pd


# href get
url = 'https://www.chosun.com/politics/'
driver = webdriver.Chrome(executable_path='./driver/chromedriver')
driver.get(url)

driver.implicitly_wait(time_to_wait=5)

more = driver.find_element_by_id('load-more-stories')

for _ in range(120):
    more.click()
    time.sleep(1)

selector = '#artwrapper > div > figure > div > div > div'
a = driver.find_elements_by_css_selector(selector)


href = []
for item in a:
    href.append(item.find_element_by_tag_name('a').get_attribute('href'))
href = list(set(href))


# article crawling
title = []
reporter = []
content = []
dates = []

for link in href:
    driver.get(link)

    try:
        check = driver.find_element_by_xpath('//*[@id="fusion-app"]/div[1]/div[2]/div/div/div[2]/a')
        if check.text != '정치':
            continue
    except:
        continue

    try:
        span = driver.find_element_by_xpath('//*[@id="fusion-app"]/div[1]/div[2]/div/div/div[3]/h1')
        title.append(span.text)
    except:
        title.append(pd.NA)

    try:
        reporter_a = driver.find_element_by_xpath('//*[@id="fusion-app"]/div[1]/div[2]/div/section/article/div[1]/div/a')
        reporter.append(reporter_a.text)
    except:
        reporter.append(pd.NA)

    try:
        content_section = driver.find_element_by_xpath('//*[@id="fusion-app"]/div[1]/div[2]/div/section/article/section')
        p = content_section.find_elements_by_tag_name('p')
        temp = []
        for item in p:
            temp.append(item.text)
        content.append('\n'.join(temp))
    except:
        content.append(pd.NA)

    try:
        date_span = driver.find_element_by_xpath('//*[@id="fusion-app"]/div[1]/div[2]/div/section/article/div[2]/span')
        date = date_span.text
        date = date.split(' ')
        date = date[1]
        dates.append(date)
    except:
        dates.append(pd.NA)

driver.close()


print(len(dates), len(title), len(reporter), len(content))
final = pd.DataFrame({'date': dates,
                      'title': title,
                      'reporter': reporter,
                      'content': content})
final.to_csv('./data/josun.csv', index=False)

