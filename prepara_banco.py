import pymysql

# Create a connection object
databaseServerIP = "127.0.0.1"  # IP address of the MySQL database server
databaseServerPort = 3306
databaseUserName = "root"  # User name of the database server
databaseUserPassword = "rootmysql"  # Password for the database user
newDatabaseName = "jogoteca"  # Name of the database that is to be created
charSet = "utf8mb4"  # Character set
cusrorType = pymysql.cursors.DictCursor


def _criar_conexao():
    return pymysql.connect(host=databaseServerIP, port=databaseServerPort, user=databaseUserName,
                           password=databaseUserPassword,
                           charset=charSet, cursorclass=cusrorType)


def _delete_database_jogoteca():
    # Drop database 'jogoteca' if it exist
    sqlQuery = "SHOW DATABASES"
    cursorInstance.execute(sqlQuery)
    databaseList = cursorInstance.fetchall()
    for datatbase in databaseList:
        if datatbase['Database'] == newDatabaseName:
            print(f'Deletando Database {newDatabaseName}!!')
            sqlStatement = "DROP DATABASE " + newDatabaseName
            cursorInstance.execute(sqlStatement)


def _criar_tabelas():
    # Criar tabelas
    stat = "USE " + newDatabaseName
    cursorInstance.execute(stat)
    criar_tabela_jogo = "  CREATE TABLE `jogo` ( `id` int(11) NOT NULL AUTO_INCREMENT, `nome` varchar(50) COLLATE utf8_bin NOT NULL, `categoria` varchar(40) COLLATE utf8_bin NOT NULL, `console` varchar(20) NOT NULL, PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin"
    criar_tabela_usuario = " CREATE TABLE `usuario` (`id` varchar(8) COLLATE utf8_bin NOT NULL, `nome` varchar(20) COLLATE utf8_bin NOT NULL, `senha` varchar(8) COLLATE utf8_bin NOT NULL,PRIMARY KEY (`id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin"
    cursorInstance.execute(criar_tabela_jogo)
    cursorInstance.execute(criar_tabela_usuario)
    # SQL query string
    sqlQuery = "show tables"
    # Execute the sqlQuery
    cursorInstance.execute(sqlQuery)
    # Fetch all the rows
    rows = cursorInstance.fetchall()
    for row in rows:
        print(f"tabela {row['Tables_in_jogoteca']}: criada")


def _carga_inicial_usuarios():
    # inserindo usuarios
    sqlQuery = "INSERT INTO jogoteca.usuario (id, nome, senha) VALUES (%s, %s, %s)"
    valores = [
        ('luan', 'Luan Marques', 'flask'),
        ('nico', 'Nico', '7a1'),
        ('danilo', 'Danilo', 'vegas')
    ]
    print('inserindo usuarios...')
    cursorInstance.executemany(sqlQuery, valores)
    cursorInstance.execute('select * from jogoteca.usuario')
    print(' -------------  Usuários:  -------------')
    for user in cursorInstance.fetchall():
        print(user['id'] + ' - ' + user['senha'])


def _carga_inicial_jogos():
    # inserindo jogos
    cursorInstance.executemany(
        'INSERT INTO jogoteca.jogo (nome, categoria, console) VALUES (%s, %s, %s)',
        [
            ('God of War 4', 'Ação', 'PS4'),
            ('NBA 2k18', 'Esporte', 'Xbox One'),
            ('Rayman Legends', 'Indie', 'PS4'),
            ('Super Mario RPG', 'RPG', 'SNES'),
            ('Super Mario Kart', 'Corrida', 'SNES'),
            ('Fire Emblem Echoes', 'Estratégia', '3DS'),
        ])
    cursorInstance.execute('select * from jogoteca.jogo')
    print(' -------------  Jogos:  -------------')
    for jogo in cursorInstance.fetchall():
        print(jogo['nome'])


print('Conectando...')
conn = _criar_conexao()
try:
    # Create a cursor object
    cursorInstance = conn.cursor()

    _delete_database_jogoteca()

    # Execute the create database SQL statment through the cursor instance
    print(f'Criando Database {newDatabaseName}!!')
    sqlStatement = "CREATE DATABASE " + newDatabaseName
    cursorInstance.execute(sqlStatement)

    _criar_tabelas()

    _carga_inicial_usuarios()

    _carga_inicial_jogos()

    # commitando senão nada tem efeito
    conn.commit()
except Exception as e:
    print("Exeception occured:{}".format(e))
finally:
    conn.close()
