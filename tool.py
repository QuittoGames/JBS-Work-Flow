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
import subprocess
import atexit
from psutil import pid_exists
import pyautogui as pg
import numpy as np
import cv2
import mss

@dataclass
class tool:
    def clear_screen():
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
    
    async def verify_modules():
        try:
            # #Uso Do modules por txt
            req_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "modules", "requirements.txt"))
            subprocess.run([sys.executable, "-m", "pip", "install", "-r", req_path], check=True)

            #Teste De Novo metodo de instaçao de modulos
            # for module in data.modules:
            #     try:
            #         __import__(module)
            #     except ImportError:
            #         subprocess.run([sys.executable, "-m", "pip", "install", module])
            # return
        
        except Exception as E:
            print(f"Erro Na Verificaçao De Modulos, Erro: {E}")
            return
        
    async def add_path_modules(data_local:data):
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
                    tool.AutoGui_classrom_altert(data_local)
            except Exception as E:
                print(f"Erro Al Verificar Horario: {E}")

            if data_local.Debug:
                print(f"Hour: {hour}, Min: {minutes}")
                print(f"Debug + Data armazenada: {data_local.date}")
                print(f"Debug + Comparando com: {(hour, minutes)}")
        except Exception as E:
            print(f"Erro Al Inicar Loop De Verificaçao, Eroo: {E}")
            return

    exit_progarm = lambda PID: os.kill(PID,signal.SIGTERM) 

        
    async def format_dates(data_local:data):
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

    @staticmethod
    def Finda_img(target, confianca=0.8):
        print(f"Procurando a imagem: {target}")
        with mss.mss() as sct:
            screenshot = np.array(sct.grab(sct.monitors[1]))
            screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

            imagem = cv2.imread(target)
            if imagem is None:
                print("Erro: imagem não encontrada no caminho fornecido.")
                return None

            resultado = cv2.matchTemplate(screenshot, imagem, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

            print(f"Confiança detectada: {max_val}")

            if max_val >= confianca:
                centro_x = max_loc[0] + imagem.shape[1] // 2
                centro_y = max_loc[1] + imagem.shape[0] // 2
                print(f"Imagem encontrada! Coordenadas: ({centro_x}, {centro_y})")
                return centro_x, centro_y
            else:
                print("Imagem não encontrada com confiança suficiente.")
                return None
            
    def PyAutoGui_script():
        #Code By Mega Ninja Padovani
        try:
            # tool.start_web(url=data_local.Odette_URL, data_local=data_local)
            tool.Notification(name="NÃO mexa no seu PC",descri="vamos começar a autoavaliação")
            sleep(15)
            pg.press('win')
            sleep(1)
            pg.write("crome")
            sleep(0.5)
            pg.press('enter')
            sleep(2)
            pg.write("https://alunos.igerminare.org.br/")
            sleep(0.5)
            pg.press('enter')
            return
        except Exception as E:
            print(f"Erro Al Execultar Script De PyAutoGui, Erro: {E}")
            return

            
    def AutoGui_classrom_altert(data_local:data):
        if not data_local.script_auto_gui:return
        try:
            #Code By Mega Ninja Padovani
            tool.PyAutoGui_script()
            # Procurando a imagem com a nova função
            postion = tool.Finda_img("icons/5_estrelas.png", confianca=0.7)
            if data_local.Debug:print("Valor da variável posicao:", postion)

            if postion:
                if data_local.Debug:print("Achei a imagem! Vou continuar o processo...")
                pg.click(x=1087, y=550)  # Clicar nas estrelas
                sleep(1)
                pg.click(x=941, y=877)  # Clicar no botão de avaliar
                return
            
            if data_local.Debug:print("Não achei a imagem! Vou mandar notificação...")
            tool.Notification(name="Avaliçao De Aula",descri="Erro Avaliar A Aula, Provavelmente O Profesor Nao Abriu A Aula")
            return
                        
        except Exception as E:
            print(f"Erro Al Execultar Altomaçao, Erro: {E}")

    def reset_altert_prosses(data_local:data):
        if data_local.alert_pid == 0: return
        try:
            tool.exit_progarm(data_local.alert_pid)
            if data_local.Debug:print(f"Prosseso alert.py com PID: {data_local.alert_pid} Foi Finlizado Com Susseso!")
            data_local.alert_pid = 0
            new_prosses = tool.start_alert_process(data_local)
            return 
        except Exception as E:
            print(f"Erro Al renicar O Prosseso, Erro: {E}")
            return

    def menu(data_Local:data):
        tool.clear_screen()
        print("_"*30 + data_Local.name + "_"*30)
        print(f"{data.day}/{data.mes}/{data.ano}")
        print(f"Sistema Operacional: {data.OS_client}")
        if data_Local.Debug:print("🖥️"+"  "+ f"alert.py: PID: {data_Local.alert_pid}")
        if data_Local.Debug:print("🖥️" +"  "+ f"Script Auto Gui: {data_Local.script_auto_gui}")
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

    # Ja ta ficado Progrmaçao Orientada A Gambiarra
    async def start_exit_systhen(data_local:data):
        async def exit_handler():
            """Chamado antes de o programa fechar"""
            if data_local.alert_pid is not None:
                if pid_exists(data_local.alert_pid): 
                    try:
                        await tool.exit_progarm(data_local.alert_pid)
                    except ProcessLookupError:
                        print(f"⚠️ Process {data_local.alert_pid} já foi encerrado.")
                    except PermissionError:
                        print("⚠️ Sem permissão para encerrar o processo.")
                    except Exception as e:
                        print(f"❌ Erro ao encerrar processo: {e}")
            else:
                print("⚠️ Nenhum PID válido para encerrar.")

        def sync_exit_handler(signum, frame):
            """Adaptador para sinais, chama a função assíncrona corretamente"""
            asyncio.get_event_loop().create_task(exit_handler())

        # Configura sinais corretamente
        signal.signal(signal.SIGINT, sync_exit_handler)
        signal.signal(signal.SIGTERM, sync_exit_handler)

        # Executa exit_handler ao sair normalmente
        def safe_exit():
            try:
                loop = asyncio.new_event_loop()  # Cria um novo loop
                asyncio.set_event_loop(loop)
                loop.run_until_complete(exit_handler())
                loop.close()
            except Exception as e:
                print(f"Erro ao fechar corretamente: {e}")

        atexit.register(safe_exit)  # Usa o novo loop para rodar exit_handler()
                
    async def show_clock():
        while True:
            tool.clear_screen()
            print(f"Horario: {datetime.now().strftime("%H:%M:%S")}")
            await asyncio.sleep(1)
        return