import psycopg2


def conectar():
    """
    Função para conectar ao Servidor de Banco de Dados Postgresql
    """
    try:
        conn = psycopg2.connect(
            database='pmvn',
            host='localhost',
            user='postgres',
            password='j&ov@123',
        )
        return conn
    except psycopg2.Error as e:
        print(f'Erro na conexão ao PostgreSQL {e}')


def desconectar(conn):

    if conn:
        conn.close()


def listar():

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM servidor')
    servidores = cursor.fetchall()

    if len(servidores) > 0:
        print('Listando Servidores')
        print('------------------------------')
        for servidor in servidores:
            print(f'ID: {servidor[0]}')
            print(f'Matricula: {servidor[1]}')
            print(f'Nome: {servidor[2]}')
            print(f'Função {servidor[3]}')
            print(f'Lotação {servidor[4]}')
            print(f'Vencimento {servidor[5]}')
            print('---------------------------')
    else:
        print('Não exite servidores cadastrados')
        desconectar(conn)


def inserir():
    """
    Função para inserir um Servidor
    """
    conn = conectar()
    cursor = conn.cursor()

    matricula = input("Informe a Matricula do Servidor: ")
    nome = input("Informe o Nome do Servidor: ")
    funcao = input("Informe a Função do Servidor: ")
    lotacao = input("Informe a Lotação do Servidor: ")
    vencimento = input("Informe vencimento do Servidor: ")

    cursor.execute(f"INSERT INTO servidor (matricula, nome, funcao, lotacao, vencimento_bruto) VALUES ('{matricula}', '{nome}', '{funcao}', '{lotacao}', {vencimento})")
    conn.commit()

    if cursor.rowcount == 1:
        print("Servidor inserido com Sucesso!")
    else:
        print("Não foi possivél inserir o Servidor!")
    desconectar(conn)


def atualizar():
    """
    Função para Atualizar um servidor
    """

    conn = conectar()
    cursor = conn.cursor()

    codigo = int(input("Informe o codigo do servidor: "))
    matricula = int(input("Informe a Matricula do Servidor: "))
    nome = input("Informe o Nome do Servidor: ")
    funcao = input("Informe a Função do Servidor: ")
    lotacao = input("Informe a Lotação do Servidor: ")
    vencimento = input("Informe vencimento do Servidor: ")

    cursor.execute(f"UPDATE servidor SET matricula={matricula}, nome='{nome}', funcao='{funcao}', lotacao='{lotacao}', vencimento_bruto='{vencimento}' WHERE id={codigo}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f"O servidor {nome} foi atualizado com sucesso!")
    else:
        print("Erro ao Atualizar o servidor!")
    desconectar(conn)


def deletar():
    """
    Função para Excluir um servidor
    """

    conn = conectar()
    cursor = conn.cursor()

    id = int(input("Informe o id do servidor a ser excluido!"))

    cursor.execute(f" DELETE FROM servidor WHERE id={id}")
    conn.commit()

    if cursor.rowcount == 1:
        print(f"O servidor foi excluido com sucesso!")
    else:
        print("Erro ao excluir o servidro!")
    desconectar(conn)


