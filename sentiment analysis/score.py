import glob
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.font_manager as fm


proba_path = glob.glob('.\\result_sig/*/*')


proba_list = []
#score_list = []
proba_press = []
#score_press = []
proba_subject = []
for proba in proba_path:
    proba_press.append(proba.split('\\')[-1].split('_')[0])
    proba_subject.append(proba.split('\\')[2])
    proba_list.append(pd.read_csv(proba))
    #score_list.append(pd.read_csv(score))

proba_mean = []
#score_mean = []
df = pd.DataFrame()
for proba in proba_list:
    proba_mean.append(proba['info'].mean())
    #score_mean.append(score['점수'].mean())


'''
print(proba_subject)
df = pd.DataFrame({'점수': proba_mean,
                   '주제': proba_subject,
                  '언론사': proba_press})
print(df.to_csv('temp.csv', encoding='utf-8-sig'))
#sr_proba = pd.Series(proba_mean, index=proba_press)
#sr_score = pd.Series(score_mean, index=score_press)

#print(sr_proba.to_csv('temp.csv', encoding='utf-8-sig'))
#print(sr_score)
#df = pd.read_csv('./result_sig/오세훈/hankyoreh_result_sig.csv')
#df2 = pd.read_csv('./score/오세훈_han_result.csv')
path = glob.glob('.\\data(감성분석)/*')

df_list = []
subject_list = []

for p in path:
    subject_list.append(p.split('\\')[-1].split('.')[0])
    df_list.append(pd.read_csv(p))
print(subject_list)

final_list = []
for df in df_list:
  final_list.append(df['sentiment'].groupby(df['press']).mean())

final = pd.DataFrame(final_list[0])

for i in range(1, len(final_list)):
    final = pd.concat([final, final_list[i]], axis=1)
final.columns = subject_list
final.to_csv('summary_prob.csv', encoding='utf-8-sig')'''
