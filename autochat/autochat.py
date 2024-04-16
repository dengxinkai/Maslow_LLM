def auto_chat(history,role,role_response,user,background,relationship_history,occasion,task):
    a = ""
    completion = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {"role": "system", "content": f"""
## Goal
你需要通过谈话完成任务{task}，但是{role}是个很难聊天的人，你需要尽可能的说正确的话来使ta满意，否则{role}会更加不满意。

##Introduction
{role}的背景：{background}
{role}对用户的了解：{user}
{role}和用户的关系变化历史：{relationship_history}         
谈话场合：{occasion}
             
## Rules
* 每次根据{role}的的回复{role_response}，生成用户的回复。

## Memory
之前的对话记录和{role}的满意程度，以及双方关系变化如下
{history}
## Output format
用户说：...         

  """}
        ],
        stream=True
    )
    for chunk in completion:
      content = chunk.choices[0].delta.content
      if content and content.strip():
          print(content, end='')
          a += content
    print('\n')
    return a
