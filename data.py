from dataclasses import dataclass
from datetime import datetime
import platform

@dataclass
class data:
    modules = []
    Debug = False
    name = "JBS Work Flow"
    Odette_URL = "https://alunos.igerminare.org.br/"
    ano = datetime.now().year
    mes = datetime.now().month
    day = datetime.now().day
    date = [(8,20), (8,30),(9,20),(9,30),(10,20),(10,30),(11,20),(11,30),(12,20),(12,30),(13,20),(13,30)] #(11,14) 

    OS_client = platform.system()
