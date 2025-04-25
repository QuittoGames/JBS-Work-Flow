# Documentação Completa: JBS Work Flow

## 📋 Sumário

1. [Introdução](#introdução)
2. [Visão Geral do Sistema](#visão-geral-do-sistema)
3. [Arquitetura do Sistema](#arquitetura-do-sistema)
4. [Instalação e Configuração](#instalação-e-configuração)
5. [Módulos Principais](#módulos-principais)
   - [Módulo Principal (index.py)](#módulo-principal-indexpy)
   - [Módulo de Dados (data.py)](#módulo-de-dados-datapy)
   - [Módulo de Ferramentas (tool.py)](#módulo-de-ferramentas-toolpy)
   - [Módulo de Alerta (alert.py)](#módulo-de-alerta-alertpy)
   - [Módulo ToDo](#módulo-todo)
   - [Módulo IA_Ollama](#módulo-ia_ollama)
6. [Funções Complexas e Reutilizáveis](#funções-complexas-e-reutilizáveis)
   - [Funções Assíncronas](#funções-assíncronas)
   - [Funções de Automação](#funções-de-automação)
   - [Funções de Gerenciamento de Processos](#funções-de-gerenciamento-de-processos)
   - [Algoritmos e Estruturas de Dados](#algoritmos-e-estruturas-de-dados)
7. [Fluxo de Execução](#fluxo-de-execução)
8. [Sistema de Notificações](#sistema-de-notificações)
9. [Sistema de Automação](#sistema-de-automação)
10. [Ciclo de Desenvolvimento](#ciclo-de-desenvolvimento)
11. [Versionamento](#versionamento)
12. [FAQ - Perguntas Frequentes](#faq---perguntas-frequentes)
13. [Contato e Suporte](#contato-e-suporte)

## Introdução

O **JBS Work Flow** é uma aplicação desktop desenvolvida em Python para otimizar o fluxo de trabalho dos alunos do Germinare Tech. 

A aplicação foi projetada com foco em dois objetivos principais:
1. Automatizar o processo de avaliação de aulas na plataforma Odette
2. Fornecer um sistema de gerenciamento de tarefas (ToDo) integrado

Este software foi inicialmente criado para automatizar a avaliação das aulas que acontecem em horários específicos, eliminando a necessidade de o usuário lembrar de realizar esta tarefa manualmente. Com o tempo, evoluiu para incluir mais funcionalidades, como o gerenciamento de tarefas e até mesmo integração com inteligência artificial local.

## Visão Geral do Sistema

O JBS Work Flow funciona como um assistente digital para estudantes, com as seguintes características principais:

- **Automação de Avaliações**: Monitora o horário e envia notificações para lembrar o usuário de avaliar as aulas, podendo até mesmo automatizar completamente esse processo.
- **Gerenciador de Tarefas**: Permite criar, visualizar e gerenciar tarefas, com sistema de notificações baseado em tempo.
- **Integração com IA Local**: Oferece integração com o Ollama para acesso a modelos de IA localmente (modo de desenvolvimento).
- **Interface de Terminal**: Interface simples baseada em menu de terminal, focada na eficiência e facilidade de uso.

A aplicação é modular, o que permite a adição de novas funcionalidades sem comprometer o sistema existente. Utiliza programação assíncrona para gerenciar múltiplas tarefas simultaneamente, melhorando a experiência do usuário.

## Arquitetura do Sistema

O JBS Work Flow segue uma arquitetura modular, onde cada módulo tem uma responsabilidade específica. A estrutura principal inclui:

```
JBS-Work-Flow/
│
├── index.py              # Ponto de entrada e menu principal
├── data.py               # Classe de dados e configurações globais
├── tool.py               # Ferramentas e funções utilitárias
├── alert.py              # Processo de monitoramento de horários
│
├── ToDo/                 # Módulo de gerenciamento de tarefas
│   ├── __init__.py
│   ├── to_do_class.py    # Classe para os objetos de tarefa
│   ├── to_do_main.py     # Ponto de entrada do módulo
│   └── to_do_tool.py     # Ferramentas específicas para tarefas
│
├── IA_Ollama/            # Módulo de integração com IA local
│   ├── __init__.py
│   ├── data_IA.py        # Configurações da IA
│   ├── index_IA.py       # Ponto de entrada do módulo IA
│   └── tool_IA.py        # Ferramentas específicas para IA
│
├── modules/              # Diretório de módulos externos
│   └── requirements.txt  # Dependências do projeto
│
├── icons/                # Ícones para notificações
│   └── icon.png          # Ícone principal
│   └── 5_estrelas.png    # Imagem usada na automação
│
└── doc/                  # Documentação
    └── documentacao_completa.md  # Este arquivo
```

O sistema utiliza uma abordagem assíncrona para gerenciar múltiplas tarefas simultaneamente através da biblioteca `asyncio` do Python. Isso permite que o menu principal continue respondendo enquanto o processo de alerta monitora os horários em segundo plano.

## Instalação e Configuração

### Pré-requisitos

- Python 3.7 ou superior
- Sistema operacional: Windows (recomendado) ou Linux

### Dependências principais

- `requests`: Para comunicação HTTP
- `winotify`: Para notificações no Windows
- `asyncio`: Para programação assíncrona
- `opencv-python` e `mss`: Para automação visual
- `pyautogui`: Para automação de mouse e teclado

### Passos para instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/QuittoGames/JBS-Work-Flow
   cd JBS-Work-Flow
   ```

2. **Instale as dependências**:
   O sistema instalará automaticamente as dependências necessárias ao iniciar, mas você também pode instalá-las manualmente:
   ```bash
   pip install -r modules/requirements.txt
   ```

3. **Execute o aplicativo**:
   ```bash
   python index.py
   ```

### Configuração inicial

Ao executar o aplicativo pela primeira vez, você terá acesso às seguintes opções de configuração no menu "Config":

1. **Ativar Dev Mode**: Habilita mensagens de debug para identificar problemas
2. **Mudar Nome do App**: Personaliza o nome do aplicativo
3. **App Info**: Exibe informações sobre a versão atual e o processo em execução
4. **Ativar Script de UI**: Habilita a automação completa (requer cuidado)

## Módulos Principais

### Módulo Principal (index.py)

O arquivo `index.py` é o ponto de entrada do aplicativo. Ele inicializa o ambiente, carrega os módulos necessários e apresenta o menu principal ao usuário. Suas responsabilidades incluem:

- **Inicialização do ambiente**: Configurar o sistema antes de começar
- **Menu principal**: Interface de usuário para acessar as funcionalidades
- **Gestão de tarefas assíncronas**: Coordenar processos simultâneos

Código principal e componentes essenciais:

```python
# Inicialização assíncrona do aplicativo
async def main():
    if not data_Local.Debug:
        asyncio.create_task(tool.verify_modules())

    asyncio.create_task(tool.add_path_modules(data_Local))
    asyncio.create_task(tool.format_dates(data_Local))
    
    # Inicia o processo de alerta se ainda não estiver em execução
    if not tool.is_alert_running(PID = data_Local.alert_pid):
        tool.start_alert_process(data_Local)
        
    await asyncio.create_task(tool.start_exit_systhen(data_Local))
    await asyncio.create_task(Start())
```

O menu principal oferece as seguintes opções:
1. **Acessar Odette**: Abre a plataforma no navegador
2. **Tasks**: Abre o módulo de gerenciamento de tarefas
3. **Config**: Acessa as configurações do aplicativo
4. **Exit**: Encerra o aplicativo e todos os processos associados
5. **IA Local** (em dev mode): Acessa o módulo de IA local

### Módulo de Dados (data.py)

O arquivo `data.py` define a classe `data`, que funciona como um repositório central para todas as configurações e dados compartilhados do aplicativo. Esta classe utiliza o decorador `@dataclass` do Python para simplificar a criação de objetos de dados.

Principais atributos:

```python
@dataclass
class data:
    modules_local = ["ToDo", "IA_Ollama"]  # Módulos locais do sistema
    modules = ["requests", "winotify"]     # Dependências externas
    Debug = False                          # Modo de desenvolvimento
    name = "JBS Work Flow"                 # Nome do aplicativo
    script_auto_gui = False                # Automação desabilitada por padrão
    Odette_URL = "https://alunos.igerminare.org.br/" # URL da plataforma
    
    # Data atual
    ano = datetime.now().year
    mes = datetime.now().month
    day = datetime.now().day
    
    alert_pid = 0                         # PID do processo de alerta
    version = "4.0v"                      # Versão atual
    version_id_register = "K2025_03_H1_20dev" # ID de versão
    
    # Horários para notificações (formato: hora, minuto)
    date = [(7, 50),(8, 0),(8, 50),(9, 0),(9, 50),(10, 0),
            (11, 20),(11, 30),(12, 20),(12, 30),(13, 20),(13, 30),(20,46)]
    
    OS_client = platform.system()         # Sistema operacional
    Tasks_to_do = []                      # Lista de tarefas
```

Esta classe centraliza todas as configurações e estados do aplicativo, facilitando o acesso aos dados em diferentes partes do código.

### Módulo de Ferramentas (tool.py)

O arquivo `tool.py` contém a classe `tool`, que fornece todas as funcionalidades utilitárias usadas em todo o aplicativo. Esta classe implementa diversos métodos estáticos que desempenham funções essenciais no sistema.

Principais funcionalidades:

1. **Gerenciamento de tela e interface**:
   ```python
   def clear_screen():
       if platform.system() == "Windows":
           os.system('cls')
       else:
           os.system('clear')
   
   def menu(data_Local:data):
       tool.clear_screen()
       print("_"*30 + data_Local.name + "_"*30)
       print(f"{data.day}/{data.mes}/{data.ano}")
       print(f"Sistema Operacional: {data.OS_client}")
       # ... mais informações conforme necessário
       print("_"*73)
   ```

2. **Sistema de notificações**:
   ```python
   @staticmethod
   def Notification(name:str, descri:str):
       try:
           current_dir = os.path.dirname(os.path.abspath(__file__))
           icon_path = os.path.join(current_dir, 'icons', 'icon.png')
           
           notification = winotify.Notification(
               app_id="Germinare TECH",
               title=name,
               msg=descri,
               icon=icon_path
           )
           notification.set_audio(winotify.audio.Default, loop=False)
           notification.add_actions(
               label="Odette",
               launch=data.Odette_URL
           )
           notification.show()
       except Exception as e:
           print(f"Erro ao exibir a notificação: {e}")
   ```

3. **Gerenciamento de processos**:
   ```python
   def start_alert_process(data_Local:data):
       try:
           alert_sub = subprocess.Popen(["python", "alert.py"], 
                                        creationflags=subprocess.CREATE_NO_WINDOW)
           data_Local.alert_pid = alert_sub.pid  # Armazena o PID
       except Exception as E:
           print(f"Erro Al Inicar Subporsses , Erro: {E}")
   
   def is_alert_running(PID:int):
       if data.OS_client == "Windows": 
           process = subprocess.run(
               ["powershell", "-Command", f"Get-Process -Id {PID}"],
               capture_output=True, text=True
           )
           return 'alert.py' in process.stdout
       else:
           return subprocess.call(['pgrep', '-f', 'alert.py']) == 0
   
   exit_progarm = lambda PID: os.kill(PID, signal.SIGTERM)
   ```

4. **Automação visual**:
   ```python
   @staticmethod
   def Finda_img(target, confianca=0.8):
       with mss.mss() as sct:
           screenshot = np.array(sct.grab(sct.monitors[1]))
           screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

           imagem = cv2.imread(target)
           if imagem is None:
               return None

           resultado = cv2.matchTemplate(screenshot, imagem, cv2.TM_CCOEFF_NORMED)
           _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

           if max_val >= confianca:
               centro_x = max_loc[0] + imagem.shape[1] // 2
               centro_y = max_loc[1] + imagem.shape[0] // 2
               return centro_x, centro_y
           else:
               return None
   ```

5. **Verificação de horários e alertas**:
   ```python
   @staticmethod
   def alert_to_to_assess_classroom(data_local:data):
       try:
           hour = datetime.now().strftime("%H")
           minutes = datetime.now().strftime("%M")

           try:
               if (int(hour),int(minutes)) in data_local.date:
                   tool.Notification(name="Avalie A Aula !!!", 
                                    descri="Avalie A Aula !!!")
                   tool.AutoGui_classrom_altert(data_local)
           except Exception as E:
               print(f"Erro Al Verificar Horario: {E}")
       except Exception as E:
           print(f"Erro Al Inicar Loop De Verificaçao, Eroo: {E}")
   ```

### Módulo de Alerta (alert.py)

O arquivo `alert.py` implementa um processo em segundo plano que monitora continuamente o tempo e dispara notificações nos horários definidos. Este arquivo é executado como um processo separado para garantir que as notificações sejam entregues mesmo que a interface principal seja fechada.

Estrutura básica:

```python
def start_alert_process(data_sub):
    try:
        tool.alert_to_to_assess_classroom(data_sub)
    except Exception as E:
        print(f"Erro ao executar o alerta: {E}")

if __name__ == "__main__":
    data_sub = data()
    while True:
        start_alert_process(data_sub)
        sleep(30)  # Verifica a cada 30 segundos
```

Este processo verifica continuamente se o horário atual coincide com algum dos horários definidos para notificação. Quando há uma correspondência, ele dispara a notificação e opcionalmente executa a automação para avaliar a aula.

### Módulo ToDo

O módulo ToDo implementa um sistema de gerenciamento de tarefas com notificações baseadas em tempo. Está organizado em três arquivos principais:

**1. to_do_class.py**: Define a estrutura das tarefas:

```python
@dataclass
class to_do_class:
    name_task: str        # Nome da tarefa
    descri_task: str      # Descrição da tarefa
    timer: int            # Tempo em segundos para notificação
    state: bool           # Estado (concluída ou pendente)
    id_task: int          # ID único da tarefa
```

**2. to_do_main.py**: Implementa o menu principal do módulo:

```python
def To_Do_Main(data_Local:data):
    print("_"*30 + " To Do "+"_"*30)
    tool.menu(data_Local)
    print(f"Tarefas: ")
    to_do_tool.Show_Menu_Task(data.Tasks_to_do)
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")  
    print("4. Exit")
    c = input("Digite Sua Resposta: ").strip().lower()
    # ... código para processar a escolha do usuário
```

**3. to_do_tool.py**: Implementa as funcionalidades do módulo:

- **Adicionar tarefas**: Cria novas tarefas com nome, descrição e tempo para notificação
- **Remover tarefas**: Remove tarefas pelo ID
- **Visualizar tarefas**: Lista todas as tarefas pendentes e concluídas
- **Timer de tarefas**: Inicia um timer separado para cada tarefa e dispara uma notificação quando o tempo expira

O módulo utiliza tempo assíncrono através do método `run_in_executor` para que os timers das tarefas não bloqueiem a interface principal.

### Módulo IA_Ollama

O módulo IA_Ollama integra modelos de linguagem locais ao aplicativo. Está organizado em três arquivos principais:

**1. data_IA.py**: Define as configurações dos modelos:

```python
@dataclass
class data_IA:
    model = "deepseek-r1"     # Modelo de IA padrão
    parameters: str = "7b"    # Tamanho do modelo (7 bilhões de parâmetros)
```

**2. index_IA.py**: Implementa o menu principal do módulo:

```python
def Start_IA(data_global:data):
    tool_IA.menu_IA(data_local=data_local, data_global=data_global)
    print("1. Config")
    print("2. Prosseguir")
    print("3. Retornar Al Menu")
    c = input("Deseja Inicar A IA Local: ").lower().strip()
    # ... código para processar a escolha do usuário
```

**3. tool_IA.py**: Implementa as funcionalidades do módulo:

- **Instalação do Ollama**: Verifica e instala o Ollama se necessário
- **Gerenciamento de modelos**: Permite alterar o modelo de IA e seus parâmetros
- **Execução de modelos**: Inicia uma sessão de chat com o modelo selecionado

Este módulo está disponível apenas no modo de desenvolvimento (Debug = True) e utiliza ferramentas de terceiros (Ollama) para acessar modelos de IA localmente.

## Funções Complexas e Reutilizáveis

Esta seção detalha as funções mais complexas do sistema, explicando seu funcionamento interno, padrões de chamada e potencial para reutilização.

### Funções Assíncronas

#### `main()` e Inicialização Assíncrona

A função `main()` no arquivo `index.py` é o centro de inicialização do sistema. Sua complexidade advém do gerenciamento de múltiplas tarefas assíncronas:

```python
async def main():
    if not data_Local.Debug:
        asyncio.create_task(tool.verify_modules())  # Verificação de dependências

    # Tarefas paralelas de inicialização
    asyncio.create_task(tool.add_path_modules(data_Local))  # Caminhos dos módulos
    asyncio.create_task(tool.format_dates(data_Local))      # Formatação de datas
    
    # Inicia o processo de alerta se não estiver em execução
    if not tool.is_alert_running(PID = data_Local.alert_pid):
        tool.start_alert_process(data_Local)
    
    # Configura o tratamento de saída e inicia o menu principal
    await asyncio.create_task(tool.start_exit_systhen(data_Local))
    await asyncio.create_task(Start())
```

**Detalhe técnico importante**: 
- As primeiras tarefas são criadas com `create_task()` sem `await`, permitindo que executem em paralelo.
- As duas últimas tarefas usam `await` porque precisamos esperar que terminem antes de continuar.
- Esta abordagem permite que o aplicativo inicialize várias operações simultaneamente, melhorando o tempo de inicialização.

**Padrão de reutilização**:
Este padrão de inicialização assíncrona pode ser facilmente adaptado para outros módulos que precisem executar tarefas em paralelo.

#### `Start()` - Menu Principal Recursivo

A função `Start()` implementa o menu principal de forma recursiva, usando `asyncio` para garantir que o menu seja responsivo:

```python
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
        tool.start_web(data_Local.Odette_URL, data_local=data_Local)
        print(f"Iniciando: {data_Local.Odette_URL}")
        await asyncio.sleep(2)
        await asyncio.create_task(Start())  # Chamada recursiva
        return
    # ... outras opções de menu ...
```

**Recursividade**: 
- A função chama a si mesma após processar a escolha do usuário, exceto quando o usuário escolhe sair.
- Este padrão recursivo cria um loop de menu infinito sem bloquear a execução de outras tarefas assíncronas.

**Pontos de atenção**:
- Recursão em Python pode levar a estouro de pilha se muito profunda, mas aqui é controlada pelo usuário.
- O `return` após cada chamada recursiva é essencial para evitar continuação indesejada do código.

#### `format_dates()` - Processamento Adaptativo de Dados

Uma função com lógica adaptativa para converter diferentes formatos de hora:

```python
async def format_dates(data_local:data):
    formatted_date = []
    for i in data_local.date:
        if isinstance(i, float):  # Formato decimal (ex: 7.5 para 7:30)
            hour = int(i)
            minutes = int((i % 1) * 60)
            formatted_date.append((hour, minutes))
        elif isinstance(i, tuple):  # Já está no formato correto
            formatted_date.append(i)
        else:
            print(f"Item inesperado encontrado: {i}")

    data_local.date = formatted_date
```

**Flexibilidade de entrada**:
- A função aceita tanto formatos de hora como float (7.5) quanto como tuplas (7, 30).
- Isso demonstra adaptabilidade para diferentes formatos de dados de entrada.

**Reutilização potencial**:
Esta função poderia ser facilmente adaptada para outros contextos onde conversão de formato de hora é necessária.

### Funções de Automação

#### `Finda_img()` - Reconhecimento Visual com OpenCV

Esta função complexa implementa reconhecimento de padrões na tela:

```python
@staticmethod
def Finda_img(target, confianca=0.8):
    print(f"Procurando a imagem: {target}")
    with mss.mss() as sct:
        # Captura da tela
        screenshot = np.array(sct.grab(sct.monitors[1]))
        screenshot = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

        # Carrega a imagem de referência
        imagem = cv2.imread(target)
        if imagem is None:
            print("Erro: imagem não encontrada no caminho fornecido.")
            return None

        # Algoritmo de template matching
        resultado = cv2.matchTemplate(screenshot, imagem, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(resultado)

        print(f"Confiança detectada: {max_val}")

        # Verificação de confiança e cálculo das coordenadas
        if max_val >= confianca:
            centro_x = max_loc[0] + imagem.shape[1] // 2
            centro_y = max_loc[1] + imagem.shape[0] // 2
            print(f"Imagem encontrada! Coordenadas: ({centro_x}, {centro_y})")
            return centro_x, centro_y
        else:
            print("Imagem não encontrada com confiança suficiente.")
            return None
```

**Complexidade algorítmica**:
- Utiliza o algoritmo Template Matching do OpenCV para encontrar padrões em imagens.
- A complexidade computacional é O(W×H×w×h), onde W,H são as dimensões da tela e w,h são as dimensões da imagem alvo.

**Parâmetros adaptáveis**:
- O parâmetro `confianca` (padrão 0.8) permite ajustar o nível de precisão necessário.
- Valores mais altos (0.9+) exigem correspondência quase perfeita, enquanto valores mais baixos (0.6-0.7) são mais tolerantes.

**Reutilização**:
Esta função é a base para qualquer automação visual no sistema e pode ser reutilizada para:
1. Reconhecer diferentes elementos da interface do Odette
2. Detectar estados da aplicação (carregado, erro, etc.)
3. Verificar se certas janelas estão abertas

#### `AutoGui_classrom_altert()` - Automação Completa com Tratamento de Erro

Esta função orquestra todo o processo de automação da avaliação de aulas:

```python
def AutoGui_classrom_altert(data_local:data):
    if not data_local.script_auto_gui:return  # Verifica se automação está ativada
    try:
        # Inicia o navegador e acessa o Odette
        tool.PyAutoGui_script()
        
        # Procura visualmente o elemento de 5 estrelas
        postion = tool.Finda_img("icons/5_estrelas.png", confianca=0.7)
        if data_local.Debug:print("Valor da variável posicao:", postion)

        if postion:
            if data_local.Debug:print("Achei a imagem! Vou continuar o processo...")
            pg.click(x=1087, y=550)  # Clicar nas estrelas
            sleep(1)
            pg.click(x=941, y=877)  # Clicar no botão de avaliar
            return
        
        # Tratamento de falha na detecção
        if data_local.Debug:print("Não achei a imagem! Vou mandar notificação...")
        tool.Notification(name="Avaliçao De Aula",
                         descri="Erro Avaliar A Aula, Provavelmente O Profesor Nao Abriu A Aula")
        return
    except Exception as E:
        print(f"Erro Al Execultar Altomaçao, Erro: {E}")
```

**Mecanismo de segurança**:
- A verificação inicial `if not data_local.script_auto_gui:return` impede que a automação execute acidentalmente.
- Esse tipo de proteção é crucial em funções que controlam o mouse e teclado.

**Tratamento abrangente de erros**:
- A função tem três caminhos de execução: sucesso, falha na detecção, e exceção inesperada.
- Para cada caminho, há uma ação apropriada, garantindo que o usuário sempre tenha feedback.

**Dependência de outras funções**:
- Reutiliza `PyAutoGui_script()` para iniciar o navegador
- Reutiliza `Finda_img()` para reconhecimento visual
- Reutiliza `Notification()` para feedback ao usuário
- Este encadeamento de funções ilustra o design modular do sistema.

### Funções de Gerenciamento de Processos

#### `start_exit_systhen()` - Tratamento Avançado de Encerramento

Esta função complexa gerencia o encerramento seguro do aplicativo e seus processos filhos:

```python
async def start_exit_systhen(data_local:data):
    async def exit_handler():
        """Chamado antes de o programa fechar"""
        if data_local.alert_pid is not None:
            if pid_exists(data_local.alert_pid): 
                try:
                    await tool.exit_progarm(data_local.alert_pid)
                except ProcessLookupError:
                    print(f"⚠️ Process {data_local.alert_pid} já foi encerrado.")
                except PermissionError:
                    print("⚠️ Sem permissão para encerrar o processo.")
                except Exception as e:
                    print(f"❌ Erro ao encerrar processo: {e}")
            else:
                print("⚠️ Nenhum PID válido para encerrar.")

    def sync_exit_handler(signum, frame):
        """Adaptador para sinais, chama a função assíncrona corretamente"""
        asyncio.get_event_loop().create_task(exit_handler())

    # Configura sinais corretamente
    signal.signal(signal.SIGINT, sync_exit_handler)
    signal.signal(signal.SIGTERM, sync_exit_handler)

    # Executa exit_handler ao sair normalmente
    def safe_exit():
        try:
            loop = asyncio.new_event_loop()  # Cria um novo loop
            asyncio.set_event_loop(loop)
            loop.run_until_complete(exit_handler())
            loop.close()
        except Exception as e:
            print(f"Erro ao fechar corretamente: {e}")

    atexit.register(safe_exit)  # Usa o novo loop para rodar exit_handler()
```

**Complexidade avançada**:
- Implementa uma função aninhada assíncrona `exit_handler()` para o trabalho principal
- Cria um adaptador `sync_exit_handler()` para converter sinais síncronos em chamadas assíncronas
- Utiliza `atexit.register()` para garantir que o código de limpeza seja chamado mesmo em saídas normais

**Múltiplos mecanismos de segurança**:
1. Tratamento de sinais do sistema (SIGINT, SIGTERM)
2. Registro de função de saída com atexit
3. Tratamento detalhado de exceções no encerramento do processo

**Padrão de bridge síncrono-assíncrono**:
Esta função demonstra como criar uma ponte entre código síncrono (manipuladores de sinais) e código assíncrono (funções async), um padrão avançado em Python.

#### `is_alert_running()` - Verificação Cross-Platform de Processos

Função que implementa verificação de processos adaptada ao sistema operacional:

```python
def is_alert_running(PID:int):
    if data.OS_client == "Windows": 
        process = subprocess.run(
            ["powershell", "-Command", f"Get-Process -Id {PID}"],
            capture_output=True, text=True
        )
        return 'alert.py' in process.stdout
    else:
        # Em sistemas Unix, usa-se o pgrep
        return subprocess.call(['pgrep', '-f', 'alert.py']) == 0
```

**Adaptação cross-platform**:
- Escolhe automaticamente o método apropriado para o sistema operacional atual
- No Windows: usa PowerShell para acessar informações de processo
- Em sistemas Unix: usa o comando pgrep

**Reutilização**:
Este padrão é valioso para qualquer aplicação Python cross-platform que precise verificar ou manipular processos.

### Algoritmos e Estruturas de Dados

#### `Find_Task()` - Busca Binária Implementada Manualmente

No módulo ToDo, a função `Find_Task()` implementa o algoritmo de busca binária para encontrar tarefas por ID de forma eficiente:

```python
def Find_Task(id:str):
    if id.strip().split() == "":return None
    low_value = 0
    hight_value = len(data.Tasks_to_do) - 1
    id = int(id)

    # Ordena a lista por ID para garantir que a busca binária funcione corretamente
    data.Tasks_to_do.sort(key=lambda task: task.id_task)

    while low_value <= hight_value:
        med = int((low_value + hight_value) // 2)
        find_value = data.Tasks_to_do[med]
        task_id = int(find_value.id_task) 

        if data.Debug:
            print(f"low_value: {low_value}")
            print(f"high_value: {hight_value}")
            print(f"med: {med}")

        if task_id == id:
            return find_value
        if task_id > id:
            hight_value = med - 1
        else:
            low_value = med + 1

    return None
```

**Complexidade algorítmica**:
- Tempo: O(log n) para busca, precedido por O(n log n) para ordenação
- Espaço: O(1) para a busca em si (apenas algumas variáveis)

**Otimização matemática**:
- Usa a operação de divisão inteira `//` para calcular o ponto médio, evitando problemas com arredondamento
- Implementa a condição de término `low_value <= hight_value` corretamente

**Reutilizável como template**:
Esta implementação pode ser facilmente adaptada para buscar qualquer objeto por qualquer atributo numérico, alterando apenas:
1. A lista a ser pesquisada
2. A chave de ordenação (lambda)
3. O atributo de comparação (task_id)

#### `task_timer()` - Contagem Regressiva com Threading

Função que implementa um timer dedicado para cada tarefa:

```python
@staticmethod
def task_timer(task:to_do_class):
    while task.timer > 0 and not task.state:
        task.timer -= 1.0
        #if data.Debug: print(f"Task {task.name_task}: tempo restante: {task.timer}s")
        sleep(1) 

    tool.Notification(name=task.name_task, descri=task.descri_task)
    task.state = True
```

**Como é chamada**:
```python
# Código em Add_Task() que inicia o timer em uma thread separada
loop = asyncio.get_event_loop()
loop.run_in_executor(None, to_do_tool.task_timer, task)
```

**Design multi-threading**:
- Cada tarefa recebe sua própria thread dedicada para contagem regressiva
- Usa `run_in_executor()` para executar código bloqueante (sleep) sem bloquear o loop de eventos principal
- Atualiza o estado da tarefa diretamente no objeto compartilhado

**Pontos técnicos importantes**:
1. O timer decrementa em intervalos de 1 segundo para precisão
2. Tem condição dupla de parada: timer <= 0 OU task.state = True
3. Marca automaticamente a tarefa como concluída ao finalizar

**Reutilização**:
Este padrão de "temporizador em thread separada" pode ser aplicado a qualquer funcionalidade que precise de contagem regressiva sem bloquear a interface.

## Fluxo de Execução

O fluxo de execução principal do JBS Work Flow segue estas etapas:

1. **Inicialização**
   - O arquivo `index.py` é executado
   - O ambiente é configurado (verificação de módulos, carregamento de caminhos)
   - O processo `alert.py` é iniciado como um subprocesso separado

2. **Menu Principal**
   - O usuário interage com o menu principal
   - Pode acessar o site Odette, gerenciar tarefas ou ajustar configurações

3. **Monitoramento contínuo**
   - O processo `alert.py` verifica continuamente o horário
   - Quando um horário definido é atingido, uma notificação é exibida
   - Se a automação estiver ativada, o sistema tentará avaliar a aula automaticamente

4. **Gerenciamento de tarefas (opcional)**
   - O usuário pode adicionar, remover ou visualizar tarefas
   - Cada tarefa pode ter um timer que, ao completar, dispara uma notificação

5. **Integração com IA (opcional, modo dev)**
   - O usuário pode acessar modelos de IA locais para assistência
   - Os modelos são gerenciados pelo Ollama

6. **Encerramento**
   - Ao sair, o aplicativo encerra todos os processos filhos
   - Usa sinais (SIGINT, SIGTERM) para garantir um encerramento limpo

## Sistema de Notificações

O JBS Work Flow implementa dois tipos de notificações:

### 1. Notificações de Horário

Essas notificações são exibidas em horários específicos definidos na classe `data` (atributo `date`). São destinadas a lembrar o usuário de avaliar as aulas.

Componentes principais:
- **Processo de alerta**: Verificação contínua do horário atual
- **Notificação visual**: Popup na área de notificações do Windows
- **Som de alerta**: Alerta sonoro para chamar atenção
- **Link direto**: Botão para acessar a plataforma Odette

### 2. Notificações de Tarefas

Essas notificações são exibidas quando o timer de uma tarefa expira. São destinadas a lembrar o usuário de realizar uma tarefa específica.

Componentes principais:
- **Timer de tarefa**: Contagem regressiva para cada tarefa
- **Notificação visual**: Popup mostrando o nome e descrição da tarefa
- **Marcação automática**: A tarefa é marcada como concluída após a notificação

O sistema utiliza a biblioteca `winotify` para exibir notificações no Windows, garantindo integração com o sistema operacional.

## Sistema de Automação

O JBS Work Flow inclui um sistema de automação opcional que pode realizar tarefas no computador sem intervenção do usuário. Esta funcionalidade está disponível principalmente para a avaliação automática de aulas.

> ⚠️ **AVISO**: A automação deve ser usada com cautela, pois controla seu mouse e teclado automaticamente.

### Como funciona

1. **Ativação**: O usuário ativa a automação no menu de configurações
2. **Detecção de horário**: O sistema detecta quando é hora de avaliar uma aula
3. **Execução da sequência**:
   - Abre o navegador Chrome
   - Navega até a plataforma Odette
   - Procura visualmente pelo elemento de 5 estrelas
   - Clica para avaliar a aula com a nota máxima

### Componentes técnicos

- **PyAutoGUI**: Controla o mouse e teclado
- **OpenCV com MSS**: Captura e analisa a tela para encontrar elementos visuais
- **Reconhecimento de padrões**: Identifica elementos da interface (como as estrelas de avaliação)

## Ciclo de Desenvolvimento

O JBS Work Flow segue um ciclo de desenvolvimento iterativo, com foco em adicionar funcionalidades mantendo a estabilidade do núcleo do sistema.

### Fases de desenvolvimento

1. **Planejamento**: Identificação de necessidades e novas funcionalidades
2. **Implementação**: Codificação das funcionalidades em módulos separados
3. **Testes**: Verificação de funcionamento e estabilidade
4. **Lançamento**: Distribuição de novas versões

### Modo de depuração (Debug)

O sistema inclui um modo de depuração que pode ser ativado nas configurações. Quando ativado:
- Exibe mensagens de debug no console
- Oferece acesso a funcionalidades experimentais
- Mostra informações adicionais sobre o estado do sistema

Para ativar o modo de depuração:
1. Abra o aplicativo
2. Selecione a opção "Config"
3. Escolha "Ativar Dev Mode"

## Versionamento

O JBS Work Flow utiliza um sistema de versionamento estruturado para identificar cada lançamento. O formato segue o padrão:

```
K{ANO}_{MES}_H{SEMESTRE}_TypeVersion
```

Onde:
- **K**: Prefixo de identificação do projeto
- **{ANO}_{MES}**: Ano e mês do lançamento
- **H{SEMESTRE}**: Semestre (H1 = primeiro, H2 = segundo)
- **TypeVersion**: Tipo de versão
  - **10** = release (estável)
  - **20** = dev (desenvolvimento)
  - **30** = test (testes)

Exemplos:
- **K2025_03_H1_10**: Versão estável de março/2025, primeiro semestre
- **K2025_03_H1_20dev**: Versão de desenvolvimento de março/2025, primeiro semestre

## FAQ - Perguntas Frequentes

### Gerais

**P: O que é o JBS Work Flow?**  
R: É um aplicativo desenvolvido para automatizar tarefas dos alunos do Germinare Tech, principalmente a avaliação de aulas na plataforma Odette.

**P: O aplicativo é oficial do Grupo JBS?**  
R: Não. O nome foi usado apenas de forma ilustrativa e não há nenhuma relação oficial com o Grupo JBS.

**P: Em quais sistemas operacionais o aplicativo funciona?**  
R: Foi projetado principalmente para Windows, mas muitas funcionalidades também funcionam em Linux. As notificações e automação visual são otimizadas para Windows.

### Técnicas

**P: O que fazer se as notificações não aparecerem?**  
R: Verifique se:
1. O processo `alert.py` está em execução (verificável em App Info)
2. Os horários estão configurados corretamente na classe `data`
3. O sistema permite notificações do aplicativo Python

**P: Como adicionar novos horários para notificação?**  
R: Edite a lista `date` na classe `data` no arquivo `data.py`. O formato é uma tupla (hora, minuto).

**P: A automação não está encontrando os elementos na tela. O que fazer?**  
R: A automação depende da resolução da tela e elementos visuais. Verifique se:
1. A imagem de referência (5_estrelas.png) existe na pasta icons
2. A resolução da tela corresponde à esperada pelo sistema
3. A interface da Odette não mudou desde a última atualização do aplicativo

**P: Como ativar o modo de desenvolvimento?**  
R: Acesse o menu Config (opção 3) e selecione "Ativar Dev Mode" (opção 1).

## Contato e Suporte

Para suporte, sugestões ou contribuições, entre em contato com os desenvolvedores:

**Quittoツ**  
Dev | Fundador  
[Instagram](https://www.instagram.com/quittooficial/) | [GitHub](https://github.com/QuittoGames) | [Twitter](https://x.com/QuittoGames)

**MagaNinjaPadovani**  
Dev Scripts | Dev  
[Instagram](https://www.instagram.com/meganinjapadovani/)

---

> **Aviso Legal**: Este aplicativo está sob a Licença MIT e foi desenvolvido para fins educacionais. O nome "JBS" foi usado apenas de forma ilustrativa e não há relação oficial com o Grupo JBS. O aplicativo foi desenvolvido para promover os estudos dos alunos do Germinare Tech. 