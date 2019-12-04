import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
from gerenciador_db import *
import os
import shutil
import cv2
import face_recognition
from datetime import datetime

fonte = "Helvetica 16 bold"
fonte_pequena = "Helvetica 12"
LOCAL_DIR = os.path.dirname(os.path.realpath(__file__))

foto = []
def cadastro():
    
    def btnFoto_Click():


        messagebox.showinfo("Cadastro", "Aperte (F) para tirar a foto")

        cap = cv2.VideoCapture(0)

        while(True):

            if cv2.waitKey(20) & 0xFF == ord('f'):
                result = tk.messagebox.askquestion ('Fotografia','Salvar essa imagem?',icon = 'warning')
                if result == 'yes':
                    
                    global foto 
                    foto = frame
                    
                    break
                else:
                    continue

            ret, frame = cap.read()
            local_das_faces = face_recognition.face_locations(frame)
            
            if(len(local_das_faces) > 0):
                local_das_faces = local_das_faces[0]
                cor = (0, 255, 0)
                traco = 2
                cv2.rectangle(frame, (local_das_faces[3],local_das_faces[0]), (local_das_faces[1], local_das_faces[2]), cor, traco)

            cv2.imshow("Camera", frame)
    
           
                
         
        cv2.destroyAllWindows()
        cap.release() 



    def btnSalvar_Click():

        nome = txt_nome.get()
        
        if(nome != "" and len(foto) > 0 and lb_nivel.curselection() ):

            nivel = lb_nivel.curselection()[0] + 1
            imgname = "".join(e for e in str(datetime.now()) if e.isalnum())
            if adicionar(nome, "/img/cadastrados/{}.jpg".format(imgname), nivel):

                cv2.imwrite(LOCAL_DIR+"/img/cadastrados/{}.jpg".format(imgname), foto)

                messagebox.showinfo("Cadastro", "Novo usuario cadastrado com sucesso")
                
                janela_cadastro.destroy()
        else:

            messagebox.showwarning("ATENCAO", "Preencha o formulario de cadastro antes de salvar!")


    #Criando janela cadastro
    janela_cadastro = tk.Tk()
    janela_cadastro["bg"] = "black"
    janela_cadastro.resizable(0, 0)

    largura = 400
    altura = 500

    screen_width = janela_cadastro.winfo_screenwidth()
    screen_height = janela_cadastro.winfo_screenheight()

    x_cordinate = int((screen_width/2) - (largura/2))
    y_cordinate = int((screen_height/2) - (altura/2))

    janela_cadastro.geometry("{}x{}+{}+{}".format(largura, altura, x_cordinate, y_cordinate))

    #Componentes janela de cadastro

    lbl_img = tk.Label(janela_cadastro, text="Foto: ", fg="yellow", bg="black",font=fonte )
    lbl_img.pack(fill=tk.X, pady=1)

    btnFoto = tk.Button(janela_cadastro, text="Tirar fotografia", bg="yellow", fg="black", command=btnFoto_Click, font=fonte)
    btnFoto.pack(fill=tk.X, pady=1)

    lbl_nome = tk.Label(janela_cadastro, text="Nome: ", fg="yellow", bg="black", font=fonte)
    lbl_nome.pack(fill=tk.X, pady=10)

    txt_nome = tk.Entry(janela_cadastro, font=fonte_pequena)
    txt_nome.pack(fill=tk.X, pady=1)

    lbl_nivel = tk.Label(janela_cadastro, text="Nivel de acesso: ", fg="yellow", bg="black", font=fonte)
    lbl_nivel.pack(fill=tk.X, pady=10)

    lb_nivel = tk.Listbox(janela_cadastro, font=fonte_pequena)

    lb_nivel.insert(0,"Nivel Ministro")
    lb_nivel.insert(0,"Nivel Diretor")
    lb_nivel.insert(0,"Nivel Publico")

    lb_nivel.pack(fill=tk.X)

    btnSalvar = tk.Button(janela_cadastro, text="Salvar", bg="yellow", fg="black", command=btnSalvar_Click, font=fonte)
    btnSalvar.pack(fill=tk.X, pady=10)

    janela_cadastro.mainloop()

