import pandas as pd
import glob


path = glob.glob('./data/*')
print(path)


keyword = '홍준표'
ex = []
press = []
count = 0
for p in path:
    df = pd.read_csv(p)
    print(df.shape[0])
    count += df.shape[0]

print(count)
'''for p in path:
    df = pd.read_csv(p)
    df.fillna('na', inplace=True)
    press.append(df['press'][0])
    content_mask = df['content'].str.contains(keyword)
    content = df[content_mask]
    title_mask = content['title'].str.contains(keyword)
    title = content[title_mask]
    ex.append(title)


for t, p in zip(ex, press):
    t.to_csv('./keyword/'+keyword+'/'+keyword+'_'+p+'.csv', encoding='utf-8-sig', index=False)'''
