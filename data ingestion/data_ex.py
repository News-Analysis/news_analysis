import glob
import pandas as pd


path_list = glob.glob('.\\keyword\\*/*')
df_list = []
keywords = []
for path in path_list:
    df_list.append(pd.read_csv(path))
    keywords.append(path.split('\\')[2])

for df, keyword in zip(df_list, keywords):
    try:
        press = df.loc[0, 'press']
        df['date'] = pd.to_datetime(df['date'])
        mask = (df['date'] < '2021-04-07')
        df = df[mask]
        df.to_csv('./date_key/'+press+'_'+keyword+'.csv', index=False, encoding='utf-8-sig')
    except:
        continue