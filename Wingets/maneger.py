import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tool import tool
from wingets_tool import winget_tool
from wingets_data import winget_data

data_local = data()

def activeWingets():
    tool.menu(data)
    winget_tool.showWingets(winget_data)


