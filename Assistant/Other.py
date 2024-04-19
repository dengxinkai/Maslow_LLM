#V2 新建向量
vector_store = client.beta.vector_stores.create(
  name="理财产品详情"
)
print(vector_store)
#V2 删除向量
deleted_vector_store = client.beta.vector_stores.delete(
  vector_store_id="vs_IN2tYDmYrt6t0X1C18IjLLhX"
)
#V2 新建向量的文件
vector_store_file = client.beta.vector_stores.files.create(
  vector_store_id=vector_store.id,
  file_id=message_file.id
)
print(vector_store_file)
client.beta.vector_stores.files.list(
  vector_store_id=vector_store.id
).data
thread_sale = client.beta.threads.create(
)
message_sale = client.beta.threads.messages.create(
  thread_id="thread_GWJFzlZe5zsW0KK6X6SpAAH0",#thread.id,
  role="user",
  content="你好",
)
#列出assistant
client.beta.assistants.list(
    order="desc",
    limit="20",
).data

#生成回答
text_content = ""
stream = client.beta.threads.runs.create(
    thread_id=thread_sale.id,
    assistant_id=assistant_sale.id,
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

client.beta.threads.messages.list("thread_Qx999ZM9UYIIY4xyEg8Xa8ns").data

#删除assistant
response = client.beta.assistants.delete(assistant.id)
print(response)
