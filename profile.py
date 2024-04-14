%%capture
!pip install pyautogen --quiet
import os
from typing_extensions import Annotated
import autogen
from google.colab import userdata
llm_config = {"config_list": [{"model": "gpt-4-0125-preview", "api_key": userdata.get('api')}]}
config_list=[{"model": "gpt-4-0125-preview", "api_key": userdata.get('api')}]
from typing import Literal
from pydantic import BaseModel, Field
from typing_extensions import Annotated
from autogen.cache import Cache
# 定义颜色
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BOLD = "\033[1m"
PURPLE = "\033[35m"
GRAY = "\033[90m"
ORANGE = "\033[33m"

#参与者有关的主观因素
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
background = sex + appearance + age + occupation + education + characteristic + interest + marriage + economic + health + mental#谈话对象的背景介绍
#参与者有关的客观因素
time = "晚上7点，"
place = "某个酒吧，"
medium = "偶遇，非正式的当面聊天"
occasion = time + place + medium#谈话场景


score = 20
role = "郑总" #谈话对象
task = f"销售一款理财产品给{role}" #挑战
relationship = "你们的关系非常好" #关系
decide = "是否购买理财产品"
