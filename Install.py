%%capture
!pip install openai --quiet
import os
from typing_extensions import Annotated
from google.colab import userdata
llm_config = {"config_list": [{"model": "gpt-4-turbo-2024-04-09", "api_key": userdata.get('api')}]}
config_list=[{"model": "gpt-4-turbo-2024-04-09", "api_key": userdata.get('api')}]
from typing import Literal
from pydantic import BaseModel, Field
from typing_extensions import Annotated
from openai import OpenAI
import re
from google.colab import files
import os
# 假设您已经正确设置了userdata来获取API密钥
client = OpenAI(api_key=userdata.get('api'))
# 定义颜色
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"
BOLD = "\033[1m"
PURPLE = "\033[35m"
GRAY = "\033[90m"
ORANGE = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
