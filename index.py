from time import sleep
from data import data
from datetime import datetime
from tool import tool
from services_manager import Services
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
    print("1. Acessar Odette")
    print("2. Tasks")
    print("3. Config")
    if data_Local.Debug:print("5. IA Local")
    print("4. Exit")
    c = input("Digite Sua Resosta: ").lower().strip()

    if c == "1":
        tool.clear_screen()
        tool.start_web(data_Local.Odette_URL,data_local=data_Local)
        print(f"Iniciando: {data_Local.Odette_URL}")
        await asyncio.sleep(2)
        await asyncio.create_task(Start())
        return
    elif c == "2":
        try:
            #Inicar Module Do To_Do
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
        Services.start_IA(data_Local)
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
    print("4. Ativar Script De UI")
    print("5. Voltar")
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
        tool.clear_screen()
        if data_Local.Debug:print(f"script_auto_gui: {data_Local.script_auto_gui}")
        print("\n⚠️  MODO AUTOMÁTICO: AVISO IMPORTANTE ⚠️\n")
        print("Ativar este modo pode causar a execução de ações possivelmente indesejadas.")
        print("Ao ser ativado, toda vez que a notificação for acionada,")
        print("uma ação automática será executada usando o mouse e o navegador.\n")
        
        c = input("Deseja continuar? (y/n): ").strip().lower()
        try:
            if c != "n" and c != "".split():
                data_Local.script_auto_gui = True
                tool.reset_altert_prosses(data_Local)
                print("\n✅ Modo automático ativado com sucesso.")
                sleep(2)
                await Start()
                return
            print("\n❌ Modo automático não foi ativado.")
            return
        except Exception as E:
            print(f"Erro Al Acionar script Automatico, Erro: {E}")

    elif c == "5":
        await asyncio.create_task(Start())
        return
    else:
        await Config_Main()
        return

def Show_PID_Info(data_local:data, PID:int):
    tool.menu(data_local)
    print(f"🚀  **App**: {data_local.name}")
    print(f"🛠️  **Version**: {data_local.version}")
    if data_Local.Debug:print(f"🛠️  **Regiter Version**: {data_local.version_id_register}")
    print(f"🖥️  **Sistema Operacional**: {data_local.OS_client}")
    print(f"⚙️  **PID do processo alert.py**: {PID}")
    print(f"📅  **Data**: {data_local.day}/{data_local.mes}/{data_local.ano}")
    print(f"⏳  **Status**: {'Ativo' if PID != 0 else 'Inativo'}")
    print(f"🔑  **Licença**: MIT")
    print(f"👨‍💻  **Criador**: Quitto | Dev")
    print("👨‍💻  **Dev de Automação** | Quitto | Dev\n 🥷 **Mega Ninja Padovanni** | Dev de Automação")

    c = input("Digite qualquer coisa para voltar: ")
    tool.clear_screen()
    asyncio.create_task(Start())
    return


#Inisalizar Tarefas Asincronas antes da inicilizao do app
async def main():
    asyncio.create_task(tool.add_path_modules(data_Local))

    #Verfica Os Argumentos
    args = tool.set_args(data_Local)
    if args.auto_avali:
        await asyncio.create_task(Services.start_auto_avali(data_Local))
        return
    elif args.IA:
        Services.start_IA(data_Local)
        return
    elif args.ToDo:
        pass

    if not data_Local.Debug:asyncio.create_task(tool.verify_modules())
    asyncio.create_task(Services.start_auto_avali(data_Local)) # Inicia Serviço De Auto Avaliçao 

    await asyncio.create_task(tool.start_exit_systhen(data_Local)) # In Dev
    await asyncio.create_task(Start())

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.run_until_complete(main())


#By: Gustavo Quitto
