import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tool import tool
from dataclasses import dataclass
from wingets_data import winget_data

@dataclass
class winget_tool:
    def showWingets(data_local:winget_data):
        for i in data_local:
            print(i)