#!/usr/bin/env python3
from cgitb import text
from doctest import master
from re import *
from tkinter import *
import tkinter 
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import os
from Authentication import  encrypt_pwd, descrypt_pwd, escreveSenhaNova
from relay8p import config, req_control, vIP, caminho


class Aplicattion:
    
    def __init__(self, master=None):

        self.i = None
        self.master = master
        master.title("Controle Relé")
        master.resizable(False, True)
        logo = Label(master, image=img)
        logo.grid(column=1, row=0, padx=5)

        self.lista_ip = {'CAB 1': '192.168.0.66',
                    'CAB 2': '192.168.0.68',
                    'CAB 3': '192.168.0.70'
                    }
        chaves = list(self.lista_ip.keys())
        # options_list = [lista_ip['CAB 1'],lista_ip['CAB 2'],lista_ip['CAB 3']]
        options_list = [chaves[0], chaves[1], chaves[2]]

        # for k in lista_ip.keys():
        #     if k == chaves[0]:
        #         asdf = lista_ip['CAB 1']
        #     elif k == chaves[1]:
        #         asdf = lista_ip['CAB 2']
        #     elif k == chaves[2]:
        #         asdf = lista_ip['CAB 3']
        #     else:
        #         pass


        # Variable to keep track of the option
        # selected in OptionMenu
        
        
        # Set the default value of the variable
        value_inside.set("Menu de IPs")


        
        # Create the optionmenu widget and passing 
        # the options_list and value_inside to it.
        self.question_menu = tkinter.OptionMenu(root, value_inside, *options_list, command=self.mudaNome)
        self.question_menu.grid(column=0, row=0)    
        


        '''border = LabelFrame(master, bd=0, bg="black")
        border.grid(column=2, row=3, padx=5, pady=5)

        border2 = LabelFrame(master, bd=0, bg="black")
        border2.grid(column=2, row=4, padx=5, pady=5)

        border3 = LabelFrame(master, bd=0, bg="black")
        border3.grid(column=2, row=5, padx=5, pady=5)

        border4 = LabelFrame(master, bd=0, bg="black")
        border4.grid(column=2, row=6, padx=5, pady=5)

        border5 = LabelFrame(master, bd=0, bg="black")
        border5.grid(column=2, row=7, padx=5, pady=5)

        border6 = LabelFrame(master, bd=0, bg="black")
        border6.grid(column=2, row=8, padx=5, pady=5)

        border7 = LabelFrame(master, bd=0, bg="black")
        border7.grid(column=2, row=9, padx=5, pady=5)

        border8 = LabelFrame(master, bd=0, bg="black")
        border8.grid(column=2, row=9, padx=5, pady=5)'''

        border9 = LabelFrame(master, bd=0, bg="black")
        border9.grid(column=3, row=4, padx=5, pady=5)

        border10 = LabelFrame(master, bd=0, bg="black")
        border10.grid(column=3, row=5, padx=5, pady=5)

        # border11= LabelFrame(master, bd=0, bg="black")
        # border11.grid(column=3, row=6, padx=5, pady=5)

        # border12= LabelFrame(master, bd=0, bg="black")
        # border12.grid(column=3, row=7, padx=5, pady=5)

        # border13 = LabelFrame(master, bd=0, bg="black")
        # border13.grid(column=3, row=8, padx=5, pady=5)

        # border14 = LabelFrame(master, bd=0, bg="black")
        # border14.grid(column=3, row=9, padx=5, pady=5)

        # border15 = LabelFrame(master, bd=0, bg="black")
        # border15.grid(column=3, row=10, padx=5, pady=5)

        # border16 = LabelFrame(master, bd=0, bg="black")
        # border16.grid(column=3, row=11, padx=5, pady=5)

        borderU = LabelFrame(master, bd=0, bg="black")
        borderU.grid(column=3, row=3, padx=5, pady=5)


        ip = Label(master, text="IP/DNS:", width= 12, height=3)
        ip.place(x=-20, y=150)



        self.ip_entry = Entry(master,textvariable = value_inside, bd=5) #textvariable popula a ip_var
        self.ip_entry.place(x=50, y=162, width=100) 


        port = Label(master, text="Porta:", width= 10, height=3)
        port.place(x=140, y=149)

        self.port_entry = Entry(master,textvariable = port_var, bd=5) #textvariable popula a ip_var
        self.port_entry.place(x=199, y=161, width=80) 

        self.btn_envia = Button(master, text='Enviar', command= self.submit)
        self.btn_envia.grid(column=3, row=2)
        self.btn_envia.place(x=289, y=160)


        porta1 = Label(master, text="MOXA e ETR", borderwidth=2, width= 20, height=3, relief="ridge", highlightbackground="black", highlightthickness=2)
        porta1.grid(column=0, row=4, padx=0, pady=0)

        porta2 = Label(master, text="Rádio, Camera e Switch", borderwidth=2, width=20, height=3, relief="ridge",highlightbackground="black", highlightthickness=2)
        porta2.grid(column=0, row=5, padx=0, pady=0)

        # porta3 = Label(master, text="Porta 3", borderwidth=2, width=10, height=3, relief="ridge",highlightbackground="black", highlightthickness=2)
        # porta3.grid(column=0, row=6, padx=0, pady=0)

        # porta4 = Label(master, text="Porta 4", borderwidth=2, width=10, height=3, relief="ridge",highlightbackground="black", highlightthickness=2)
        # porta4.grid(column=0, row=7, padx=0, pady=0)

        # porta5 = Label(master, text="Porta 5", borderwidth=2, width=10, height=3, relief="ridge",highlightbackground="black", highlightthickness=2)
        # porta5.grid(column=0, row=8, padx=0, pady=0)

        # porta6 = Label(master, text="Porta 6", borderwidth=2, width=10, height=3, relief="ridge",highlightbackground="black", highlightthickness=2)
        # porta6.grid(column=0, row=9, padx=0, pady=0)

        # porta7 = Label(master, text="Porta 7", borderwidth=2, width=10, height=3, relief="ridge",highlightbackground="black", highlightthickness=2)
        # porta7.grid(column=0, row=10, padx=0, pady=0)

        # porta8 = Label(master, text="Porta 8", borderwidth=2, width=10, height=3, relief="ridge",highlightbackground="black", highlightthickness=2)
        # porta8.grid(column=0, row=11, padx=0, pady=0)


        self.update = Button(borderU, text="Atualizar", width=10, height=3, fg="black", command= lambda: [self.verificaOn(), self.submit()])
        self.update.grid(column=3, row=3, padx=5, pady=5)

        
        self.status1 = Label(master, text="Status1: ", borderwidth=2, width=10, height=3, relief="ridge",highlightbackground="black", highlightthickness=2)
        self.status1.grid(column=1, row=4, padx=0, pady=0)

        
        self.status2 = Label(master, text="Status2: ", borderwidth=2, width=10, height=3, relief="ridge", highlightbackground="black", highlightthickness=2)
        self.status2.grid(column=1, row=5, padx=0, pady=0)

        
        # self.status3 = Label(master, text="Status3: ", borderwidth=2, width=10, height=3, relief="ridge",highlightbackground="black", highlightthickness=2)
        # self.status3.grid(column=1, row=6, padx=0, pady=0)

        
        # self.status4 = Label(master, text="Status4: ", borderwidth=2, width=10, height=3, relief="ridge",highlightbackground="black", highlightthickness=2)
        # self.status4.grid(column=1, row=7, padx=0, pady=0)

        
        # self.status5 = Label(master, text="Status5: ", borderwidth=2, width=10, height=3, relief="ridge",highlightbackground="black", highlightthickness=2)
        # self.status5.grid(column=1, row=8, padx=0, pady=0)

        
        # self.status6 = Label(master, text="Status6: ", borderwidth=2, width=10, height=3, relief="ridge",highlightbackground="black", highlightthickness=2)
        # self.status6.grid(column=1, row=9, padx=0, pady=0)
    
        
        # self.status7 = Label(master, text="Status7: ", borderwidth=2, width=10, height=3, relief="ridge",highlightbackground="black", highlightthickness=2)
        # self.status7.grid(column=1, row=10, padx=0, pady=0)

        
        # self.status8 = Label(master, text="Status8: ", borderwidth=2, width=10, height=3, relief="ridge",highlightbackground="black", highlightthickness=2)
        # self.status8.grid(column=1, row=11, padx=0, pady=0)


        self.button9 = Button(border9, text="Pulso", width=10, height=2, fg="black", command= lambda: self.change())
        self.button9.grid(column=3, row=4, padx=5, pady=5)

        self.button10 = Button(border10, text="Pulso", width=10, height=2, fg="black",command= lambda: self.change2())
        self.button10.grid(column=3, row=5, padx=5, pady=5)

        # self.button11 = Button(border11, text="Pulso", width=10, height=2, fg="black",command= lambda: self.change3())
        # self.button11.grid(column=3, row=6, padx=5, pady=5)

        # self.button12 = Button(border12, text="Pulso", width=10, height=2, fg="black", command=lambda: self.change4())
        # self.button12.grid(column=3, row=7, padx=5, pady=5)

        # self.button13 = Button(border13, text="Pulso", width=10, height=2, fg="black", command=lambda: self.change5())
        # self.button13.grid(column=3, row=8, padx=5, pady=5)

        # self.button14= Button(border14, text="Pulso", width=10, height=2, fg="black", command=lambda: self.change6())
        # self.button14.grid(column=3, row=9, padx=5, pady=5)

        # self.button15 = Button(border15, text="Pulso", width=10, height=2, fg="black", command=lambda: self.change7())
        # self.button15.grid(column=3, row=10, padx=5, pady=5)

        # self.button16 = Button(border16, text="Pulso", width=10, height=2, fg="black", command=lambda: self.change8())
        # self.button16.grid(column=3, row=11, padx=5, pady=5)


        # lista_ip = {'CAB 1': '192.168.0.10',
        #             'CAB 2': '192.168.0.12',
        #             'CAB 3': '192.168.0.14'
        #             }

        # options_list = [lista_ip['CAB 1'],lista_ip['CAB 2'],lista_ip['CAB 3']]
  
        # # Variable to keep track of the option
        # # selected in OptionMenu
        # value_inside = tkinter.StringVar(root)
        
        # # Set the default value of the variable
        # value_inside.set("Select an Option")
        
        # # Create the optionmenu widget and passing 
        # # the options_list and value_inside to it.
        # question_menu = tkinter.OptionMenu(root, value_inside, *options_list)
        # question_menu.grid(column=0, row=0)
  


        '''' self.button1 = Button(border, text="On/Off", borderwidth=2, width=15, height=5, fg="black", command= lambda m='btn1': self.mudarTexto(m))
                self.button1.grid(column=2, row=1, padx=5, pady=5)

                self.button2 = Button(border2, text="On/Off", borderwidth=2, width=15, height=5, fg="black", command= lambda m='btn2': self.mudarTexto(m))
                self.button2.grid(column=2, row=2, padx=5, pady=5)

                self.button3 = Button(border3, text="On/Off", borderwidth=2, width=15, height=5, fg="black", command= lambda m='btn3': self.mudarTexto(m))
                self.button3.grid(column=2, row=3, padx=5, pady=5)

                self.button4 = Button(border4, text="On/Off", borderwidth=2, width=15, height=5, fg="black",command=lambda m='btn4': self.mudarTexto(m))
                self.button4.grid(column=2, row=4, padx=5, pady=5)

                self.button5 = Button(border5, text="On/Off", borderwidth=2, width=15, height=5, fg="black",command=lambda m='btn5': self.mudarTexto(m))
                self.button5.grid(column=2, row=5, padx=5, pady=5)

                self.button6 = Button(border6, text="On/Off", borderwidth=2, width=15, height=5, fg="black",command=lambda m='btn6': self.mudarTexto(m))
                self.button6.grid(column=2, row=6, padx=5, pady=5)

                self.button7 = Button(border7, text="On/Off", borderwidth=2, width=15, height=5, fg="black",command=lambda m='btn7': self.mudarTexto(m))
                self.button7.grid(column=2, row=7, padx=5, pady=5)

                self.button8 = Button(border8, text="On/Off", borderwidth=2, width=15, height=5, fg="black",command=lambda m='btn8': self.mudarTexto(m))
                self.button8.grid(column=2, row=8, padx=5, pady=5)'''''

    '''def mudarTexto(self, m):

        global on_button
        posicao = 0
        i = 0
        self.posicao = posicao 

        if m == 'btn1':
            if on_button:
                req_control(0, 0, 1)
                self.status1.config(background='green', text="Ligado")
                on_button = False
            else:
                req_control(0, 0, 0)
                self.status1.config(background='red', text="Desligado")
                on_button = True
        elif m == 'btn2':
            if on_button:
                self.status2.config(background='green', text="Ligado")
                req_control(0, 1, 1)
                on_button = False
            else:
                self.status2.config(background='red', text="Desligado")
                req_control(0, 1, 0)
                on_button = True
        elif m == 'btn3':
            if on_button:
                self.status3.config(background='green', text="Ligado", )
                req_control(0, 2, 1)
                on_button = False
            else:
                self.status3.config(background='red', text="Desligado")
                req_control(0, 2, 0)
                on_button = True
        elif m == 'btn4':
            if on_button:
                self.status4.config(background='green', text="Ligado", )
                req_control(0, 3, 1)
                on_button = False
            else:
                self.status4.config(background='red', text="Desligado")
                req_control(0, 3, 0)
                on_button = True
        elif m == 'btn5':
            if on_button:
                self.status5.config(background='green', text="Ligado", )
                req_control(0, 4, 1)
                on_button = False
            else:
                self.status5.config(background='red', text="Desligado")
                req_control(0, 4, 0)
                on_button = True
        elif m == 'btn6':
            if on_button:
                self.status6.config(background='green', text="Ligado", )
                req_control(0, 5, 1)
                on_button = False
            else:
                self.status6.config(background='red', text="Desligado")
                req_control(0, 5, 0)
                on_button = True
        elif m == 'btn7':
            if on_button:
                self.status7.config(background='green', text="Ligado", )
                req_control(0, 6, 1)
                on_button = False
            else:
                self.status7.config(background='red', text="Desligado")
                req_control(0, 6, 0)
                on_button = True
        elif m == 'btn8':
            if on_button:
                self.status8.config(background='green', text="Ligado", )
                req_control(0, 7, 1)
                on_button = False
            else:
                self.status8.config(background='red', text="Desligado")
                req_control(0, 7, 0)
                on_button = True
        else:
            pass'''
    def mudaNome(self, choice):
        choice= value_inside.get()
        if choice == "CAB 1":
            value_inside.set(self.lista_ip["CAB 1"])
        elif choice == "CAB 2":
            value_inside.set(self.lista_ip["CAB 2"])
        else:
            value_inside.set(self.lista_ip["CAB 3"])

    def submit(self):
        ips = ip_var.get()
        ports = port_var.get()
        listaIp = []
        listaIp.append(ips)
        print(listaIp)
        

        if ips and ports: 
            # vIP(ips, ports)
            dic = vIP(ips, ports)
            # print(dic)
            lista = []
            if not lista:            
                for j in dic.values():
                    lista.append(int(j))
                lista.remove(0)
                if len(lista) == 3: 
                    lista.remove(2)
                    self.status01 = lista[0]
                    self.status02 = lista[1]
                    self.status03 = 0
                    self.status04 = 0
                    self.status05 = 0
                    self.status06 = 0
                    self.status07 = 0
                    self.status08 = 0


                elif len(lista) == 9:
                    lista.remove(8)
                    self.status01 = lista[0]
                    self.status02 = lista[1]
                    self.status03 = lista[2]
                    self.status04 = lista[3]
                    self.status05 = lista[4]
                    self.status06 = lista[5]
                    self.status07 = lista[6]
                    self.status08 = lista[7]
                self.lista = lista
            else:
                self.lista = []
                for j in dic.values():
                    lista.append(int(j))
                lista.remove(0)
                if len(lista) == 3:
                    lista.remove(2)
                    self.status01 = lista[0]
                    self.status02 = lista[1]
                    self.status03 = 0
                    self.status04 = 0
                    self.status05 = 0
                    self.status06 = 0
                    self.status07 = 0
                    self.status08 = 0
                elif len(lista) == 9:
                    lista.remove(8)
                    self.status01 = lista[0]
                    self.status02 = lista[1]
                    self.status03 = lista[2]
                    self.status04 = lista[3]
                    self.status05 = lista[4]
                    self.status06 = lista[5]
                    self.status07 = lista[6]
                    self.status08 = lista[7]
                self.lista = lista
            print(self.verificaOn())
        else:
            messagebox.showinfo(title="Campos em Branco!", message='Preencha os campos!')


    def change(self):
        req_control(1, 0, 1)
        self.status1.configure(bg='red', text='Desligado')
        self.status1.after(5000, self.change_back)

    def change2(self):
        req_control(1, 1, 1)
        self.status2.configure(bg='red', text='Desligado')
        self.status2.after(5000, self.change_back2)

    # def change3(self):
    #     if len(self.lista) == 8:
    #         req_control(1, 2, 0)
    #         self.status3.configure(bg='red', text='Desligado')
    #         self.status3.after(5000, self.change_back3)
    #     else:
    #         self.status3.configure(bg='red', text='Desligado')
    #         self.status3.after(5000, self.change_back3)
    # def change4(self):
    #     req_control(1, 3, 0)
    #     self.status4.configure(bg='red', text='Desligado')
    #     self.status4.after(5000, self.change_back4)

    # def change5(self):
    #     req_control(1, 4, 0)
    #     self.status5.configure(bg='red', text='Desligado')
    #     self.status5.after(5000, self.change_back5)

    # def change6(self):
    #     req_control(1, 5, 0)
    #     self.status6.configure(bg='red', text='Desligado')
    #     self.status6.after(5000, self.change_back6)

    # def change7(self):
    #     req_control(1, 6, 0)
    #     self.status7.configure(bg='red', text='Desligado')
    #     self.status7.after(5000, self.change_back7)

    # def change8(self):
    #     req_control(1, 7, 0)
    #     self.status8.configure(bg='red', text='Desligado')
    #     self.status8.after(5000, self.change_back8)

    def change_back(self):
        self.status1.configure(bg='green', text='Ligado')
    def change_back2(self):
        self.status2.configure(bg='green', text='Ligado')
    # def change_back3(self):
    #     self.status3.configure(bg='green', text='Ligado')
    # def change_back4(self):
    #     self.status4.configure(bg='green', text='Ligado')
    # def change_back5(self):
    #     self.status5.configure(bg='green', text='Ligado')
    # def change_back6(self):
    #     self.status6.configure(bg='green', text='Ligado')
    # def change_back7(self):
    #     self.status7.configure(bg='green', text='Ligado')
    # def change_back8(self):
    #     self.status8.configure(bg='green', text='Ligado')

    def verificaOn(self):
        ips = ip_var.get()
        ports = port_var.get()
        if ips and ports:
            lista = self.lista
            cont = 0
            valores = [self.status01, self.status02, self.status03, self.status04, self.status05, self.status06, self.status07, self.status08]
            # print(lista)
            # print(valores)
            if len(lista) == 8:
                self.limpastatus()
                for l in lista:
                    if l == valores[cont]:
                        self.mudaStatus()
                        cont+=1
                    else:
                        self.mudaStatus()
                        cont+=1 
            else:
                i = 0
                while i < 8:
                    self.mudaStatus()
                    i += 1
            var2 = vIP(ips, ports)
        else:
            messagebox.showinfo(title="Campos em Branco!", message='Preencha os campos!')
        return var2


    def limpastatus(self):
        self.status1['text'] = 'Status1: '
        self.status2['text'] = 'Status2: '
        # self.status3['text'] = 'Status3: '
        # self.status4['text'] = 'Status4: '
        # self.status5['text'] = 'Status5: '
        # self.status6['text'] = 'Status6: '
        # self.status7['text'] = 'Status7: '
        # self.status8['text'] = 'Status8: '

    def mudaStatus(self):
        if self.status1['text'] == 'Status1: ':
            if self.status01 == 1:
                self.status1.configure(bg='green', text='Ligado')
            else:
                self.status1.configure(bg='red', text='Desligado')

        elif self.status2['text'] == 'Status2: ':
            if self.status02 == 1:
                self.status2.configure(bg='green', text='Ligado')
            else:
                self.status2.configure(bg='red', text='Desligado')

        # elif self.status3['text'] == 'Status3: ':
        #     if self.status03 == 1:
        #         self.status3.configure(bg='green', text='Ligado')
        #     else:
        #         self.status3.configure(bg='red', text='Desligado')

        # elif self.status4['text'] == 'Status4: ':
        #     if self.status04 == 1:
        #         self.status4.configure(bg='green', text='Ligado')
        #     else:
        #         self.status4.configure(bg='red', text='Desligado')

        # elif self.status5['text'] == 'Status5: ':
        #     if self.status05 == 1:
        #         self.status5.configure(bg='green', text='Ligado')
        #     else:
        #         self.status5.configure(bg='red', text='Desligado')

        # elif self.status6['text'] == 'Status6: ':
        #     if self.status06 == 1:
        #         self.status6.configure(bg='green', text='Ligado')
        #     else:
        #         self.status6.configure(bg='red', text='Desligado')

        # elif self.status7['text'] == 'Status7: ':
        #     if self.status07 == 1:
        #         self.status7.configure(bg='green', text='Ligado')
        #     else:
        #         self.status7.configure(bg='red', text='Desligado')

        # elif self.status8['text'] == 'Status8: ':
        #     if self.status08 == 1:
        #         self.status8.configure(bg='green', text='Ligado')
        #     else:
        #         self.status8.configure(bg='red', text='Desligado')
