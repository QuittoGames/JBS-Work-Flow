from time import sleep
from data import data
from datetime import datetime
from tool import tool
import asyncio

#Iniliza A Classe data
data_Local = data()

#LINCEÇA MIT
#By: Gustavo Quitto

#Runtime
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
        await asyncio.sleep(5)
        await asyncio.create_task(Start())
        return
    elif c == "2":
        tool.clear_screen() 
        await Config_Main()
        return
    elif c == "3":
        tool.clear_screen()
        return
    else:
        await asyncio.create_task(Start())
        return
    
async def Config_Main():
    tool.menu(data_Local)
    print("1. Ativar Dev Mode")
    print("2. Mudar Nome Do App")
    print("3. Voltar")
    c = input("Digite sua resposta: ").lower().strip()

    if c == "1":
        tool.clear_screen()
        c = input("O Dev Mode ativara mesagem de debug no codigo tem certeza que quer continuar?(y/n): ").lower().strip()
        if c != "y":
            await Config_Main()
            return
        if data_Local.Debug:
            data_Local.Debug = False
            print("🔧 Dev Mode Desativado!")
        else:
            data_Local.Debug = True
            tool.clear_screen()
            print("🔧 Dev Mode ativado!")
        sleep(2)
        await Config_Main()
        return
    elif c == "2":
        tool.change_app_name(data_Local)
        await Config_Main()
        return
    elif c == "3":
        await asyncio.create_task(Start())
        return
    else:
        await Config_Main()
        return


#Inisalizar Tarefas Asincronas antes da inicilizao do app
async def main():
    tool.verify_modules()
    tool.format_dates(data_Local)
    asyncio.create_task(tool.alert_to_to_assess_classroom(data_local=data_Local))
    await asyncio.create_task(Start())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())


#By: Gustavo Quitto
