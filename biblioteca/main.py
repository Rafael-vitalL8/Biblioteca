import psycopg2
from psycopg2 import sql
from datetime import date



def conectar_banco():
    return psycopg2.connect(
    dbname='biblioteca',
    user='postgres',
    password='12345',
    host='localhost',
    port='5432'
)
class Biblioteca:
    def __init__(self, dbname, user, password, host='localhost'):
        self.conn = psycopg2.connect(dbname='biblioteca', user='postgres', password='12345', host='localhost', port='5432' )
        self.cursor = self.conn.cursor()

    def vizualizar_livros(self):
        self.cursor.execute('''SELECt * FROM books;''')
        registros = self.cursor.fetchall()
        
        for registro in registros:
            
            print(registro)
    
            

    def adicionar_livro(self, titulo, autor, ano_publicacao, numero_paginas):
        self.cursor.execute('''INSERT INTO books (titulo, autor, ano_publicacao, numero_paginas) VALUES (%s, %s, %s, %s)''',
                                (titulo, autor, ano_publicacao, numero_paginas))
        self.conn.commit()
        print('\nLivro adicionado com sucesso.')

    def adicionar_usuario(self, nome, data_nascimento, telefone):
        self.cursor.execute('''INSERT INTO members (nome, data_nascimento, telefone) VALUES (%s, %s, %s)''',
                            (nome, data_nascimento, telefone))
        self.conn.commit()
        print('\nCadastro realizado')

    def emprestar_livro(self, id_livro, id_membro, data_, data_1, stat):
        self.cursor.execute('''INSERT INTO loans (id_livro, id_membro, data_retirada, data_devolucao, status)''',
                             (id_livro, id_membro, data_, data_1, stat))
        
        
        
        self.conn.commit()
        print("Livro emprestado com sucesso.")
        
        

    def fechar(self):
            self.cursor.close()
            self.conn.close()
            print('biblioteca encerrada')


def menu():
    biblioteca = Biblioteca(dbname='biblioteca', user='postgres', password='12345' )

    while True:
        print('\n MENU:\n')
        print('0. vizualizar Livros:')
        print('1. Adicionar Livro')
        print('2. Adicionar Usuário')
        print('3. Emprestar Livro')
        print('4. Devolver Livro')
        print('5. Sair')
        escolha = input('Resposta : ')

        if escolha == '0':
            biblioteca.vizualizar_livros()
            

        elif escolha == '1':
            titulo = input('Título do livro: ')
            autor = input('Autor do livro: ')
            ano_public = input('ano de publicação')
            numero_pg = input ('numerro de páginas')
            biblioteca.adicionar_livro(titulo, autor, ano_public, numero_pg)

        elif escolha == '2':
            nome_ = input('Digite seu nome: ')
            data_nasc = input('Digite a data de Nascimento: ')
            tel = input('Telefone, ex:5555-5555: ')
            biblioteca.adicionar_usuario(nome_, data_nasc, tel)

        elif escolha == '3':
            biblioteca.vizualizar_livros()
            print('Digite ID do livro       ')
            livro_id = input('ID do livro: ')
            usuario_id = input('ID do usuário: ')
            data_ = date.today()
            data_1 = '25-09-2024'
            stat = False
            biblioteca.emprestar_livro(livro_id, usuario_id, data_, data_1, stat)

        elif escolha == '5':
         print('Biblioteca encerrada')
         break
        else:
            print('erro ao conectar')




menu()