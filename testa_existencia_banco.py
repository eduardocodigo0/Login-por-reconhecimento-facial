import sqlite3

def bancoExiste():
    link = 'file:banco.db?mode=rw'
    try:

        conn = sqlite3.connect(link, uri=True)
        return True

    except(sqlite3.OperationalError):
        
        print("Banco nao existe")
        return False