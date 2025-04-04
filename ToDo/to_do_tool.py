import os
import sys
from dataclasses import dataclass
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tool import tool 
from to_do_class import to_do_class
from time import sleep
from winotify import Notification
from random import randint
import asyncio
import threading

@dataclass
class to_do_tool:
    def Add_Task(): 
        tool.clear_screen()
        name_task = input("Digite O Nome Da Task: ")
        if name_task.strip() == "":return
        descr_task = input("Digite A Descriçao De Sua Task: ")
        
        time_notificate = input("Digite O Tempo De Espera Da Notificaçao (M): ")
        time = float(time_notificate)
        time = time * 60.0 

        id_task = randint(0,10000)
        task = to_do_class(name_task=name_task,descri_task=descr_task,timer=time,state=False,id_task=id_task)
        tool.clear_screen()

        data.Tasks_to_do.append(task)
        print("Tarefa Adicionada Com Susseso!")

        loop = asyncio.get_event_loop()
        loop.run_in_executor(None, to_do_tool.task_timer, task)    

        return 

    
    def Remove_Task():
        tool.clear_screen()

        for i in data.Tasks_to_do:print(f"Nome: {i.name_task} | Status: {i.state} | ID: {i.id_task}")

        id_task = input("Digite O ID Da Task: ")
        task = to_do_tool.Find_Task(id_task)
        if task == None:
            print("Tarefa Nao Pode Ser Encotrada!")
            sleep(2)
            return
        
        data.Tasks_to_do.remove(task)
        tool.clear_screen()
        print("Tarefa Removida Com Susseso!")
        return 
    
    @staticmethod
    def task_timer(task:to_do_class):
        while task.timer > 0 and not task.state:
            task.timer -= 1.0
            #if data.Debug: print(f"Task {task.name_task}: tempo restante: {task.timer}s")
            sleep(1) 

        tool.Notification(name=task.name_task,descri=task.descri_task)
        task.state = True
    
    def Show_Menu_Task(task:to_do_class):
        for tarefa in task:
            status = "Concluída" if tarefa.state else "Pendente"
            print(f"Nome: {tarefa.name_task} | Status: {status}")
        

    def Show_Task_Pendentes():
        tool.clear_screen()
        if len(data.Tasks_to_do) == 0:
            print("Nenhuma tarefa encontrada!")
        
        for task in data.Tasks_to_do:
            print(f"Nome: {task.name_task} | Tempo: {task.timer}s | Status: {task.state} | ID: {task.id_task}")
        input("Pressione Enter para voltar ao menu.")
        return
        
    #Implementar Pesquisa Binaria
    # def Find_Task(name_task):
    #     for i in data.Tasks_to_do:
    #         if i.name_task == name_task:
    #             return i
    #     return None
    
    def Find_Task(id:str):
        if id.strip().split() == "":return None
        low_value = 0
        hight_value = len(data.Tasks_to_do) - 1
        id = int(id)

        data.Tasks_to_do.sort(key=lambda task: task.id_task) #tarforma por meio de uma lambda todos elementos em int cujo sao IDs

        while low_value <= hight_value:
            med = int((low_value + hight_value) //2)
            find_value = data.Tasks_to_do[med]
            task_id = int(find_value.id_task) 

            if data.Debug:
                print(f"low_value: {low_value}")
                print(f"high_value: {hight_value}")
                print(f"med: {med}")

            if task_id == id:
                return find_value
            if task_id > id:
                hight_value = med -1
            else:
                low_value = med + 1

        return None
