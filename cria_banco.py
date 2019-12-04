import sqlite3
from tkinter import messagebox

def criarBanco():
        conn = sqlite3.connect('banco.db')
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE faces (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                foto TEXT NOT NULL,
                nivel INTEGER NOT NULL
                
        );
        """)
        print("Banco criado")
        conn.commit()
        conn.close()
        
