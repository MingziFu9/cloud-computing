"""实验 3-2：调用阿里云百炼的大模型 API（模型即服务 MaaS）。

准备：在阿里云百炼控制台开通服务、创建 API Key，然后在终端设置环境变量：
    Linux / macOS：export DASHSCOPE_API_KEY="sk-你的密钥"
    Windows：      set DASHSCOPE_API_KEY=sk-你的密钥
安装依赖：pip install openai
运行：python lab3_2_bailian.py
"""
import os
import time

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"),                          # 不要把密钥直接写在代码里
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",    # 百炼的 OpenAI 兼容接口
)

question = "用三句话向零基础的同学解释什么是云计算的按需付费。"
start = time.time()
resp = client.chat.completions.create(
    model="qwen-plus",                                               # 通义千问模型，可在百炼“模型广场”查看其他模型名
    messages=[
        {"role": "system", "content": "你是一位耐心的云计算课程助教。"},
        {"role": "user", "content": question},
    ],
)
print("问题：", question)
print("回答：", resp.choices[0].message.content)
print(f"用时 {time.time() - start:.1f} 秒")
print("本次消耗的 token：输入", resp.usage.prompt_tokens, "，输出", resp.usage.completion_tokens)
