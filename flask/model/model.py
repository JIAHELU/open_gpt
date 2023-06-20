from config.model_config import *
from commons.get_logger import logger
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np


def str_to_array(s):
    # 去除字符串两端的方括号，并将字符串按空格分割为单个元素
    elements = s.strip("[]").split()
    # 将每个元素转换为float类型，并创建ndarray
    array = np.array([float(x) for x in elements])
    return array


def model_fun(search_Value, data):
    model = SentenceTransformer(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )
    logger.info(f"\n调用模型!!!!!输入：{search_Value}")
    query_embedding = model.encode([search_Value])
    print(type(query_embedding))

    if not hasattr(model_fun, "str_to_array_called"):
        # 第一次调用model_fun时调用str_to_array函数
        data["embedding"] = data["embedding"].apply(str_to_array)
        model_fun.str_to_array_called = True

    # 计算查询词与每个词的余弦相似度
    embeddings = np.vstack(data["embedding"].apply(lambda x: x[:]))
    similarities = np.dot(query_embedding, embeddings.T).flatten()

    # 根据相似度排序并选择前五个结果
    top_indices = np.argsort(similarities)[::-1][:5]
    top_words = data.loc[top_indices, "prompt"].values.tolist()
    return top_words


if __name__ == "__main__":
    print()
