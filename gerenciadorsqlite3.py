import sqlite3

# Função para listar tarefas
def listar_tarefas(cursor):
    cursor.execute('SELECT COUNT(*) FROM tarefas')
    qtd_tarefas = cursor.fetchone()[0]
    if qtd_tarefas > 0:
        cursor.execute('SELECT * FROM tarefas') 
        tarefas = cursor.fetchall()
        print('\nVocê tem as seguintes tarefas:') 
        for idx, tarefa in enumerate(tarefas, start=1):
            print(f'\n{idx}. | Tarefa: {tarefa[1]} | Descrição: {tarefa[2]} | Status: {tarefa[3]} | Data de Início: {tarefa[4]} | Data de Término: {tarefa[5]} | Prazo: {tarefa[6]} |')
        return tarefas
    else: 
        print('\nNão há tarefas pendentes')
        return []

# Função para obter data formatada
def obter_data(prompt): 
    while True: 
        data = input(prompt).strip() 
        if len(data) == 8 and data.isdigit(): 
            dia = data[:2] 
            mes = data[2:4] 
            ano = data[4:] 
            data_formatada = f'{dia}/{mes}/{ano}' 
            return data_formatada 
        else: 
            print("Formato inválido. Por favor, insira a data no formato DDMMYYYY, somente números.")

# Função para adicionar tarefa
def adicionar_tarefa(cursor, conexao):
    adicionar_tarefa = input('\nDeseja adicionar uma nova tarefa? (sim/não): ').strip().lower() 
    if adicionar_tarefa == 'sim': 
        tarefa = input('Título da tarefa: ') 
        descricao = input('Descrição da tarefa: ') 
        status = input('Status da tarefa: ') 
        data_inicio = obter_data('Data de início (DDMMYYYY): ') 
        data_termino = obter_data('Data de término (DDMMYYYY): ') 
        prazo = obter_data('Prazo (DDMMYYYY): ') 
        cursor.execute(''' INSERT INTO tarefas (tarefa, descricao, status, data_inicio, data_termino, prazo) VALUES (?, ?, ?, ?, ?, ?) ''', (tarefa, descricao, status, data_inicio, data_termino, prazo)) 
        conexao.commit() 
        print('\nNova tarefa adicionada com sucesso!')

# Função para excluir tarefa
def excluir_tarefa(cursor, conexao):
    excluir_tarefa = input('\nDeseja excluir alguma tarefa? (sim/não): ').strip().lower() 
    if excluir_tarefa == 'sim': 
        tarefas = listar_tarefas(cursor)
        numero_tarefa = int(input('Digite o número da tarefa que deseja excluir: ').strip()) - 1
        if 0 <= numero_tarefa < len(tarefas):
            tarefa_a_excluir = tarefas[numero_tarefa][1]
            cursor.execute('DELETE FROM tarefas WHERE tarefa = ?', (tarefa_a_excluir,)) 
            conexao.commit() 
            print(f'Tarefa "{tarefa_a_excluir}" excluída com sucesso!')

# Função para atualizar tarefa
def atualizar_tarefas(cursor, conexao):
    tarefas = listar_tarefas(cursor)
    numero_tarefa = int(input('Digite o número da tarefa que deseja atualizar: ').strip()) - 1
    if 0 <= numero_tarefa < len(tarefas):
        tarefa_a_atualizar = tarefas[numero_tarefa]
        print("O que você deseja atualizar?")
        print("1. Título")
        print("2. Descrição")
        print("3. Status")
        print("4. Data de Início")
        print("5. Data de Término")
        print("6. Prazo")
        opcao = int(input("Digite o número da sua escolha: ").strip())
        
        novo_valor = input('Digite o novo valor: ').strip()
        campo = {1: 'tarefa', 2: 'descricao', 3: 'status', 4: 'data_inicio', 5: 'data_termino', 6: 'prazo'}[opcao]
        
        cursor.execute(f'UPDATE tarefas SET {campo} = ? WHERE id = ?', (novo_valor, tarefa_a_atualizar[0])) 
        conexao.commit() 
        print(f'Tarefa "{tarefa_a_atualizar[1]}" atualizada com sucesso!')

# Função de menu
def menu(): 
    print("\nO que você deseja fazer agora?") 
    print("1. Encerrar programa") 
    print("2. Ver lista de tarefas atualizadas") 
    print("3. Adicionar tarefa") 
    print("4. Excluir tarefa") 
    print("5. Atualizar tarefa") 
    escolha = input("Digite o número da sua escolha: ").strip() 
    return escolha

# Conecta ao banco de dados (ou cria um novo)
conexao = sqlite3.connect('tarefas.db')
cursor = conexao.cursor()

# Cria a tabela se não existir
cursor.execute('''
CREATE TABLE IF NOT EXISTS tarefas (
    id INTEGER PRIMARY KEY,
    tarefa TEXT NOT NULL,
    descricao TEXT,
    status TEXT NOT NULL,
    data_inicio TEXT,
    data_termino TEXT,
    prazo TEXT NOT NULL
)
''')
# Executa o programa
try:
    listar_tarefas(cursor)
    while True: 
        escolha = menu() 
        if escolha == '1': 
            print("\nEncerrando o programa. Até a próxima!") 
            break 
        elif escolha == '2': 
            listar_tarefas(cursor) 
        elif escolha == '3': 
            adicionar_tarefa(cursor, conexao) 
        elif escolha == '4': 
            excluir_tarefa(cursor, conexao)
        elif escolha == '5': 
            atualizar_tarefas(cursor, conexao)
        else: 
            print("\nOpção inválida, tente novamente.")
finally:
    conexao.close()