class fdp:
    
    def __init__(self, master=None):

        master.resizable(False, False)
        senha = ''
        self.senha = senha
        
        l_u = Label(master, text="Usuário:", width= 10, height=3)
        l_u.grid(column=2, row=1)

        self.ip_entry = Entry(master,textvariable = User, bd=5) #textvariable popula a ip_var
        self.ip_entry.grid(column=3, row=1) 

        l_psw = Label(master, text="Senha:", width= 10, height=3)
        l_psw.grid(column=2, row=2)

        self.pwd = Entry(master,textvariable = passw, show='*', bd=5) #textvariable popula a ip_var
        self.pwd.grid(column=3, row=2) 

        n_pw = Label(master, text="Nova Senha:", width= 12, height=3)
        n_pw.grid(column=2, row=5)

        self.n_pwd = Entry(master,textvariable = entryNovaSenha, show='*', bd=5) #textvariable popula a ip_var
        self.n_pwd.grid(column=3, row=5) 

        c_pw = Label(master, text="Senha Atual:", width= 15, height=3)
        c_pw.grid(column=2, row=4)

        self.c_pwd = Entry(master,textvariable = entrySenhaAtual, show='*', bd=5) #textvariable popula a ip_var
        self.c_pwd.grid(column=3, row=4) 

        self.btn_envia = Button(master, text='Submit', command= self.login)
        self.btn_envia.grid(column=3, row=3)  

        self.btn_mudaSenha = Button(master, text='Submit', command= self.mudaSenha)
        self.btn_mudaSenha.grid(column=3, row=6)        


        
    def login(self):        
        entryUser = User.get()
        self.pword = passw.get()        
        global asd
        self.criaConfig()
        entryPwdDecry = descrypt_pwd()

        if (entryUser == '' and entryPwdDecry == ''):
            messagebox.showinfo(title='ERRO!',message='Campo em branco!')

        elif (entryUser == 'admin' and self.pword == entryPwdDecry):
            messagebox.showinfo(title='',message='Sucesso!')
            asd = 1
            rato.destroy()
        else:
            messagebox.showinfo(title='ERRO!',message='Login Inválido!')


    def mudaSenha(self):
       self.entryPwdAtual = entrySenhaAtual.get()
       self.newPwd = entryNovaSenha.get()
       self.verificaConfig()
       self.n_pwd.delete(0, 'end')
       self.c_pwd.delete(0, 'end')

    def verificaConfig(self):
        pathPublic =  caminho('keys\public.pem')
        pathPriv = caminho('keys\private.pem')
        pathConfig = caminho('config\config.txt')

        if os.path.exists(pathConfig) and os.path.exists(pathPriv) and os.path.exists(pathPublic):
            atualEncry = encrypt_pwd(self.entryPwdAtual.encode())
            lista = []
            for i in atualEncry:
                lista.append(i)          
        
            with open(pathConfig, 'rb') as file2:
                atualPwd = file2.read()
                if atualPwd == lista[0]:
                    self.mudaConfig()
            
        else:
            messagebox.showinfo(title="ERRO!", message='Senhas ainda não cadastradas!!!')

    def mudaConfig(self):
        novaSenha = self.newPwd
        escreveSenhaNova(novaSenha)
        messagebox.showinfo(title="Sucesso!", message='Senha alterada com sucesso!!') 

    def criaConfig(self):
        senha = passw.get().encode()   
        encrypt_pwd(senha)
        

   
    
    
     

asd = 0
# listC = []
# configs = config()
# for i in configs:
#     listC.append(i)
config()

try:
    rato = Tk()
    User = StringVar()
    passw = StringVar()
    entryNovaSenha = StringVar()
    entrySenhaAtual = StringVar()
    rato.title('Login')
    rato.geometry('330x300')
    fdp(rato)
    rato.mainloop()
finally:
    if asd == 1:
        root = Tk()
        value_inside = tkinter.StringVar()                
        ip_var = tkinter.StringVar()
        value_inside = ip_var       
        port_var = tkinter.StringVar()
        img = ImageTk.PhotoImage(Image.open(caminho('logo\preto_CMYK.png')).resize((249,113)))
        Aplicattion(root)
        root.mainloop()
    else:
        pass