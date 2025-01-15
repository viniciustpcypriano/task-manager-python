# Gerenciadores de Tarefas (Excel, SQLite e CSV)

Este repositório contém três arquivos que implementam funcionalidades para gerenciar tarefas utilizando diferentes formatos de armazenamento: Excel, SQLite e CSV. Os arquivos permitem a manipulação de tarefas através de operações como listar, adicionar, excluir e atualizar tarefas.

## Descrição dos Arquivos

### 1. `gerenciadorexcel.py`

Este arquivo utiliza a biblioteca `pandas` para gerenciar tarefas armazenadas em um arquivo Excel (`tarefas_excel.xlsx`). As funções principais incluem:

- **listar\_tarefas(df)**: Exibe a lista de tarefas existentes no DataFrame.
- **obter\_data(prompt)**: Solicita uma data ao usuário no formato `DDMMYYYY`.
- **adicionar\_tarefa(df)**: Permite ao usuário adicionar uma nova tarefa ao DataFrame.
- **excluir\_tarefa(df)**: Exclui uma tarefa específica do DataFrame.
- **atualizar\_tarefas(df)**: Atualiza os dados de uma tarefa existente no DataFrame.

### 2. `gerenciadorsqlite3.py`

Este arquivo utiliza a biblioteca `sqlite3` para gerenciar tarefas armazenadas em um banco de dados SQLite (`tarefas.db`). As funções principais incluem:

- **listar\_tarefas(cursor)**: Lista todas as tarefas existentes na tabela do banco de dados.
- **obter\_data(prompt)**: Solicita uma data ao usuário no formato `DDMMYYYY`.
- **adicionar\_tarefa(cursor, conexao)**: Adiciona uma nova tarefa ao banco de dados.
- **excluir\_tarefa(cursor, conexao)**: Exclui uma tarefa específica do banco de dados.
- **atualizar\_tarefas(cursor, conexao)**: Atualiza os dados de uma tarefa existente no banco de dados.

### 3. `gerenciadorcsv.py`

Este arquivo também utiliza a biblioteca `pandas`, mas para gerenciar tarefas armazenadas em um arquivo CSV (`tarefas_csv.csv`). As funções principais são semelhantes às do `gerenciadorexcel.py`, incluindo:

- **listar\_tarefas(df)**: Exibe a lista de tarefas existentes no DataFrame.
- **obter\_data(prompt)**: Solicita uma data ao usuário no formato `DDMMYYYY`.
- **adicionar\_tarefa(df)**: Permite ao usuário adicionar uma nova tarefa ao DataFrame.
- **excluir\_tarefa(df)**: Exclui uma tarefa específica do DataFrame.
- **atualizar\_tarefas(df)**: Atualiza os dados de uma tarefa existente no DataFrame.

## Como Executar

Para executar qualquer um dos arquivos, você pode rodá-los diretamente no terminal ou no ambiente de sua preferência. Cada arquivo possui um menu interativo que permite ao usuário escolher as ações a serem realizadas.

### Executando o `gerenciadorexcel.py`

```bash
python gerenciadorexcel.py
```

### Executando o `gerenciadorsqlite3.py`

```bash
python gerenciadorsqlite3.py
```

### Executando o `gerenciadorcsv.py`

```bash
python gerenciadorcsv.py
```

## Funcionalidades Comuns

Todos os três arquivos compartilham as seguintes funcionalidades principais:

- **Listar tarefas**: Exibe todas as tarefas armazenadas.
- **Adicionar tarefa**: Permite ao usuário adicionar uma nova tarefa.
- **Excluir tarefa**: Permite ao usuário excluir uma tarefa existente.
- **Atualizar tarefa**: Permite ao usuário atualizar os dados de uma tarefa existente.

## Requisitos

- Python 3.6+
- Bibliotecas necessárias: `pandas`, `sqlite3`

## Testes Unitários

O arquivo de testes unitários criado (`testeunitario.py`) abrange as principais funções dos três arquivos e pode ser executado com o seguinte comando:

```bash
python testeunitario.py
```

## Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato!




