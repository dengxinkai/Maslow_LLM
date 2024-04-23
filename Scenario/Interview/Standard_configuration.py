assist_1 = "理财经理"
sale_assist_name = "销售经理"
role = "面试官" #谈话对象
user = "用户是一个大三新生，正在找实习"
#role有关的主观因素
name = "杨丹,"
sex = "男,"
appearance = "小帅，身高182,"
age = "40岁,"
occupation = "chait公司副总裁，chait公司是一家中国的上市公司，主要是做在线传媒的,"
education = "清华大学土木工程研究生毕业,"
characteristic = "乐观,"
interest = "非常好色,对美女感兴趣," #谈话对象的兴趣
marriage = "已婚，老婆很漂亮，有一个7岁的小男孩,"
economic = "现金存款30万，房产价值400万（贷款300万），股权估值300万,"
health = "有胃病，"
mental = "最近很郁闷，因为夫妻生活不和谐,"
background = name + sex + appearance + age + occupation + education + characteristic + interest + marriage + economic + health + mental#谈话对象的背景介绍
#参与者有关的客观因素
medium = f"方式：boss直聘邀约面试的\n"
time = f"时间：下午2点\n"
place = f"地点：公司里办公室"
occasion = medium + time + place#谈话场景
#关系
task = f"面试成功，获得{role}的offer" #挑战
decide = "是否给用户offer"
maslow = ""
relationship = f"{role}第一次见用户"
relationship_history = [relationship]
role_response = ""
history = f""
score = 20
ww = ""
history = f""
