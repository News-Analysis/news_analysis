import pandas as pd
from scipy import stats
import glob

p_list = glob.glob('./result_entire/박영선/*')
o_list = glob.glob('./result_entire/오세훈/*')
#print(path_list)
df_list = []

for path in p_list:
    df_list.append(pd.read_csv(path))
for path in o_list:
    df_list.append(pd.read_csv(path))

final = df_list[0]

for i in range(1, len(df_list)):
    final = pd.concat([final, df_list[i]], axis=0)



# 비모수 검정
re = stats.wilcoxon(final['info'] - 0.5)
print("wilcoxon 검정 결과")
print(re)
print("mu : 0.5")
print('alpha = 0.05')
print("rejection : ", end="")
print(0.05>re[1])