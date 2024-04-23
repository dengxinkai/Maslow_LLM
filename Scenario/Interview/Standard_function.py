# 正确定义generate_reply函数
def maslow_task1(ww, user,score,task,history,role,role_response,background,relationship_history,occasion):
    a = ''
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
* 每次生成用户对于完成\n{task}\n的成功概率估计：
* 0%为一定失败
  100%为一定成功

## Memory
之前的对话记录和满意程度，以及双方关系变化如下
{history}

## Output format
{role}心情：...
{role}说：...
得分：+-满意程度的变化
满意程度：更新的满意程度
{role}和用户的关系更新：...
{task}的成功概率：...
            """},
            {"role": "user", "content": ww}
        ]
    )
    a = completion.choices[0].message.content
    return a

def auto_chat(history,role,role_response,user,background,relationship_history,occasion,task):
    a = ""
    if role_response:
      completion = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {"role": "system", "content": f"""
## Goal
你需要通过谈话来改变{role}的马斯洛需求层级，从而完成任务\n{task}\n，但是{role}是个很难聊天的人，你需要尽可能的说正确的话来使ta满意，否则{role}会更加不满意。

##Introduction
{role}的背景\n{background}\n
{role}对用户的了解\n{user}\n
{role}和用户的关系变化历史\n{relationship_history}\n
谈话场合\n{occasion}\n

## Rules
* 每次根据{role}的的回复\n{role_response}\n，生成用户的回复。

## Memory
之前的对话记录和{role}的满意程度，以及双方关系变化如下\n{history}\n
             
## Output format
用户说：...

  """}
        ],
        stream=True
    )
      for chunk in completion:
        content = chunk.choices[0].delta.content
        if content and content.strip():
            print(f"{GRAY}{content}{RESET}", end='')
            a += content
      print('\n')
    else:
      completion = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {"role": "system", "content": f"""
## Goal
你需要通过谈话来改变{role}的马斯洛需求层级，从而完成任务\n{task}\n，但是{role}是个很难聊天的人，你需要尽可能的说正确的话来使ta满意，否则{role}会更加不满意。

##Introduction
{role}的背景\n{background}\n
{role}对用户的了解\n{user}\n
{role}和用户的关系变化历史\n{relationship_history}\n
谈话场合\n{occasion}\n

## Rules
* 根据{role}的背景、对用户的了解和之间的关系，生成用户对{role}的开场白。
             
## Output format
用户说：...

  """}
        ],
        stream=True
    )
      for chunk in completion:
        content = chunk.choices[0].delta.content
        if content and content.strip():
            print(f"{GRAY}{content}{RESET}", end='')
            a += content
      print('\n')

    return a
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
          print(f"{GRAY}{content}{RESET}", end='')
          a += content
    print('\n')
    return a

def ending(ww):
    a = ""
    completion = client.chat.completions.create(
        model="gpt-4-turbo-2024-04-09",
        messages=[
            {"role": "system", "content": f"""
            对话记录、满意程度以及双方关系变化如下：{ww}
            满意程度低于或等于0则谈话失败。
            如果失败，根据上面的对话总结出谈话失败的教训"""}
        ],
        stream=True
    )
    for chunk in completion:
      content = chunk.choices[0].delta.content
      # 检查内容是否为None或空字符串
      if content and content.strip():
          print(f"{GRAY}{content}{RESET}", end='')
          a += content
    print('\n')
    return a

def get_resume_help(role,role_response,history,relationship_history):
  if role_response:
    message = client.beta.threads.messages.create(
    thread_id='thread_aJpd9m93MQ8LpbG1jxMm5lJL',
    role="user",
    content=f"""
  ## Rules
  * 每次根据{role}的的回复和回复里的要求\n{role_response}\n以及目前的关系\n{relationship}\n生成用户的回复。

  {role}和用户的关系变化历史\n{relationship_history}\n

  ## Memory
  之前的对话记录和{role}的满意程度，以及双方关系变化如下\n{history}\n

  ## Output format
  用户说：...
    """,
  )
  else:
    message = client.beta.threads.messages.create(
    thread_id='thread_aJpd9m93MQ8LpbG1jxMm5lJL',
    role="user",
    content=f"""
  ## Rules
  * 根据{role}的背景、对用户的了解和之间的关系，生成用户对{role}的开场白。

  {role}和用户的关系变化历史\n{relationship_history}

  ## Memory
  之前的对话记录和{role}的满意程度，以及双方关系变化如下\n
  {history}

  ## Output format
  用户说：...
    """,
  )
  text_content = ""
  stream = client.beta.threads.runs.create(
      thread_id='thread_aJpd9m93MQ8LpbG1jxMm5lJL',
      assistant_id='asst_TsBVGRbE5ESfPZN1AzC4UGwj',
      tool_choice = {"type": "file_search"},
      stream=True
  )
  for event in stream:
      # 检查事件是否为ThreadMessageDelta，然后打印文本内容
      if 'ThreadMessageDelta' in str(event):
          message_deltas = event.data.delta.content
          for delta in message_deltas:
              if delta.type == 'text':
                  # 使用print函数的end参数来防止换行，并直接连续打印文本
                  if delta.text.annotations is None or not delta.text.annotations:
                    print(delta.text.value, end='')
                    text_content += delta.text.value
  return text_content
