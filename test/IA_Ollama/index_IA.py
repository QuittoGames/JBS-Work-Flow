import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tool import tool
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from data import data
from data_IA import data_IA
from tool_IA import tool_IA

data_local = data_IA()

def Start_IA(data_global:data):
    tool_IA.menu_IA(data_local = data_local,data_global = data_global)
    print("1. Config")
    print("2. Prosseguir")
    print("3. Retornar Al Menu")
    c = input("Deseja Inicar A IA Local: ").lower().strip()
    if c == "1":
        Config_IA(data_global=data_global)
        return
    elif c == "2":
        tool_IA.start_IA(data_local)
        return
    else:
        return
        
def Config_IA(data_global:data):
    tool_IA.menu_IA(data_local = data_local,data_global = data_global)
    print("1. Mudar Modelo")
    print("2. Mudar Parametros")
    print("3. Retornar Al Menu Pricipal")
    
    c = input("Digite Sua Opiçao: ").lower().strip()

    if c == "1":
        tool.clear_screen()
        print("Modelos: https://ollama.com/search")
        new_model = input("Digite O Nome Do Novo Modelo: ")
        tool_IA.change_model(new_model, data_local)  # Correção aqui
        Config_IA(data_global=data_global)
        return
    elif c == "2":
        tool.clear_screen()
        print("Modelos: https://ollama.com/search")
        print("!! VERIFIQUE SE O MODELO ESCOLHIDO SUPORTA A QUANTIDADE DE PARÂMETROS !!")
        parameters_new = input("Digite A Nova Quantidade De Parâmetros: ")
        tool_IA.change_parameters(parameters_new, data_local)  # Correção aqui
        Config_IA(data_global=data_global)
        return
    else: 
        Start_IA(data_global=data_global)
        return
    
def main(data_global:data):
    tool_IA.install_ollama(data_global)
    Start_IA(data_global=data_global)
    return

if __name__ == "__main__":
    main(data_global=data)