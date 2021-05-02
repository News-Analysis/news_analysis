from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re


# href get
driver = webdriver.Chrome(executable_path='./driver/chromedriver')

href = []
for number in range(1,150):
    url = 'https://www.pressian.com/pages/news-politics-list?page='
    number = str(number)
    url = url + number
    driver.get(url)
    driver.implicitly_wait(time_to_wait=5)

    h4 = driver.find_elements_by_class_name('title')

    for item in h4:
        url = item.find_element_by_tag_name('a').get_attribute('href')
        if len(url) == 59:
            href.append(item.find_element_by_tag_name('a').get_attribute('href'))


print(len(href))



# article crawling
title = []
reporter = []
content = []
dates = []


def clean_text(text):
    cleaned_text = re.sub('\xa0','', text)
    cleaned_text = ' '.join(cleaned_text.split())
    return cleaned_text


for link in href:
    req = requests.get(link)
    soup = BeautifulSoup(req.text, 'html.parser')

    try:
        title.append(soup.select_one('.view_header > p').text.strip())
    except:
        title.append(pd.NA)
    try:
        text = soup.select_one('.view_header > div > div').get_text().strip()
        i = 0
        while text[i] != ' ':
            i += 1
        text = text[0:i]
        reporter.append(text)
    except:
        reporter.append(pd.NA)

    try:
        text = soup.select_one('.article_body').text.strip()
        text = clean_text(text)
        content.append(text)
    except:
        content.append(pd.NA)

    try:
        text = soup.select_one('.view_header > div > div').get_text().strip()
        text = text[-20:-9]
        dates.append(text)
    except:
        dates.append(pd.NA)

driver.close()


print(len(dates), len(title), len(reporter), len(content))
final = pd.DataFrame({'date': dates,
                      'title': title,
                      'reporter': reporter,
                      'content': content})
final.to_csv('./data/pressian.csv', index=False)
