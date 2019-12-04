import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from tkinter import filedialog
from gerenciador_db import *
import re 
import os
import shutil
from loginCamera import identificar
from cria_banco import *
from testa_existencia_banco import *
from cadastro_com_foto import *
from datetime import datetime


fonte = "Helvetica 16 bold"
fonte_pequena = "Helvetica 12"

LOCAL_DIR = os.path.dirname(os.path.realpath(__file__))
print(LOCAL_DIR)

# ===== Acoes componentes ==================================================================

def btnCam_Click():

    messagebox.showinfo("Importante", "Aperte (q) para desligar a camera!")
    janela_principal.destroy()
    identificar()
    
#========= Criando janela principal =======================================================

if bancoExiste():
    janela_principal = tk.Tk()
    janela_principal.title("Reconhecimento facial")
    janela_principal["bg"] = "black"
    janela_principal.resizable(0, 0)
    largura = 400
    altura = 200

    #Posicionando janela principal no centro da tela
    screen_width = janela_principal.winfo_screenwidth()
    screen_height = janela_principal.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (largura/2))
    y_cordinate = int((screen_height/2) - (altura/2))

    janela_principal.geometry("{}x{}+{}+{}".format(largura, altura, x_cordinate, y_cordinate))

    #Componentes da janela principal
    btnCam = tk.Button(janela_principal, text="Entrar", bg="yellow", fg="black", command=btnCam_Click, font=fonte)
    btnCam.pack(fill=tk.X, pady=60)



    #Loop principal da GUI
    janela_principal.mainloop()

else:

    criarBanco()
    os.system("mkdir img\cadastrados")
    f = open("log.txt", "w+")
    f.write("Arquivo de log criado em: {}".format(datetime.now()))
    f.close()
    cadastro()
    
    


