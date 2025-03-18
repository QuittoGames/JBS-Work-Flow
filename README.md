# JBS Work Flow


# Notas da Nova Versão - Módulo "To Do" 3.0v 

- O módulo **To Do** está em fase **Beta** e faz parte do sistema **JBS Work Flow**.
- **Modo de Desenvolvimento (Debug)** precisa estar ativado para acessar e interagir com o módulo.
- A versão **3.0v a** pode apresentar comportamentos inesperados.
- O **To Do** permite o gerenciamento de tarefas com funcionalidades de:
  - Adicionar, remover e visualizar tarefas.
  - Configuração de notificações baseadas em tempo.
- O sistema envia **notificações automáticas** para tarefas em horários específicos.
- O módulo é **interativo** com um menu para gerenciar tarefas e configurações do aplicativo.


## Visão Geral

O **JBS Work Flow** é um acelerador de fluxo de trabalho desenvolvido para facilitar as atividades na escola, principalmente através de notificações que lembram os usuários de avaliar as aulas em horários pré-definidos. O sistema utiliza tarefas assíncronas para gerenciar o menu interativo e um processo em segundo plano para monitorar o horário e disparar notificações automaticamente.

## Funcionalidades

- **Notificações Automáticas:** Envia alertas (ex.: "Avalie A Aula !!!") em horários específicos para lembrar os usuários de avaliar a aula.
- **Menu Interativo:** Permite acessar o site (Odette), alterar configurações e sair do programa.
- **Modo de Desenvolvimento (Debug):** Exibe mensagens de depuração para facilitar a identificação e correção de erros.
- **Processo de Alerta em Segundo Plano:** Monitora continuamente os horários definidos para disparar notificações sem interromper o fluxo principal do aplicativo.

## Estrutura do Código

- **index.py:**  
  - Ponto de entrada principal do aplicativo.
  - Gerencia o fluxo de execução utilizando funções assíncronas (asyncio).
  - Apresenta um menu com as opções: acessar o site, configurar o aplicativo ou sair.

- **data.py:**  
  - Define a classe `data`, que armazena as configurações e informações essenciais, como:
    - Módulos necessários (ex.: `requests`, `winotify`).
    - Modo de depuração (Debug).
    - Nome do aplicativo.
    - URL do site (Odette).
    - Dados de data e horários para notificações.
    - Informações sobre o sistema operacional.

- **tool.py:**  
  - Contém funções auxiliares para:
    - Limpar a tela do terminal.
    - Verificar e instalar módulos necessários.
    - Exibir notificações utilizando a biblioteca `winotify`.
    - Gerenciar subprocessos (iniciando o processo de alerta, verificando se ele já está em execução, etc.).
    - Formatar datas e manipular configurações do aplicativo.
    - Abrir um site no navegador.

- **alert.py:**  
  - Executa um loop contínuo que verifica o horário atual.
  - Quando o horário coincide com os momentos pré-definidos, chama a função de notificação para alertar os usuários.

## Instalação e Configuração

### Pré-Requisitos

- **Python:**  
  Certifique-se de ter o Python instalado em seu computador. Baixe a versão mais recente em:  
  [Python Downloads](https://www.python.org/downloads/)

- **Git:**  
  Para clonar o repositório, você precisará do Git. Faça o download em:  
  [Git Downloads](https://git-scm.com/downloads)

- **Módulos Python Necessários:**  
  O projeto utiliza os módulos `requests` e `winotify`. Caso não estejam instalados, eles podem ser instalados automaticamente pelo código ou manualmente via pip:
  ```bash
  pip install requests winotify
# Como Executar o Aplicativo

### 1. Clone o Repositório
Para começar, clone o repositório no seu computador:
  ```bash
  git clone https://github.com/QuittoGames/JBS-Work-Flow
  cd JBS-Work-Flow
  python index.py
