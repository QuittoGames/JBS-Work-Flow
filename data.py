from dataclasses import dataclass
from datetime import datetime
import platform

@dataclass
class data:
    modules = ["requests","winotify"]
    Debug = False
    name = "JBS Work Flow"
    Odette_URL = "https://alunos.igerminare.org.br/"
    version: str = "2.0.2v"
    ano = datetime.now().year
    mes = datetime.now().month
    day = datetime.now().day
    alert_pid : int = 0
    version:str = "2.0.2v"
    date = [(7, 50),(8, 0),(8, 50),(9, 0),(9, 50),(10, 0),(11, 20),(11, 30),(12, 20),(12, 30),(13, 20),(13, 30),(10,12)] 
    OS_client = platform.system()
    Tasks_to_do = []
