from typing import List
import qianfan
from langchain_community.chat_models import QianfanChatEndpoint

from api_secret_key import API_Key, API_SECRET
import os
os.environ["QIANFAN_AK"] = API_Key
os.environ["QIANFAN_SK"] = API_SECRET


# 使用文心一言模型
def chat_with_qianfan() -> QianfanChatEndpoint:
    """For basic init and call"""
    chat = QianfanChatEndpoint(streaming=True,  # 是否使用流式模式
                               model="ERNIE-Bot-turbo",  # 使用的模型
                               **{"top_p": 0.8, "temperature": 0.95, "penalty_score": 1}  # 模型参数
    )
    return chat

def call_chat_model(messages: List[dict]) -> str:
    client = qianfan.ChatCompletion()  # 创建客户端
    response = client.do(  # 调用模型
        model="ERNIE-Bot-turbo",
        messages=messages,
    )
    return response.body['result']  # 返回结果

def invoke_chain(topic: str) -> str:
    prompt_template = "Tell me a short joke about {topic}"
    prompt_value = prompt_template.format(topic=topic)  # 定义prompt
    messages = [{"role": "user", "content": prompt_value}]  # 定义消息
    return call_chat_model(messages)  # 调用模型

def invoke_with_qianfan() -> str:
    response = invoke_chain("ice cream")
    print(response)
    return response


if __name__ == "__main__":
    invoke_with_qianfan()