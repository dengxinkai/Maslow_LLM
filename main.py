# 开始游戏循环
#关系
relationships = [f"{role}喜欢用户",f"{role}非常厌恶用户",f"{role}不认识用户"] #关系
relationship = relationships[2]
relationship_history = []
relationship_history.append(relationship)
role_response = ""
history = f""
score = 20
print(f"{RED}{BOLD}  挑战：{task}。{RESET}")
print(f"{GREEN}{BOLD}{role}的背景{RESET}")
# print(f"性别：{sex}\n外貌：{appearance}\n年龄：{age}\n职业：{occupation}\n教育状况：{education}\n个人特质：{characteristic}\n兴趣：{interest}\n婚姻状况：{marriage}\n经济情况：{economic}\n健康状况：{health}\n心理状况：{mental}")#透明模式

print(f"性别：{sex}\n外貌：{appearance}\n年龄：***\n职业：***\n教育状况：***\n个人特质：***\n兴趣：***\n婚姻状况：***\n经济情况：***\n健康状况：***\n心理状况：***")#真实模式
print(f"{BLUE}{BOLD}{role}对用户的了解{RESET}")
print(f"{user}")
print(f'{CYAN}{BOLD}谈话场合{RESET}')
print(f'{occasion}')
history = f"你的任务：{task}\n"
ww = ""
print(f"{RED}{BOLD}你们的初始关系：{relationship}{RESET}")
while True:
    # 获取用户输入
    user_input = input(f"\n输入文字交谈，输入s求助销售经理，输入f求助理财经理，输入d让对方决策，输入q退出游戏\n")
    if user_input.lower() == 'q':
        print("模拟结束，谢谢您的参与！")
        break
    if user_input.lower() == 'd':
        print("对方开始决策...")
        decision(history,role,user,background,relationship_history,occasion,decide)
        break
    if user_input.lower() == 's':
        update_sale_assistant('asst_q9yTNWJvPZ7Mv4ihGFOkYxhS', sale_assist_name, task, role, background, user, relationship_history, occasion, role_response, history)
        user_input1 = get_sale_help("thread_GWJFzlZe5zsW0KK6X6SpAAH0",'asst_q9yTNWJvPZ7Mv4ihGFOkYxhS',role,role_response,history,relationship_history)
        user_input = re.search(r"用户说：([\w，。？！,.?!]+)", user_input1).group(1)
    if user_input.lower() == 'f':
        update_fm_assistant('asst_vVkQ5k14p8rm2iwH4GxuY07m', vector_store.id, assist_1, task, role, background, user, relationship_history, occasion, role_response, history)
        user_input1 = get_fm_help("thread_Qx999ZM9UYIIY4xyEg8Xa8ns",'asst_vVkQ5k14p8rm2iwH4GxuY07m',role,role_response,history,relationship_history)
        user_input = re.search(r"用户说：([\w，。？！,.?!]+)", user_input1.replace(" ", "")).group(1)
    history += f"用户说：{user_input}\n"
    # 调用函数并打印回复
    reply = task1(user_input, user,score,task,history,role,background,relationship_history,occasion)
    forgiveness_value = re.search(r"满意程度：(-?\d+)", reply)
    if forgiveness_value:
        score = int(forgiveness_value.group(1))
    else:
        score = 20
    role_response = re.search(r"说的话：([\w，。？！,.?!]+)", reply).group(1)
    relationship_update = re.search(r"关系更新：([\w，。？！,.?!]+)", reply)
    if relationship_update:
        relationship = relationship_update.group(1)
        relationship_history.append(relationship)
    reply += "\n"
    history += reply
    print(reply)
    if score < 1:
      ww = ending(history)
      break
    if score > 49:
      ww = ending(history)
      break
