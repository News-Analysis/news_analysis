import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm

font_path = './font/NanumBarunpenB.ttf'
fontprop = fm.FontProperties(fname=font_path, size=18)

# full
proba_path = glob.glob('.\\result_sig_sen/*/*')


proba_list = []
proba_press = []
proba_subject = []

for proba in proba_path:
    proba_press.append(proba.split('\\')[-1].split('_')[0])
    proba_subject.append(proba.split('\\')[2])
    proba_list.append(pd.read_csv(proba))


proba_mean = []

df = pd.DataFrame()
for proba in proba_list:
    proba_mean.append(proba['info'].mean())
    #score_mean.append(score['점수'].mean())
print(proba_subject)
print(proba_press)
print(proba_mean)
'''for i in range(len(proba_list)):
    sns.histplot(proba_list[i]['info'], bins=10).set_title(
        proba_subject[i] + '_' + proba_press[i],
        fontproperties=fontprop
    )
    plt.savefig('./hist_sen/' + proba_subject[i] + '_' + proba_press[i] + '.png')
    plt.clf()
    plt.close('all')
'''
# summary
'''proba_path = glob.glob('.\\result(요약_감성분석)/*')

df_list = []
subject_list = []

for p in proba_path:
    subject_list.append(p.split('\\')[-1].split('.')[0])
    df_list.append(pd.read_csv(p))

final_list = []
han = []
jo = []
jong = []
seoul = []
mt = []
kyng = []
dong = []
pres = []
for df in df_list:
    han.append(df[df['press'] == 'hankyoreh'])
    jo.append(df[df['press'] == '조선일보'])
    jong.append(df[df['press'] == '중앙일보'])
    seoul.append(df[df['press'] == '서울경제'])
    mt.append(df[df['press'] == '머니투데이'])
    kyng.append(df[df['press'] == '경향신문'])
    dong.append(df[df['press'] == '동아일보'])
    pres.append(df[df['press'] == '프레시안'])'''

