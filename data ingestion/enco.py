import pandas as pd

jo = pd.read_csv('./data/josun.csv')
han = pd.read_csv('./data/hankyoreh.csv')

jo.to_csv('./data/josun.csv', index=False, encoding='utf-8-sig')
han.to_csv('./data/hankyoreh.csv', index=False, encoding='utf-8-sig')