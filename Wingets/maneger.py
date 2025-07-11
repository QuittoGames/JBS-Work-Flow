import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import data
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tool import tool
from time import sleep
from winget_tool import winget_tool 
from wingets_data import winget_data
from Wingets import Wingets

def WingetsConfig(data_local:data):
    tool.menu(data_local)
    print("1. Run Wingets")
    print("2. Return")
    c = input("Digite Sua Opiçao: ")
    
    if c == "1":
        activeWinget(data_local=data_local)
        sleep(1)
        WingetsConfig()
        return
    elif c == "2":
        return
    else:
        WingetsConfig()
        return


def activeWinget(data_local:data):
    tool.menu(data_local)
    print("Wingets: ")
    winget_tool.showWingets(winget_data)
    
    ID_winget = input("Digite O ID do Winget: ").lower().strip()
    ID_winget = int(ID_winget)
    try:
        #Refatorara Para pesquisa binaria
        winget_local = winget_tool.getWinget(ID_winget,winget_data)
        if winget_local is None:
            print("Winget Nao Pode Ser Encotrado!!")
            sleep(5)
            WingetsConfig()
            return

        winget_local.start()
    except Exception as E:
        print(f"Erro Al Iniciar Winget, Erro: {E}")
        sleep(1000)

if __name__ == "__main__":
    WingetsConfig()


