import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm


paths = glob.glob('result/*/*')
dic_list = []

for path in paths:
    df = pd.read_csv(path, encoding='utf-8-sig')
    press = path.split('\\')[2].split('_')[0]
    keyword = path.split('\\')[1]
    dic = {
        'press': press,
        'keyword': keyword,
        'df': df
    }
    dic_list.append(dic)

font_path = './font/NanumBarunpenB.ttf'
fontprop = fm.FontProperties(fname=font_path, size=18)

for dic in dic_list:
    df = dic['df']
    keyword = dic['keyword']
    press = dic['press']
    total = str(df.shape[0])

    sns.histplot(data=df, x='info', stat='probability', bins=2, hue='info').set_title(
        keyword + '_' + press,
        fontproperties=fontprop
    )
    plt.savefig('./image/'+keyword+'_'+press+'_'+total+'.png')
    plt.clf()
    plt.close('all')