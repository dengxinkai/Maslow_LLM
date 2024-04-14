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
