import os
import platform
from dataclasses import dataclass
import subprocess
import sys
from data import data
import winotify
import threading
import asyncio
import signal
from requests import get
from time import sleep
from datetime import datetime

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    def verify_modules():
        if data.modules == None:return
        try:
            for i in data.modules:
                os.system(f"pip3 install {i}")
            return
        except Exception as E:
            print(f"Erro Na Verificaçao De Modulos, Erro: {E}")
            return
        
    def add_path_modules(data_local:data):
        if data.modules_local == None:return
        try:
            for i in data.modules_local:
                sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), i)))
                if data_local.Debug:print(f"Module_local: {i}")
            return
        except Exception as E:
            print(f"Erro Al Adicionar Os Caminhos Brutos, Erro: {E}")
            return
                            
    
    @staticmethod
    def Notification(name:str,descri:str):
        try:
            current_dir = os.path.dirname(os.path.abspath(__file__))
            icon_path = os.path.join(current_dir, 'icons', 'icon.png')
            
            if not os.path.exists(icon_path):
                print(f"Ícone encontrado: {os.path.exists(icon_path)}")
                return None

            notification = winotify.Notification(
                app_id="Germinare TECH",
                title=name,
                msg=descri,
                icon=icon_path
            )
            notification.set_audio(winotify.audio.Default, loop=False)
            notification.add_actions(
                label="Odette",
                launch= data.Odette_URL
            )
            notification.show()
        except Exception as e:
            print(f"Erro ao exibir a notificação: {e}")
            return None

    def start_tread(fuction,parameter):
        if not isinstance(parameter, tuple):
            parameter = (parameter,) 
        tread = threading.Thread(target=fuction,args=parameter)
        tread.daemon = True
        tread.start()
        return tread
    
    def Retun_reponse(url):
        tool.clear_screen()
        try:
            reponse = get(url)
        except Exception as e:
            print(f"Erro ao tentar acessar a URL: {url}\n"
            "Possíveis causas:\n"
            "- A URL pode estar incorreta ou malformada.\n"
            "- O site pode estar fora do ar ou com problemas de conexão.\n"
            "- Verifique sua conexão com a internet.\n"
            f"Detalhes técnicos do erro: {e}")
            sleep(5)
            return

        print(f"resposta do server: {reponse}")
        sleep(5)
        return
     
    def start_alert_process(data_Local:data):
        try:
            alert_sub = subprocess.Popen(["python", "alert.py"], creationflags=subprocess.CREATE_NO_WINDOW)
            data_Local.alert_pid = alert_sub.pid # Armazena o PID
            if data_Local.Debug: 
                print("🚀 alert.py iniciado!") # Este print foi colocando somente para use dev trocando no score code 
                print(f"Subprosses Info: {subprocess.PIPE} \n PID: {alert_sub.pid}")


        except Exception as E:
            print(f"Erro Al Inicar Subporsses , Erro: {E}\n")
            print(f"Subprosses Info: {subprocess.PIPE}")
            sleep(5)
            return
        
    def is_alert_running(PID:int):
        if data.OS_client == "Windows": 
            process = subprocess.run(
                ["powershell", "-Command", f"Get-Process -Id {PID}"],
                capture_output=True, text=True
            )
            return 'alert.py' in process.stdout
        else:
            # Em sistemas Unix, usa-se o pgrep
            return subprocess.call(['pgrep', '-f', 'alert.py']) == 0

    
    @staticmethod
    def alert_to_to_assess_classroom(data_local:data):
        try:
            hour = datetime.now().strftime("%H")
            minutes = datetime.now().strftime("%M")

            #if (int(hour), int(minutes)) not in data.date or not (7 <= int(hour) <= 14):return

            if data_local.Debug:
                print(f"Hour: {hour}, Min: {minutes}")
                print(f"Debug + Data armazenada: {data_local.date}")
                print(f"Debug + Comparando com: {(hour, minutes)}")

            try:
                if (int(hour),int(minutes)) in data_local.date:
                    if data_local.Debug:print("🔔 Notificaçao!")
                    tool.Notification(name="Avalie A Aula !!!",descri="Avalie A Aula !!!")
            except Exception as E:
                print(f"Erro Al Verificar Horario: {E}")

            if data_local.Debug:
                print(f"Hour: {hour}, Min: {minutes}")
                print(f"Debug + Data armazenada: {data_local.date}")
                print(f"Debug + Comparando com: {(hour, minutes)}")
        except Exception as E:
            print(f"Erro Al Inicar Loop De Verificaçao, Eroo: {E}")
            return
    
    exit_progarm = lambda PID: os.kill(PID,9) 
        
    def format_dates(data_local:data):
        formatted_date = []
        for i in data_local.date:
            if isinstance(i, float): #isinstance usado para verificar type
                hour = int(i)
                minutes = int((i % 1) * 60)
                formatted_date.append((hour, minutes))
            elif isinstance(i, tuple):
                formatted_date.append(i)
            else:
                print(f"Item inesperado encontrado: {i}")

        data_local.date = formatted_date  
            
    def menu(data_Local:data):
        tool.clear_screen()
        print("_"*30 + data_Local.name + "_"*30)
        print(f"{data.day}/{data.mes}/{data.ano}")
        print(f"Sistema Operacional: {data.OS_client}")
        if data_Local.Debug:print("🖥️"+"  "+ f"alert.py: PID: {data_Local.alert_pid}")
        if data_Local.Debug:print("🔧 Dev Mode")
        print("_"*73)
        return

    def change_app_name(data_local:data):
        try:
            tool.clear_screen()
            name = str(input("Digite O Nome Do App: "))
            print("Nome Trocado Com Susseso! ")
            sleep(2)
            data_local.name = name
            return
        except Exception as E:
            print(f"Erro Al Trocar O Nome Do App, Erro: {E}")
            sleep(5)
            return
    
    def start_web(url:str,data_local:data):
        try:
            if data_local.Debug:
                try:
                    print("requet URL: "+ str(get(url=url)))
                    print(f"URL: {url}")
                except Exception as E:
                    print("Erro Na Requisao HTTPS Da URL!")
                    print(f"Erro: {E}")

            subprocess.run(["cmd", "/c", "start", url], shell=True)
            return
        except Exception as E:
            print(f"Erro Al Inicar Site, Erro: {E}")
            return
    

    #Dev Function
    async def start_exit_systhen(data_local:data):
        signal.signal(signal.SIGINT, lambda signum, frame: tool.exit_progarm(data_local))
        return
              
    async def show_clock():
        while True:
            tool.clear_screen()
            print(f"Horario: {datetime.now().strftime("%H:%M:%S")}")
            await asyncio.sleep(1)
        return