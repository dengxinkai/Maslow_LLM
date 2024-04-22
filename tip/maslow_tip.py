# 展示task相关的马斯洛需求层级的tip
def maslow_tip(ww, role,task,background):
    a = ''
    completion = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {"role": "system", "content": f"""

##Introduction
{role}的背景：{background}
             
## Rules


## Output format
{role}关于{task}的需求等级：
1、生理需求（相关性：高、中、低）(解释）\n
2、安全需求（相关性：高、中、低）(解释）\n
3、社交需求（相关性：高、中、低）(解释）\n
4、尊重需求（相关性：高、中、低）(解释）\n
5、自我实现需求（相关性：高、中、低）(解释）
            """},
            {"role": "user", "content": ww}
        ],
        stream=True
    )
    for chunk in completion:
      content = chunk.choices[0].delta.content
      # 检查内容是否为None或空字符串
      if content and content.strip():
          print(content, end='')
          a += content
    print('\n')
    return a
