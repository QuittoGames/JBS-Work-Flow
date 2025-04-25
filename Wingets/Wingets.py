from dataclasses import dataclass
import subprocess
import os

@dataclass
class Wingets:
    name: str
    path: str

    def start(self):
        if os.path.exists(self.path):
            process = subprocess.Popen(["python", self.path], creationflags=subprocess.CREATE_NEW_CONSOLE)
            return
        print(f"❌ Caminho não encontrado: {self.path}")

    def __str__(self):
        return f"|Nome Do Winget: {self.name} | Caminho: {self.path}|"