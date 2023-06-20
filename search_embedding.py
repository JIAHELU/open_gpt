from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np


model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

df = pd.read_csv(
    "D:\\CScience\\Git\\semantic-search-frontend\\fed_embeddings.csv",
    index_col=False,
    header=None,
    encoding="gbk",
)
df.columns = ["text"]
df = df.loc[0:200, :]
# 提取文本列
# 在 DataFrame 中添加一个空的列 'embedding'
df["embedding"] = ""
# 使用 sentence-transformers 生成嵌入向量并存入 'embedding' 列
for index, row in df.iterrows():
    text = row["text"]
    # 使用 sentence-transformers 进行嵌入向量的转换
    embedding = model.encode([text])
    embedding = embedding.tolist()
    print(type(embedding))
    # 将嵌入向量存入 'embedding' 列
    df.at[index, "embedding"] = embedding[0]

df.to_csv(
    "D:\\CScience\\Git\\semantic-search-frontend\\fed_embeddings.csv",
    index=False,
    encoding="gbk",
)
