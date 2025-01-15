import unittest
import pandas as pd
import sqlite3
from io import StringIO
from gerenciadorexcel import listar_tarefas as listar_tarefas_excel, adicionar_tarefa as adicionar_tarefa_excel
from gerenciadorsqlite3 import listar_tarefas as listar_tarefas_sqlite, adicionar_tarefa as adicionar_tarefa_sqlite
from gerenciadorcsv import listar_tarefas as listar_tarefas_csv, adicionar_tarefa as adicionar_tarefa_csv

class TestGerenciadores(unittest.TestCase):

    def setUp(self):
        # DataFrame para os testes com CSV e Excel
        self.df = pd.DataFrame({
            'tarefa': ['Tarefa 1'],
            'descricao': ['Descrição 1'],
            'status': ['Pendente'],
            'data_inicio': ['01/01/2025'],
            'data_termino': ['02/01/2025'],
            'prazo': ['05/01/2025']
        })

        # Configuração do banco de dados SQLite
        self.conexao = sqlite3.connect(':memory:')
        self.cursor = self.conexao.cursor()
        self.cursor.execute('''
            CREATE TABLE tarefas (
                id INTEGER PRIMARY KEY,
                tarefa TEXT NOT NULL,
                descricao TEXT,
                status TEXT NOT NULL,
                data_inicio TEXT,
                data_termino TEXT,
                prazo TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            INSERT INTO tarefas (tarefa, descricao, status, data_inicio, data_termino, prazo) 
            VALUES ('Tarefa 1', 'Descrição 1', 'Pendente', '01/01/2025', '02/01/2025', '05/01/2025')
        ''')
        self.conexao.commit()

    def test_listar_tarefas_excel(self):
        result = listar_tarefas_excel(self.df)
        self.assertFalse(result.empty)

    def test_adicionar_tarefa_excel(self):
        new_df = adicionar_tarefa_excel(self.df)
        self.assertEqual(len(new_df), len(self.df) + 1)

    def test_listar_tarefas_sqlite(self):
        result = listar_tarefas_sqlite(self.cursor)
        self.assertTrue(len(result) > 0)

    def test_adicionar_tarefa_sqlite(self):
        adicionar_tarefa_sqlite(self.cursor, self.conexao)
        self.cursor.execute('SELECT COUNT(*) FROM tarefas')
        result = self.cursor.fetchone()[0]
        self.assertEqual(result, 2)

    def test_listar_tarefas_csv(self):
        result = listar_tarefas_csv(self.df)
        self.assertFalse(result.empty)

    def test_adicionar_tarefa_csv(self):
        new_df = adicionar_tarefa_csv(self.df)
        self.assertEqual(len(new_df), len(self.df) + 1)

    def tearDown(self):
        self.conexao.close()

if __name__ == '__main__':
    unittest.main()
