# JBS Work Flow


# Notas da Nova Versão - Script Automatico De Avaliaçao 4.0v 

## ✨ Novidades

### 🤖 Script Automático de Autoavaliação
- Implementado novo sistema de automação para executar tarefas sem intervenção manual
- Por padrão, o recurso vem **desabilitado** por questões de segurança
- Pode ser ativado através do menu de Configurações (opção 4)
- Executa ações automáticas usando mouse e navegador quando as notificações são acionadas

### 🎮 Sistema de Controle
- Novo canal de testes disponível para experimentar funcionalidades em desenvolvimento
- Interface de controle aprimorada para gerenciamento de tarefas
- Monitoramento avançado do status das automações

### 🖼️ Widgets (Preview)
- Iniciada a implementação de widgets na versão principal
- Permite visualização rápida de informações importantes sem abrir o menu principal
- Acesso simplificado às funcionalidades mais utilizadas
- Configuração personalizada dos widgets através do menu de configurações
- Ainda em fase inicial de desenvolvimento

## 📋 Funcionalidades Mantidas
### Melhorias da versão 3.1
- **Módulo To Do**: Gerenciamento completo de tarefas (adicionar, remover, visualizar)
- **Notificações**: Configuração baseada em tempo com alertas automáticos
- **Módulo IA**: Integração com serviços Ollama (acessível via modo Dev)

## ⚠️ Observações
- Esta versão pode apresentar comportamentos inesperados por estar em fase de testes
- Recomendamos fazer backup dos dados antes de atualizar
- Código da versão: **K2023_4_H1_30_test**

## 🔧 Como Ativar o Script Automático
1. Acesse o menu principal
2. Selecione a opção "3. Config"
3. Escolha "4. Ativar Script De UI"
4. Confirme a ativação digitando "y"

## 🔜 Próximos Passos
- Criaçao De Um Sistema De Wingets
- Expansão das funcionalidades automáticas
- Melhorias na integração com IA
  
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
  exit
````

## Sistema de Versão

O **JBS Work Flow** utiliza um sistema de versão para organizar e identificar as diferentes atualizações e estágios de desenvolvimento do projeto. A estrutura de versão segue o formato:
**K{ANO}_{MES}_H{SEMESTRE}_TypeVersion**


### Explicação dos Componentes:
- **K**: Prefixo de identificação do projeto.
- **{ANO}_{MES}**: Representa o **ano** e **mês** em que a versão foi lançada.
- **H{SEMESTRE}**: Indica o semestre do ano. Por exemplo, `H1` para o primeiro semestre e `H2` para o segundo semestre.
- **TypeVersion**: Tipo de versão, que pode ser:
  - **10** = `release` (versão estável com grandes mudanças).
  - **20** = `dev` (versão de desenvolvimento, com novas funcionalidades e experimentações).
  - **30** = `test` (versão de teste, com correções e ajustes).

### Exemplo:
- **K2025_03_H1_10_release**: Versão final (release) do primeiro semestre de 2025, lançada em março.
- **K2025_03_H2_20_dev**: Versão de desenvolvimento do segundo semestre de 2025, lançada em março.
- **K2025_03_H1_30_test**: Versão de teste do primeiro semestre de 2025, lançada em março.

Este sistema de versões permite identificar claramente em qual semestre a versão foi lançada, seu tipo (estável, em desenvolvimento ou em teste) e a data de lançamento.


# 🚨 Aviso Legal  

**Este aplicativo não possui nenhuma relação oficial com o Grupo JBS.**  
A menção ao nome foi apenas ilustrativa, pois a aplicação foi desenvolvida com o objetivo de promover os estudos dos alunos do **Germinare Tech**.  

O nome do aplicativo **pode ser alterado a qualquer momento** e ele poderá se tornar um projeto independente, pertencente exclusivamente ao seu criador.  

# 🛠️ Equipe

**Quittoツ**  
Dev | Fundador
[Instagram](https://www.instagram.com/quittooficial/) | [GitHub](https://github.com/QuittoGames) | [Twiter](https://x.com/QuittoGames)

---

**MagaNinjaPadovani**  
Dev Scripts | Dev  
[Instagram](https://www.instagram.com/meganinjapadovani/)

