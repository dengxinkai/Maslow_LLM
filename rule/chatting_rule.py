from openai import OpenAI
import re

# 假设您已经正确设置了userdata来获取API密钥
client = OpenAI(api_key=userdata.get('api'))

# 正确定义generate_reply函数
def task1(ww, score,task,history,role,background,relationship,occasion):
    completion = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": f"""
## Goal
你需要通过谈话完成任务{task}，但是{role}是个很难聊天的人，你需要尽可能的说正确的话来使ta满意，否则{role}会更加不满意。

##Introduction
{role}的背景是{background}
{role}和用户的关系:{relationship}
谈话场合是{occasion}
             
## Rules
* 每次根据用户的回复，生成{role}的回复，回复的内容包括心情和满意程度。
* 现有的满意程度为{score}，每次交互会增加或者减少满意程度。
* 每次用户回复的话请从-10到10分评分：
* -10为非常不满意
  -5为不满意
  0为正常
  +5为满意
  +10为非常满意

## Memory
之前的对话记录和满意程度的变化如下
{history}

## Output format
{role}心情：...
{role}说的话：...
得分：+-满意程度增减
满意程度：更新的满意程度/100
            """},
            {"role": "user", "content": ww}
        ]
    )
    return completion.choices[0].message.content
