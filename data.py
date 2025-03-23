from dataclasses import dataclass
from datetime import datetime
import platform

@dataclass
class data:
    modules = ["requests","winotify"]
    Debug = False
    name = "JBS Work Flow"
    Odette_URL = "https://alunos.igerminare.org.br/"
    ano = datetime.now().year
    mes = datetime.now().month
    day = datetime.now().day
    alert_pid : int = 0
    version:str = "3.1v"
    version_id_register:str = "K2025_03_H1_10_relise"
    date = [(7, 50),(8, 0),(8, 50),(9, 0),(9, 50),(10, 0),(11, 20),(11, 30),(12, 20),(12, 30),(13, 20),(13, 30),(12,47)] 
    OS_client = platform.system()
    Tasks_to_do = []
