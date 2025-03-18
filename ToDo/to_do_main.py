import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tool import tool
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import data
from to_do_tool import to_do_tool
import asyncio

def To_Do_Main(data_Local:data):
    print("_"*30 + " To Do "+"_"*30)
    tool.menu(data_Local)
    print(f"Tarefas: ")
    to_do_tool.Show_Menu_Task(data.Tasks_to_do)
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")
    c = input("Digite Sua Resposta: ").strip().lower()
    if c == "1":
        if to_do_tool.Add_Task() == None:
            To_Do_Main(data_Local=data_Local)
            return
        
    elif c == "2":
        if to_do_tool.Remove_Task() == None:
            To_Do_Main(data_Local=data_Local)
            return
    elif c == "3":
        to_do_tool.Show_Task_Pendentes()
        To_Do_Main(data_Local=data_Local)
        return
    elif c == "4":
        if data_Local.Debug:print("Fechando To_Do")
        return
    else:
        To_Do_Main(data_Local=data_Local)
        return


if data.Debug:
    print("Iniciando To_Do_Main...")
To_Do_Main(data)