def update_fm_assistant(assistant_id, vector_store_id, assist_name, task, role, background, user, relationship_history, occasion, role_response, history):
    assistant = client.beta.assistants.update(
        assistant_id=assistant_id,
        tool_resources={"file_search": {"vector_store_ids": [vector_store_id]}},
        name=assist_name,
        instructions=f"""
        ## Goal
        你需要通过谈话完成任务{task}，但是{role}是个很难聊天的人，你需要尽可能的说正确的话来使ta满意，否则{role}会更加不满意。

        ## Introduction
        {role}的背景\n{background}
        {role}对用户的了解\n{user}
        谈话场合\n{occasion}
        """,
    )
    return assistant

def get_fm_help(thread_id, assistant_id,role,role_response,history,relationship_history):
  message = client.beta.threads.messages.create(
  thread_id=thread_id,#"thread_Qx999ZM9UYIIY4xyEg8Xa8ns"
  role="user",
  content=f"""
## Rules
* 每次根据{role}的的回复和回复里的要求\n{role_response}\n以及目前的关系\n{relationship}\n生成用户的回复。

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
      thread_id=thread_id,
      assistant_id=assistant_id,
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
