import pandas as pd
import glob


path = glob.glob('./data/*')
print(path)


keyword = '홍준표'
ex = []


for p in path:
    df = pd.read_csv(p)
    try:
        content_mask = df['content'].str.contains(keyword)
        content = df[content_mask]
        title_mask = content['title'].str.contains(keyword)
        title = content[title_mask]
        ex.append(title)
    except:
        print('except')


press = ['donganew.csv', 'hankyoreh.csv', 'joins.csv', 'josun.csv', 'mt_data.csv',
         'pressian.csv', 'seoul_data.csv', 'trendnews.csv']


for t, p in zip(ex, press):
    t.to_csv(keyword+'_'+p, encoding='utf-8-sig')
