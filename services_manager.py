import asyncio
from data import data
from tool import tool
from dataclasses import dataclass


@dataclass
class Services:
    async def start_auto_avali(data_Local:data):
        try:
            asyncio.create_task(tool.format_dates(data_Local))
            if not tool.is_alert_running(PID = data_Local.alert_pid):  # A função is_alert_running precisa ser implementada para verificar se o alerta já está em execução
                tool.start_alert_process(data_Local)
                if data_Local.Debug: print(f"🚀 alert.py iniciado! iniciado com PID: {data_Local.alert_pid}")  # Print para debug
        except Exception as E:
            print(f"Erro Al Inciar Sistema De Auto Avaliçaos, Erro: {E}")

    def start_IA(data_Local:data):
        try:
            from IA_Ollama.index_IA import main
            main(data_global=data_Local)
        except ImportError as e:
            print(f"Erro ao importar IA_Ollama: {e}")
            return
        except Exception as e:
            print(f"Erro ao iniciar IA: {e}")
            return

    def start_ToDo(data_Local:data):
        try:
            from ToDo.to_do_main import To_Do_Main
            To_Do_Main(data_Local=data_Local)
        except ImportError as e:
            print(f"Erro ao importar ToDo: {e}")
            return
        except Exception as e:
            print(f"Erro ao iniciar ToDo: {e}")
            return
