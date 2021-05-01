from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd


# href get
driver = webdriver.Chrome(executable_path='./driver/chromedriver')

href = []
for number in range(1, 150):
    url = 'http://www.hani.co.kr/arti/politics/list'
    if number < 10:
        number = '0' + str(number)
    else:
        number = str(number)
    url = url + number + '.html'
    driver.get(url)
    driver.implicitly_wait(time_to_wait=5)

    h4 = driver.find_elements_by_class_name('article-title')

    for item in h4:
        href.append(item.find_element_by_tag_name('a').get_attribute('href'))

href = list(set(href))
print(len(href))

# article crawling
title = []
reporter = []
content = []
dates = []

for link in href:
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'html.parser')

    try:

        #title_span = driver.find_element_by_xpath('//*[@id="article_view_headline"]/h4/span')
        #title.append(title_span.text)
        #print(len(title))
        title.append(soup.select_one('span.title').text.strip())
    except:
        title.append(pd.NA)

    try:
        content_div = soup.select_one('div.text')
        divs = content_div.select('div')
        for div in divs:
            div.decompose()
        content_text = content_div.text.strip().split('\n')
        reporter.append(content_text[-1])
        del content_text[-1]
        content.append(('\n'.join(content_text)))
    except:
        content.append(pd.NA)
        reporter.append(pd.NA)

    try:
        #date = driver.find_element_by_class_name('date-time').text
        date = soup.select_one('p.date-time > span').text.strip()
        date = date.split(' ')
        dates.append(date[1][1:])
    except:
        dates.append(pd.NA)
driver.close()


print(len(dates), len(title), len(reporter), len(content))
final = pd.DataFrame({'date': dates,
                      'title': title,
                      'reporter': reporter,
                      'content': content})
final.to_csv('./data/hankyoreh.csv', index=False)
