from dataclasses import dataclass
from datetime import datetime
import platform
import subprocess

@dataclass
class data:
    modules_local = ["ToDo","IA_Ollama"]
    modules = ["requests","winotify","Wingets"]
    Debug = True
    name = "JBS Work Flow"
    script_auto_gui:bool = True # Por Padrao vem desabilitada
    wingets_active:bool = False
    Odette_URL = "https://alunos.igerminare.org.br/"
    ano = datetime.now().year
    mes = datetime.now().month
    day = datetime.now().day
    alert_pid : int = 0
    version:str = "4.0v"
    version_id_register:str = "K2025_05_H1_20dev"
    date = [(7, 50),(8, 0),(8, 50),(9, 0),(9, 50),(10, 0),(11, 20),(11, 30),(12, 20),(12, 30),(13, 20),(13, 30),(10,6)] 
    OS_client = platform.system()
    Tasks_to_do = []