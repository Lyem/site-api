import pymysql
from datetime import datetime
import key

conexao = pymysql.connect(
        host=key.host,
        user=key.user,
        passwd=key.passwd,
        database=key.database
    )

class models:

    def criabancodedados(self):
        cursor = conexao.cursor()

        cursor.execute('CREATE TABLE IF NOT EXISTS usuario(id_usuario INT PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(30) NOT NULL UNIQUE, email VARCHAR(100) NOT NULL UNIQUE, senha VARCHAR(40) NOT NULL, data DATE NOT NULL)default charset = utf8;')

        cursor.execute('CREATE TABLE IF NOT EXISTS admuser(id_adm INT PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(30) NOT NULL UNIQUE, email VARCHAR(100) NOT NULL UNIQUE, senha VARCHAR(40))default charset = utf8; ')

        cursor.execute('CREATE TABLE IF NOT EXISTS manga(id_manga INT PRIMARY KEY AUTO_INCREMENT,capa VARCHAR(150) NOT NULL, nome  VARCHAR(150), data DATE, status varchar(30), nota int, sinopse VARCHAR(280))default charset = utf8;')

        cursor.execute('CREATE TABLE IF NOT EXISTS capitulos(id_capitulos INT PRIMARY KEY AUTO_INCREMENT, numero_do_capitulo int, nome VARCHAR(50), data DATE,id_domanga int, CONSTRAINT ids FOREIGN KEY (id_domanga) REFERENCES manga (id_manga))default charset = utf8;')

        cursor.close()

    def cadastrarusuarios(nome, email, senha, data):
        data = datetime.strptime(data, '%d/%m/%Y').date()
        cursor = conexao.cursor()
        sql = "INSERT INTO usuario(nome, email, senha, data) VALUES (%s,%s,%s,%s)"
        valor = (nome, email, senha, data)
        cursor.execute(sql, valor)
        conexao.commit()
        cursor.close()
        pass

    def cadastroadm(nome, email, senha):
        cursor = conexao.cursor()
        sql = "INSERT INTO admuser(nome, email, senha) VALUES(%s,%s,%s)"
        valor = (nome, email, senha)
        cursor.execute(sql,valor)
        conexao.commit()
        cursor.close()

    def cadastromanga(capa, nome, data, status, nota, sinopse):
        data = datetime.strptime(data, '%d/%m/%Y').date()
        cursor = conexao.cursor()
        sql = "INSERT INTO manga(capa, nome, data, status, nota, sinopse) VALUES(%s,%s,%s,%s,%s,%s)"
        valor = (capa, nome, data, status, nota, sinopse)
        cursor.execute(sql, valor)
        conexao.commit()
        cursor.close()
