from time import sleep
from data import data
from datetime import datetime
from tool import tool
import asyncio
import subprocess
import os
import sys

#Iniliza A Classe data
data_Local = data()
 
#LINCEÇA MIT
#By: Gustavo Quitto

#Runtime
async def Start():
    tool.menu(data_Local)
    print("1. Assesar Odette")
    print("2. Tasks")
    print("3. Config")
    if data_Local.Debug:print("5. IA Local")
    print("4. Exit")
    c = input("Digite Sua Resosta: ").lower().strip()

    if c == "1":
        tool.clear_screen()
        tool.start_web(data_Local.Odette_URL)
        print(f"Iniciando: {data_Local.Odette_URL}")
        await asyncio.sleep(5)
        await asyncio.create_task(Start())
        return
    elif c == "2":
        try:
            #Inicar Module Do To_Do
            sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "ToDo")))
            from ToDo.to_do_main import To_Do_Main
            To_Do_Main(data_Local=data_Local)
            await Start()
            return
        except Exception as E:
            print(f"Erro Al Iniciar To_Do Tasks Module, Erro: {E}")
    elif c == "3":
        tool.clear_screen() 
        await Config_Main()
        return
    elif c == "4":
        if data_Local.alert_pid is None or not isinstance(data_Local.alert_pid, int):
            print(f"Erro: PID inválido ({data_Local.alert_pid})")
        else:
            tool.exit_progarm(PID=data_Local.alert_pid) #Fecha por PID do agente.py
        tool.clear_screen()
        return
    elif c == "5" and data_Local.Debug:
        sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "IA_Ollama")))
        from IA_Ollama.index_IA import Start_IA
        main(data_global=data_Local)
        await Start()
        return

    else:
        await asyncio.create_task(Start())
        return
    
async def Config_Main():
    tool.menu(data_Local)
    print("1. Ativar Dev Mode")
    print("2. Mudar Nome Do App")
    print("3. App Info")
    print("4. Voltar")
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
        tool.clear_screen() 
        Show_PID_Info(data_local=data_Local,PID=data_Local.alert_pid)
        return
    elif c == "4":
        await asyncio.create_task(Start())
        return
    else:
        await Config_Main()
        return

def Show_PID_Info(data_local:data, PID:int):
    tool.menu(data_local)
    print(f"🚀  **App**: {data_local.name}")
    print(f"🛠️  **Version**: {data_local.version}")
    print(f"🖥️  **Sistema Operacional**: {data_local.OS_client}")
    print(f"⚙️  **PID do processo alert.py**: {PID}")
    print(f"📅  **Data**: {data_local.day}/{data_local.mes}/{data_local.ano}")
    print(f"⏳  **Status**: {'Ativo' if PID != 0 else 'Inativo'}")
    print(f"🔑  **Licença**: MIT")
    print(f"👨‍💻  **Criador**: Quitto")

    c = input("Digite qualquer coisa para voltar: ")
    tool.clear_screen()
    asyncio.create_task(Start())
    return

#Inisalizar Tarefas Asincronas antes da inicilizao do app
async def main():
    tool.verify_modules()
    tool.format_dates(data_Local)
    if not tool.is_alert_running(PID = data_Local.alert_pid):  # A função is_alert_running precisa ser implementada para verificar se o alerta já está em execução
        tool.start_alert_process(data_Local)
        if data_Local.Debug: print(f"🚀 alert.py iniciado! iniciado com PID: {data_Local.alert_pid}")  # Print para debug
    await asyncio.create_task(Start())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())


#By: Gustavo Quitto
