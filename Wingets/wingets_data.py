import os
import sys
from dataclasses import dataclass
from random import randint
from Wingets import Wingets 

@dataclass
class winget_data:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))   
    wingets = [Wingets(name="Monitor De Sistema", path=os.path.join(BASE_DIR, "src_Wingets", "monitor_w.py"),ID=randint(0, 1000))]
