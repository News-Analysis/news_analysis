import pandas as pd
from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize
from konlpy.tag import Okt
from tqdm import tqdm
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import seaborn as sns

news = pd.read_csv('./data/news.CSV', encoding='cp949')

okt = Okt()
news_content = news['summary']
tagged_data = [TaggedDocument(words=okt.morphs(_d), tags=[str(i)]) for i, _d in enumerate(news_content)]

max_epochs = 50
model = Doc2Vec(vector_size=20,
                alpha=0.025,
                min_alpha=0.00025,
                min_count=1,
                dm=1)

#
model.build_vocab(tagged_data)

# 학습
for epoch in tqdm(range(max_epochs)):
    model.train(tagged_data,
                total_examples=model.corpus_count,
                epochs=model.iter)
    # decrease the learning rate
    model.alpha -= 0.0002
    # fix the learning rate, no decay
    model.min_alpha = model.alpha

model.wv.most_similar("박영선")

doc_tags = list(model.docvecs.doctags.keys())
X = model[doc_tags]
tsne = TSNE(n_components=2)
X_tsne = tsne.fit_transform(X)
df1 = pd.DataFrame(X_tsne, columns=['x', 'y'])
df1['label'] = news['sentiment']


# Apply the default theme
sns.set_theme()

# Create a visualization
sns.relplot(
    data=df1,
    x="x", y="y",
    hue="label", style="label"
)

#pca
X = model[doc_tags]
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
df2 = pd.DataFrame(X_pca, columns=['x', 'y'])
df2['label'] = news['sentiment']

# Apply the default theme
sns.set_theme()

# Create a visualization
sns.relplot(
    data=df2,
    x="x", y="y",
    hue="label", style="label"
)
