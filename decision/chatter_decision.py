def final_decision(history,role,maslow,user,background,relationship_history,occasion,decide):
    a = ""
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
* 根据之前的对话记录和满意程度，结合{role}的背景和对用户的了解，最重要是根据{role}的马斯洛需求层次\n{maslow}\n,生成{role}关于\n{decide}\n的决定。

## Memory
之前的对话记录和满意程度，以及双方关系变化如下\n{history}\n

## Output format
{role}决定：...\n
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
