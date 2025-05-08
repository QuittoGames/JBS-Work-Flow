from dataclasses import dataclass
import subprocess
from random import randint
from time import sleep
import os

@dataclass
class Wingets:
    ID: int
    name: str
    path: str

    def start(self,path:str):
        if os.path.exists(self.path):
            try:
                prosses = subprocess.Popen(["python", self.path], creationflags=subprocess.CREATE_NEW_CONSOL)
                print(prosses)
                sleep(100)
            except Exception as E:
                print(f"Erro Al Inicar Winget, Erro: {E}")
            
            return
        print(f"❌ Caminho não encontrado: {self.path}")

    def __str__(self):
        return f"|Nome Do Winget: {self.name} | Caminho: {self.path}|"