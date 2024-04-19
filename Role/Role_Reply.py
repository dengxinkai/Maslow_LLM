# 正确定义generate_reply函数
def task1(ww, user,score,task,history,role,background,relationship_history,occasion):
    completion = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {"role": "system", "content": f"""

##Introduction
{role}的背景：{background}
{role}对用户的了解：{user}
{role}和用户的关系变化历史：{relationship_history}
谈话场合：{occasion}

## Rules
* 每次根据用户的回复，生成{role}的回复，回复的内容包括心情、满意程度和双方关系更新。
* 现有的满意程度为{score}，每次交互会增加或者减少满意程度。
* 每次用户回复的话请从-10到10分之间评分，1分为分值起伏：
* -10为最不满意
  0为正常
  +10为最满意

## Memory
之前的对话记录和满意程度，以及双方关系变化如下
{history}

## Output format
{role}心情：...
{role}说的话：...
得分：+-满意程度的变化
满意程度：更新的满意程度
{role}和用户的关系更新：...
            """},
            {"role": "user", "content": ww}
        ]
    )
    return completion.choices[0].message.content
