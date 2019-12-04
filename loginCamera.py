import face_recognition
import os
from PIL import Image, ImageDraw
import cv2
import tkinter as tk
from gerenciador_db import *
from menu import *
from datetime import datetime

def identificar():

    LOCAL_DIR = os.path.dirname(os.path.realpath(__file__))

    registros = listar()
    print(registros)

    #Gerando encodings

    face_encoding_conhecidos = []
    nomes_conhecidos = []
    nivel = []
    nomeLog = "Desconhecido"

    for face in registros:

        nova_face = face_recognition.load_image_file(LOCAL_DIR+face[2])
        nova_face_encoding = face_recognition.face_encodings(nova_face)[0]

        face_encoding_conhecidos.append(nova_face_encoding)
        nomes_conhecidos.append(face[1])
        nivel.append(face[3])


    #liga camera
    cap = cv2.VideoCapture(0)
    count = 0
    nivel_de_acesso = -1

    while(True):

        if nivel_de_acesso > -1:
            break
            
        ret, frame = cap.read()
        nivel_acesso = 0
        imagem_desconhecido = frame
        #imagem_desconhecido = face_recognition.load_image_file(frame_image)
        local_das_faces = face_recognition.face_locations(imagem_desconhecido)

        imagem_desconhecido_encoding = face_recognition.face_encodings(imagem_desconhecido, local_das_faces)

        for(top, right, bottom, left), face_encoding in zip(local_das_faces, imagem_desconhecido_encoding):

            encontrados = face_recognition.compare_faces(face_encoding_conhecidos, face_encoding, tolerance= 0.55)

            nome = "Desconhecido"

            if True in encontrados:

                first_math_index = encontrados.index(True)
                nome = nomes_conhecidos[first_math_index]
                print(nivel[first_math_index]) #Testar nivel de acesso face

                if  nome != "Desconhecido":
                    print("O contador foi incrementado")
                    
                    count += 1
                else:
                    print("O contador foi zerado")
                    count = 0
                
                if count >= 5:
                    nomeLog = nome
                    nivel_de_acesso = nivel[first_math_index]
                    break
    
            print(count)

            font = cv2.FONT_HERSHEY_SIMPLEX
            color = (255,255,255)
            stroke = 1
            cv2.putText(frame, nome, (left,top - 5), font, 0.7, color, stroke, cv2.LINE_AA)

            cor = (255, 0, 0)
            traco = 2
        
            cv2.rectangle(frame, (right,top), (left, bottom), cor, traco)

            

        cv2.imshow("Camera", frame)
    
        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
         
    cv2.destroyAllWindows()
    cap.release() 


    if nivel_de_acesso > 0:
        menu(nivel_de_acesso)
        f=open("log.txt", "a+")  
        f.write("\nTentativa de login efetuada por:[ {} ] resultado:[ {} ] data:[ {} ]".format(nomeLog, "Acesso autorizado", datetime.now()))
        f.close()

    else:
        f=open("log.txt", "a+")  
        f.write("\nTentativa de login efetuada por:[ {} ] resultado:[ {} ] data:[ {} ]".format(nomeLog, "Acesso NEGADO", datetime.now()))
        f.close()
        messagebox.showwarning("Atencao", "Acesso NEGADO!")
        exit()