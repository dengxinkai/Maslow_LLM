print(f"{BLUE}{BOLD}谈话任务：{task}。{RESET}")
print(f"{BLUE}{BOLD}{role}的背景{RESET}")
print(f"姓名：{name}\n性别：{sex}\n外貌：{appearance}\n年龄：{age}\n职业：{occupation}\n教育状况：{education}\n个人特质：{characteristic}\n兴趣：{interest}\n婚姻状况：{marriage}\n经济情况：{economic}\n健康状况：{health}\n心理状况：{mental}")#透明模式
# print(f"姓名：{name}\n性别：{sex}\n外貌：{appearance}\n年龄：***\n职业：***\n教育状况：***\n个人特质：***\n兴趣：***\n婚姻状况：***\n经济情况：***\n健康状况：***\n心理状况：***")#真实模式
print(f"{BLUE}{BOLD}{role}对用户的了解{RESET}")
print(f"{user}")
print(f'{BLUE}{BOLD}谈话场合{RESET}')
print(f'{occasion}')
print(f"{BLUE}{BOLD}你们的初始关系{RESET}")
print(f"{relationship}")

while True:
    user_input = input(f"输入文字交谈\n输入 a 自动聊天\n输入 s 求助销售经理，输入 f 求助理财经理\n输入 d 让对方决策\n输入 t 获取maslow_tip\n输入 q 退出\n")
    if user_input.lower() == 't':
        maslow_tip(ww, role,task,background)
    else:
      if user_input.lower() == 'a':
          user_input1 = auto_chat(history,role,role_response,user,background,relationship_history,occasion,task)
          user_input = re.search(r"用户说：([\w\s，。？（）()！,.?!【】{}]+)", user_input1)
          if user_input:
            user_input = user_input.group(1)
          else:
            user_input = user_input1
      if user_input.lower() == 'q':
          print("模拟结束，谢谢您的参与！")
          break
      if user_input.lower() == 'd':
          print("对方开始决策...")
          final_decision(history,role,maslow,user,background,relationship_history,occasion,decide)
          break
      if user_input.lower() == 's':
          update_sale_assistant('asst_q9yTNWJvPZ7Mv4ihGFOkYxhS', sale_assist_name, task, role, background, user, relationship_history, occasion, role_response, history)
          user_input1 = get_sale_help("thread_GWJFzlZe5zsW0KK6X6SpAAH0",'asst_q9yTNWJvPZ7Mv4ihGFOkYxhS',role,role_response,history,relationship_history)
          user_input = re.search(r"用户说：([\w\s，。？、（）()！,.?!【】{}]+)", user_input1)
          if user_input:
            user_input = user_input.group(1)
          else:
            user_input = user_input1
      if user_input.lower() == 'f':
          update_fm_assistant('asst_vVkQ5k14p8rm2iwH4GxuY07m', vector_store.id, assist_1, task, role, background, user, relationship_history, occasion, role_response, history)
          user_input1 = get_fm_help("thread_Qx999ZM9UYIIY4xyEg8Xa8ns",'asst_vVkQ5k14p8rm2iwH4GxuY07m',role,role_response,history,relationship_history)
          user_input = re.search(r"用户说：([\w\s，。？、（）()！,.?!【】{}]+)", user_input1.replace(" ", ""))
          if user_input:
            user_input = user_input.group(1)
          else:
            user_input = user_input1
      reply = maslow_task1(user_input, user,score,task,history,role,role_response,background,relationship_history,occasion)
      if reply == "拒绝":
        break
      history += f"用户说：{user_input}\n"
      # 调用函数并打印回复
      forgiveness_value = re.search(r"满意程度：(-?\d+)", reply)
      if forgiveness_value:
          score = int(forgiveness_value.group(1))
      else:
          score = 20
      role_response = re.search(r"说：(.*?)(?=得分：)", reply, re.DOTALL)
      if role_response:
        role_response = role_response.group(1)
      else:
        role_response = role_response
      # role_response = re.search(r"([^\n]+)", role_response)
      # if role_response:
      #   role_response = role_response.group(1)
      # else:
      #   role_response = role_response

      # maslow = re.search(fr"需求层级：(.*?)(?={role}心情：)", reply, re.DOTALL).group(1)
      relationship = re.search(fr"关系更新：(.*?)(?={task}的成功概率)", reply, re.DOTALL).group(1)
      relationship_history.append(relationship)
      reply += "\n"
      history += reply
      print(f'{CYAN}{reply}{RESET}')
      if score < 1:
        ww = ending(history)
        break
