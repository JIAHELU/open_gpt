import sys

sys.path.insert(0, sys.path[0] + "/../")
import traceback
from datetime import datetime
from flask import Flask, request, jsonify
from commons.get_logger import logger, args
from model.model import *
from flask_cors import CORS
from sqlalchemy import create_engine
import json


embedding_sort = Flask("sort")
CORS(embedding_sort)
embedding_sort.config["JSON_AS_ASCII"] = False  # 保证返回的json编码正确


engine = create_engine(DATABASE_URL, execution_options={})
appData = pd.read_sql("OpenGptApp", con=engine)
print(appData)


@embedding_sort.route(sort_path, methods=["POST"])
def search_embedding():
    try:
        request_id = f"request_{datetime.now().strftime('%Y%m%d_%H%M%S%f')}"
        # 获取数据
        data = request.get_json()
        search_Value = data.get("search_Value")

        # 解析数据
        if search_Value is None:
            logger.info(f"{request_id}:请输入必填参数：content")
            return jsonify(status=112001, msg="请输入必填参数：content")

        # 调用模型
        logger.info(f"{request_id}:\ncontent:{search_Value}")
        result = model_fun(search_Value, appData)
        logger.info(f"{request_id}:\nresult:{result}")
        return jsonify(result)

    except:
        logger.info(f"{request_id}:\n错误信息: {traceback.format_exc()}")
        return jsonify({"status": "112001", "message": "fail"})


@embedding_sort.route(calculate_path, methods=["POST"])
def calculate_embedding():
    try:
        request_id = f"request_{datetime.now().strftime('%Y%m%d_%H%M%S%f')}"
        # 获取数据
        data = request.get_json()
        prompt = data.get("prompt")

        if prompt is None:
            logger.info(f"{request_id}:请输入必填参数：content")
            return jsonify(status=112001, msg="请输入必填参数：content")

        # 调用模型
        model = SentenceTransformer(
            "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
        )
        logger.info(f"{request_id}:\ncontent:{prompt}")
        result = model.encode(prompt)
        res_list = result.tolist()
        res_json = json.dumps(res_list)
        logger.info(f"{request_id}:\nresult:{res_json}")
        return jsonify({"embeddingValue": res_json})

    except:
        logger.info(f"{request_id}:\n错误信息: {traceback.format_exc()}")
        return jsonify({"status": "112001", "message": "fail"})


if __name__ == "__main__":
    embedding_sort.run(host="0.0.0.0", port=port)
