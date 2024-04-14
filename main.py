print(f"{RED}{BOLD}  挑战：{task}。{RESET}")
print(f"{GREEN}{role}的背景：{background}{RESET}")
print(f"{PURPLE}{role}和你的关系：{relationship}{RESET}")
print(f'{GRAY}谈话场合：{occasion}{RESET}')
history = f"你的任务：{task}\n"
ww = ""
while True:
    # 获取用户输入
    user_input = input(f"继续交谈，输入d让对方决策，输入q退出游戏\n")
    history += f"用户说：{user_input}\n"
    if user_input.lower() == 'q':
        print("游戏结束，谢谢您的参与！")
        break
    if user_input.lower() == 'd':
        print("对方开始决策...")
        decision(history,role,background,relationship,occasion,decide)

        break
    
    # 调用函数并打印回复
    reply = task1(user_input, score,task,history,role,background,relationship,occasion)
    forgiveness_value = re.search(r"满意程度：(-?\d+)", reply)
    if forgiveness_value:
        score = int(forgiveness_value.group(1))
    else:
        score = 20
    reply += "\n"
    history += reply
    print(reply)
    if score < 1:
      ww = ending(history)
      break
    if score > 49:
      ww = ending(history)
      break
