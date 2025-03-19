import os
import platform
from dataclasses import dataclass
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tool import tool
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import data
from data_IA import data_IA

@dataclass
class tool_IA:
    def install_ollama(data_global: data):
        #Trecho Retirado Do Dev Flow 2.0
        try:
            if data_global.OS_client == "Windows":
                print("Para Execuçao Da Feture IA Local E Ultilizado ferramentas de terceros neste caso sendo a ferramenta 'ollama' mais informaçoes no site 'https://ollama.com/'")
                print("Caso Ja Possua A Ferramete Apenas Presisone Qualquer Tecla")
                license_run = input("Deseja Continuar: (y/n)")
                if license_run.lower().strip() == "n":return
                os.system("winget install ollama")
            else:
                print("Para Execuçao Da Feture IA Local E Ultilizado ferramentas de terceros neste caso sendo a ferramenta 'ollama' mais informaçoes no site 'https://ollama.com/'")
                print("Caso Ja Possua A Ferramete Apenas Presisone Qualquer Tecla")
                license_run = input("Deseja Continuar: (y/n)")
                if license_run.lower().strip() == "n":return
                os.system("sudo apt install ollama")
        except Exception as E:
            print(f"Erro Na Innstalaçao Do ollama!, Erro: {E}")


    def menu_IA(data_global:data,data_local:data_IA):
        tool.clear_screen()
        print("_"*30 + data_global.name + "_"*30)
        print(f"{data.day}/{data.mes}/{data.ano}")
        print(f"🤖 Model: {data_local.model}")
        print("_"*73)
        return
    
    def start_IA(data_local:data_IA):
        #os.system("ollama start")
        os.system(f"ollama run {data_local.model + ":" + data_local.parameters}")
        return
    
    def change_model(model:str,data_Local:data_IA ):
        data_Local.model = model
        return
    
    def change_parameters(parameter:str,data_local:data_IA):
        data_local.parameters = parameter + "b"
        return