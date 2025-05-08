import os
import sys
# from wingets_data import winget_data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tool import tool
from dataclasses import dataclass
from random import randint
from wingets_data import winget_data
from Wingets import Wingets 

@dataclass
class winget_tool:
    def showWingets(data_local):
        for i in data_local.wingets:
            print(f"ID   : {i.ID}")
            print(f"Nome : {i.name}")
            print(f"Path : {i.path}")
            print("-" * 30)

    def getWinget(id: int, data_local:winget_data) -> Wingets:
        for i in data_local.wingets:
            if i.ID == id:
                return i 
        return None
    
    #Refatorado Do Modulo ToDo
    def Find_WingetByID(arry: list, target: int):
        low_value = 0
        high_value = len(arry) - 1

        while low_value <= high_value:
            med = (low_value + high_value) // 2
            find_value = arry[med]
            task_id = find_value.id_task

            if data.Debug:
                print(f"low_value: {low_value}")
                print(f"high_value: {high_value}")
                print(f"med: {med}")

            if task_id == target:
                return target
            elif task_id > target:
                high_value = med - 1
            else:
                low_value = med + 1

        return None