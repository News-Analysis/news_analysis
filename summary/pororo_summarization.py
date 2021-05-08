from pororo import Pororo
import pandas as pd


seoul_data = pd.read_csv("seoul_data.csv")
mt_data = pd.read_csv("mt_data.csv")
josun_data = pd.read_csv("josun.csv")
hankyoreh_data = pd.read_csv("hankyoreh.csv")

seoul_sum_text_list = list()
mt_sum_text_list = list()
josun_sum_text_list = list()
han_sum_text_list = list()

summarize = Pororo(task="summary", lang="kr")

i = 0

for text in seoul_data['content']:
    sum_text = summarize(text)
    seoul_sum_text_list.append(sum_text)
    i += 1
    print(i, "텍스트 완성")
    print(sum_text)

df = pd.DataFrame(seoul_sum_text_list)
df.to_csv('C:\\Users\\RYU\\seoul_data_sum.csv', index=False, encoding='utf-8-sig')

for text in mt_data['content']:
    sum_text = summarize(text)
    mt_sum_text_list.append(sum_text)
    i += 1
    print(i, "텍스트 완성")
    print(sum_text)

df = pd.DataFrame(mt_sum_text_list)
df.to_csv('C:\\Users\\RYU\\mt_data_sum.csv', index=False, encoding='utf-8-sig')

for text in josun_data["content"]:
    sum_text = summarize(text)
    josun_sum_text_list.append(sum_text)
    i += 1
    print(i, "텍스트 완성")
    print(sum_text)

df = pd.DataFrame(josun_sum_text_list)
df.to_csv('C:\\Users\\RYU\\josun_data_sum.csv', index=False, encoding='utf-8-sig')

i = 0
for text in hankyoreh_data["content"]:
    sum_text = summarize(text)
    han_sum_text_list.append(sum_text)
    i += 1
    print(i, "텍스트 완성")
    print(sum_text)

df = pd.DataFrame(han_sum_text_list)
df.to_csv('C:\\Users\\RYU\\han_data_sum.csv', index=False, encoding='utf-8-sig')