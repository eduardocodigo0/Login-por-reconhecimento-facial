import sqlite3
from tkinter import messagebox


def baixarNivel(cod):
    try:

        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        query = "UPDATE faces SET nivel = 0 WHERE id = {};".format(cod)
        cursor.execute(query)
        conn.commit()
        cursor.close()
        return True

    except sqlite3.Error as erro:
        
        print("ERRO AO BAIXAR NIVEL: ", erro)
        return False
    finally:

        if(conn):
            conn.close()


def selecionar(cod):
    resultado = False

    try:

        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        query = "SELECT * FROM faces where id = {};".format(cod)

        cursor.execute(query)
        resultado = cursor.fetchall()
        return resultado

    except sqlite3.Error as erro:

        print("ERRO AO SELECIONAR DADOS: ", erro)

    finally:

        if(conn):
            conn.close()

def listar():
    resultado = False

    try:

        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        query = "SELECT * FROM faces;"
        cursor.execute(query)
        resultado = cursor.fetchall()
        return resultado

    except sqlite3.Error as erro:

        print("ERRO AO LISTAR DADOS: ", erro)

    finally:

        if(conn):
            conn.close()

    
def deletar(cod):
     
    resultado = False

    try:

        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        query = "DELETE FROM faces WHERE id = {};".format(cod)
        cursor.execute(query)
        conn.commit()
        cursor.close()
        resultado = True

    except sqlite3.Error as erro:
        
        print("ERRO AO DELETAR: ", erro)
    
    finally:

        if(conn):
            conn.close()

    return resultado


def adicionar(nome, foto, nivel):

    try:

        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        query = "INSERT INTO faces (nome, foto, nivel) VALUES (?, ?, ?);"
        dados = (nome, foto, nivel)
        cursor.execute(query, dados)
        conn.commit()
        cursor.close()
        return True

    except sqlite3.Error as erro:
        
        print("ERRO AO INSERIR NO BANCO: ", erro)
        return False
    finally:

        if(conn):
            conn.close()     