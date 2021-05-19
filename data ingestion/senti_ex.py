import pandas as pd


df = pd.read_csv('./sum_senti/news.CSV', encoding='cp949')

keyword_list = ['대통령', '박영선', '백신', '오세훈', '이낙연',
                '이재명', '재난지원금', '홍준표']

for keyword in keyword_list:
    content_mask = df['content'].str.contains(keyword)
    content = df[content_mask]
    title_mask = content['title'].str.contains(keyword)
    title = content[title_mask]
    title.to_csv(keyword + '.csv', index=False, encoding='utf-8-sig')       # 경로만 설정하시면 됩니다.
