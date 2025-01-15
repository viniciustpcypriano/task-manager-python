import pandas as pd

# Função para listar tarefas
def listar_tarefas(df):
    if not df.empty:
        print('\nVocê tem as seguintes tarefas:')
        for idx, tarefa in df.iterrows():
            print(f'\n{idx + 1}. | Tarefa: {tarefa["tarefa"]} | Descrição: {tarefa["descricao"]} | Status: {tarefa["status"]} | Data de Início: {tarefa["data_inicio"]} | Data de Término: {tarefa["data_termino"]} | Prazo: {tarefa["prazo"]} |')
        return df
    else:
        print('\nNão há tarefas pendentes')
        return df

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
def adicionar_tarefa(df):
    adicionar_tarefa = input('\nDeseja adicionar uma nova tarefa? (sim/não): ').strip().lower()
    if adicionar_tarefa == 'sim':
        tarefa = input('Título da tarefa: ')
        descricao = input('Descrição da tarefa: ')
        status = input('Status da tarefa: ')
        data_inicio = obter_data('Data de início (DDMMYYYY): ')
        data_termino = obter_data('Data de término (DDMMYYYY): ')
        prazo = obter_data('Prazo (DDMMYYYY): ')
        nova_tarefa = pd.DataFrame({
            'tarefa': [tarefa],
            'descricao': [descricao],
            'status': [status],
            'data_inicio': [data_inicio],
            'data_termino': [data_termino],
            'prazo': [prazo]
        })
        df = pd.concat([df, nova_tarefa], ignore_index=True)
        print('\nNova tarefa adicionada com sucesso!')
    return df

# Função para excluir tarefa
def excluir_tarefa(df):
    excluir_tarefa = input('\nDeseja excluir alguma tarefa? (sim/não): ').strip().lower()
    if excluir_tarefa == 'sim':
        df = listar_tarefas(df)
        numero_tarefa = int(input('Digite o número da tarefa que deseja excluir: ').strip()) - 1
        if 0 <= numero_tarefa < len(df):
            tarefa_a_excluir = df.iloc[numero_tarefa]['tarefa']
            df = df.drop(numero_tarefa).reset_index(drop=True)
            print(f'Tarefa "{tarefa_a_excluir}" excluída com sucesso!')
    return df

# Função para atualizar tarefa
def atualizar_tarefas(df):
    df = listar_tarefas(df)
    numero_tarefa = int(input('Digite o número da tarefa que deseja atualizar: ').strip()) - 1
    if 0 <= numero_tarefa < len(df):
        tarefa_a_atualizar = df.iloc[numero_tarefa]
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
        
        df.at[numero_tarefa, campo] = novo_valor
        print(f'Tarefa "{tarefa_a_atualizar["tarefa"]}" atualizada com sucesso!')
    return df

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

# Carrega ou cria o DataFrame
try:
    df = pd.read_csv('tarefas_csv.csv')
except FileNotFoundError:
    df = pd.DataFrame(columns=['tarefa', 'descricao', 'status', 'data_inicio', 'data_termino', 'prazo'])

# Executa o programa
try:
    listar_tarefas(df)
    while True:
        escolha = menu()
        if escolha == '1':
            df.to_csv('tarefas_csv.csv', index=False)
            print("\nEncerrando o programa. Até a próxima!")
            break
        elif escolha == '2':
            listar_tarefas(df)
        elif escolha == '3':
            df = adicionar_tarefa(df)
        elif escolha == '4':
            df = excluir_tarefa(df)
        elif escolha == '5':
            df = atualizar_tarefas(df)
        else:
            print("\nOpção inválida, tente novamente.")
finally:
    df.to_csv('tarefas_csv.csv', index=False)
