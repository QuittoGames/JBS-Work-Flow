from tool import tool
from data import data
from time import sleep

# Função que pode ser chamada para rodar a lógica do alerta
def start_alert_process(data_sub):
    try:
        tool.alert_to_to_assess_classroom(data_sub)
    except Exception as E:
        print(f"Erro ao executar o alerta: {E}")

if __name__ == "__main__":
    data_sub = data()
    while True:
        start_alert_process(data_sub)
        sleep(30)
