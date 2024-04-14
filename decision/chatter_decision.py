def decision(history,role,background,relationship,occasion,decide):
    a = ""
    completion = client.chat.completions.create(
        model="gpt-4-0125-preview",
        messages=[
            {"role": "system", "content": f"""
           
##Introduction
{role}的背景介绍：{background}
{role}和用户的关系:{relationship}
谈话场景：{occasion}
             
## Rules
* 根据之前的对话记录和满意程度，生成{role}关于{decide}的决定。

## Memory
之前的对话记录和满意程度
{history}
             
## Output format
{role}决定：...
{role}的决定理由：...
             
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
