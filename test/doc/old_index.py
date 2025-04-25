from time import sleep
from data import data
from datetime import datetime
from tool import tool
import asyncio

data_Local = data()

async def Start():
    tool.menu(data_Local)
    print("1. Assesar Odette")
    print("2. Config")
    print("3. Exit")
    c = input("Digite Sua Resosta: ").lower().strip()

    if c == "1":
        tool.clear_screen()
        tool.start_web(data_Local.Odette_URL)
        print(f"Iniciando: {data_Local.Odette_URL}")
        asyncio.sleep(5)
        Start()
        return
    elif c == "2":
        tool.clear_screen() 
        Config_Main()
        return
    elif c == "3":
        tool.clear_screen()
        return
    else:
        asyncio.run(Start())
        return
    
async def Config_Main():
    tool.menu(data_Local)
    print("1. Ativar Dev Mode")
    print("2. Voltar")
    c = input("Digite sua resposta: ").lower().strip()

    if c == "1":
        tool.clear_screen()
        c = input("O Dev Mode ativara mesagem de debug no codigo tem certeza que quer continuar?(y/n): ").lower().strip()
        if c != "y":
            Config_Main()
            return
        if data_Local.Debug:
            data_Local.Debug = False
            print("🔧 Dev Mode Desativado!")
        else:
            data_Local.Debug = True
            tool.clear_screen()
            print("🔧 Dev Mode ativado!")
        sleep(2)
        Config_Main()
        return
    elif c == "2":
        Start()
        return
    else:
        Config_Main()
        return
    

#Inisalizar Tarefas Asincronas antes da inicilizao do app
async def Start_Alert():
    while True:
        await asyncio.sleep(data.time_classroom)
        await tool.alert_to_to_assess_classroom(data.time_classroom,data_Local)
        
async def main():
    tool.verify_modules()
    asyncio.create_task(Start_Alert())  # Inicia o alerta em paralelo
    Start()  # Roda a função principal

if __name__ == "__main__":
    asyncio.run(main()) 
