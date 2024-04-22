def decision_to_talk(ww,role,user,background,relationship,occasion):
    a = ""
    completion = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {"role": "system", "content": f"""

##Introduction
{role}的背景：{background}
{role}对用户的了解：{user}
{role}和用户的关系初始关系：{relationship}
谈话场合：{occasion}

## Rules
* 根据{role}的背景、对用户的了解、两者之间的关系、谈话场景和用户的开场白\n{ww}\n最重要是根据{role}的马斯洛需求层次,生成{role}关于是否与用户交谈的决定。


## Output format
{role}决定：接受或者拒绝
{role}的决定理由：结合郑总的马斯洛需求层级说明作出上述决定的理由

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
