import pandas as pd
from sqlalchemy import create_engine
from google.cloud import translate_v2 as translate
import os

# 连接google.cloud翻译接口
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\prompt\cloud_translateAPI.json"


# def translate_text(text, target_language):
#     translate_client = translate.Client()
#     result = translate_client.translate(text, target_language=target_language)
#     return result["translatedText"]


# def translate_xlsx_file(input_file, output_file, target_language):
#     df = pd.read_excel(input_file)
#     df["描述翻译"] = df["description"].apply(lambda x: translate_text(x, target_language))
#     df["提示翻译"] = df["prompt"].apply(lambda x: translate_text(x, target_language))
#     df.to_excel(output_file, index=False)


# # 指定输入和输出文件路径
# input_file_path = "D:\\prompt\\prompt_for_sale.xlsx"
# output_file_path = "D:\\prompt\\prompt_for_sale.xlsx"

# # 指定目标语言代码
# target_language = "zh-CN"

# # 翻译并写入到输出文件
# translate_xlsx_file(input_file_path, output_file_path, target_language)

# 读取Excel文件
df = pd.read_excel(
    "D:\CScience\Git\OpenGpt\prompt.xlsx",
    usecols=[
        "id",
        "name",
        "icon",
        "demoInput",
        "prompt",
        "usedCount",
        "embedding",
        "createdAt",
        "updatedAt",
    ],
)

# 连接数据库
engine = create_engine("mysql://root:password@localhost:3306/app")

# 将数据存入数据库
df.to_sql("OpenGptApp", con=engine, if_exists="replace", index=False)

# 爬取数据存入xlsx文件
# import requests
# import pandas as pd
# from bs4 import BeautifulSoup

# # 发起请求获取网页内容
# url = "https://bestprompts.org/best-chatgpt-prompts-for-sales/"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
# }
# response = requests.get(url, headers=headers)
# html = response.text

# # 使用 BeautifulSoup 解析网页内容
# soup = BeautifulSoup(html, "html.parser")

# ul_tags = soup.find_all("ul")
# td_tags = soup.find_all("td")
# # p_tages = soup.find_all("p", attrs={"class": "class_name"})

# # 创建空的 DataFrame
# df = pd.DataFrame(columns=["prompt"])

# # 遍历每个 ul 标签并将内容写入 DataFrame
# for ul in ul_tags:
#     prompt_text = ul.get_text(separator="\n")
#     df = df.append({"description": prompt_text}, ignore_index=True)

# # 遍历每个 td 标签并将内容写入 DataFrame
# for td in td_tags:
#     prompt_text = td.get_text(separator="\n")
#     df = df.append({"prompt": prompt_text}, ignore_index=True)

# # 保存到文件
# df.to_excel("D:\\prompt\\prompt_for_sale.xlsx", index=False)

# 数据清洗步骤
# df = pd.read_excel("D:\\prompt\\prompt_for_stable_diffusion.xlsx")
# df["prompt"] = df["prompt"].replace(r"Prompt: ", "", regex=True)  # 去除中文冒号后的换行
# df["prompt"] = df["prompt"].replace(r"[\u0031-\u0039\uFE0F\u20E3\U0001F51F]", "", regex=True)  # 去除中文冒号后的换行
# df["prompt"] = df["prompt"].replace(r"^\s+", "", regex=True)  # 去除中文冒号后的换行
# df.to_excel(
#     "D:\\prompt\\prompt_for_stable_diffusion.xlsx", index=False
# )
