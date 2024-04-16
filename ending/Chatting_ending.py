def ending(ww):
    a = ""
    completion = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {"role": "system", "content": f"""
            对话记录、满意程度以及双方关系变化如下：{ww}
            直到满意程度超过49，游戏通关，满意程度低于或等于0则谈话失败。
            如果通关，根据上面的对话总结出谈话成功的经验，如果失败，根据上面的对话总结出谈话失败的教训"""}
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
