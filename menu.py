
import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from tkinter import filedialog
from gerenciador_db import *
import re 
import os
import shutil
from cadastro_com_foto import *

def janela(nivel_de_acesso):

    info = {
        "ultra_secretas":[  "Vazamento de oleo pode ter sido proposital",
                            "Aumento de poluicao da agua em cidades proximas da fronteira com a bolivia"
                    ],

        "secretas":[    "Projeto iniciativa publica para reviver os rios atingidos pelo estouro da barragem em Minas Gerais"],

        "publicas":[    "Ararinha azul foi oficialmente extinta",
                        "Amazonia sofre com aumento no nivel de queimadas",
                        "Usinas de desalinizacao podem acabar com a sede no nordeste"
                    ]
    }

    vis_info = "\nInformacoes publicas:\n\n"
    for text in info["publicas"]:
        vis_info += "- "+text+"\n"

    fonte = "Helvetica 24 bold"
    fonte_pequena = "Helvetica 16"
    fonte_texto = "Helvetica 14"
    
    janela = tk.Tk()
    janela.title("Ministerio do Meio Ambiente")
    janela["bg"] = "black"
    janela.resizable(0, 0)
    largura = 800
    altura = 600

   
    screen_width = janela.winfo_screenwidth()
    screen_height = janela.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (largura/2))
    y_cordinate = int((screen_height/2) - (altura/2))

    janela.geometry("{}x{}+{}+{}".format(largura, altura, x_cordinate, y_cordinate))

    lbl_texto = tk.Label(janela, text="Usuario logado como: ", fg="white", bg="black", font=fonte_pequena)
    lbl_texto.pack(fill=tk.X, pady=10)

    if nivel_de_acesso == 3: 
        acesso = "Ministro do Meio Ambiente"
        vis_info += "\nInformacoes Secretas: \n\n"
        for text in info["secretas"]:
            vis_info += "- "+text+"\n"

        vis_info += "\nInformacoes Ultra Secretas: \n\n"
        for text in info["ultra_secretas"]:
            vis_info += "- "+text+"\n"

    elif nivel_de_acesso == 2:
        acesso = "Diretor"

        vis_info += "\nInformacoes Secretas: \n\n"
        for text in info["secretas"]:
            vis_info += "- "+text+"\n"

    elif nivel_de_acesso == 1:
        acesso = "Publico"
        
    lbl_nivel = tk.Label(janela, text=acesso, fg="white", bg="black", font=fonte)
    lbl_nivel.pack(fill=tk.X, pady=10)

    
    lbl_info = tk.Message(janela, text=vis_info, relief=tk.RAISED, font=fonte_texto)
    lbl_info.pack()


    janela.mainloop()


def menu(nivelAcesso):
    fonte = "Helvetica 16 bold"
    fonte_pequena = "Helvetica 12"

    LOCAL_DIR = os.path.dirname(os.path.realpath(__file__))
    print(LOCAL_DIR)

    

    # ===== Acoes componentes ==================================================================

    def btnGer_Click():

        def btnDel_Click():
            
            if lb_faces.curselection():

                var = re.findall(r'\d+',lb_faces.get(lb_faces.curselection() ))
                id = list(map(int, var))         
                
                dados = selecionar(id[0])[0]
                try:
                    
                    print(id[0])
                    baixarNivel(id[0])
                except:
                    messagebox.showwarning("ERRO", "Erro ao baixar o nivel")
                
                lb_faces.delete(0, "end")
                dados = listar()
                for x in dados:
                    lb_faces.insert(0,"id = {}  nome = {}".format(x[0], x[1]))
            
            else:
                messagebox.showwarning("Atencao", "Selecione um item para poder deletar!")

                
        janela_ger = tk.Toplevel(janela_principal)
        janela_ger["bg"] = "black"
        janela_ger.resizable(0, 0)

        largura = 400
        altura = 300

        screen_width = janela_ger.winfo_screenwidth()
        screen_height = janela_ger.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (largura/2))
        y_cordinate = int((screen_height/2) - (altura/2))

        janela_ger.geometry("{}x{}+{}+{}".format(largura, altura, x_cordinate, y_cordinate))

        scrollbar = tk.Scrollbar(janela_ger, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        lb_faces = tk.Listbox(janela_ger, font=fonte_pequena, yscrollcommand = scrollbar.set)
        
        dados = listar()
        #print(dados)
        for x in dados:
            lb_faces.insert(0,"id = {}  nome = {}".format(x[0], x[1]))

        lb_faces.pack(fill=tk.X, pady=1)

        btnCad = tk.Button(janela_ger, text="Cadastrar novo", bg="green", fg="white", command=btnCad_Click, font=fonte)
        btnCad.pack(fill=tk.X, pady=2)

        btnDel = tk.Button(janela_ger, text="Deletar registro", bg="red", fg="white", command=btnDel_Click, font=fonte)
        btnDel.pack(fill=tk.X, pady=2)

    def btnInfo_Click():
        janela(nivelAcesso)

    def btnCad_Click():
        cadastro()

        


    def btnCam_Click():

        messagebox.showinfo("Importante", "Aperte (q) para desligar a camera!")
        janela_principal.destroy()
        identificar()
        
        
        
    #========= Criando janela principal =======================================================

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
    btnCam = tk.Button(janela_principal, text="Informacoes", bg="yellow", fg="black", command=btnInfo_Click, font=fonte)
    btnCam.pack(fill=tk.X, pady=20)
    
    if nivelAcesso >= 3:
        btnGer = tk.Button(janela_principal, text="Gerenciar Faces", bg="yellow", fg="black", command=btnGer_Click, font=fonte)
        btnGer.pack(fill=tk.X, pady=20)

    #Loop principal da GUI
    janela_principal.mainloop()