from tkinter import *
from tkinter import Tk, ttk

# importando pillow

from PIL import Image, ImageTk 

# cores
co0 = "#2e2d2b" # Preta
co1 = "#feffff" # Branca
co2 = "#4fa882" # Verde
co3 = "#38576b" # Valor
co4 = "#403d3d" # Letra
co5 = "#e06636" # - profit
co6 = "#038cfc" # Azul
co7 = "#3fbfb9" # Verde
co8 = "#263238" #  + Verde
co9 = "#e9edf5" #  + Verde
co10 = "#6e8faf" 
co11 = "#f2f4f2"

# Criando Janela

janela = Tk()
janela.title("")
janela.geometry('250x400')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

Style = ttk.Style(janela)
Style.theme_use('clam')

# frames

FrameCima = Frame(janela, width=300, height=50, bg=co1, relief="flat")
FrameCima.grid(row=0, column=0)
FrameMeio = Frame(janela, width=300, height=90, bg=co1, relief="flat")
FrameMeio.grid(row=1, column=0)
FrameBaixo = Frame(janela, width=300, height=290, bg=co9, relief="flat")
FrameBaixo.grid(row=2, column=0)


# LOGO ------------------------------------------

app_=Label(FrameCima, text='Orçamento',compound=LEFT, padx=5,relief=FLAT, anchor=NW, font=('Verdana 20'), bg=co1,fg=co4)
app_.place(x=0, y=0)

# Abrindo Imagem

app_img = Image.open('123 copy.png')
app_img = app_img.resize((40,40))
app_img = ImageTk.PhotoImage(app_img)

app_logo=Label(FrameCima,image=app_img,compound=LEFT, padx=5,relief=FLAT, anchor=NW, font=('Verdana 20'), bg=co1,fg=co4)
app_logo.place(x=160, y=0)

app_linha=Label(FrameCima,width=295,relief=FLAT, anchor=NW, font=('Verdana 1'), bg=co3,fg=co1)
app_linha.place(x=0, y=47)

# Funçao calcular.

def calcular():
 
    # Obtendo o valor total.

 renda_mensal = float(e_valor.get())

# Obtendo as percentual /40% - /30% - /30%

 obterpercentual_40 = (40/100) * renda_mensal
 obterpercentual_30 = (30/100) * renda_mensal 
 obterpercentual_30 = (30/100) * renda_mensal 

 total_necessidades  ['text']  = (f' R$ {obterpercentual_40}') 
 total_Gastos        ['text']  = (f' R$ {obterpercentual_30}') 
 total_Investimentos ['text']  = (f' R$ {obterpercentual_30}') 


# frame meio 

app_=Label(FrameMeio, text=' Entrando com sua Renda Mensal' ,relief=FLAT, anchor=NW, font=('ivy 10'), bg=co1,fg=co4) 
app_.place(x=7, y=15)
 

e_valor = Entry(FrameMeio,width=10, font=('Ivy 14'), justify='center',relief='solid')
e_valor.place(x=10, y =40)

botao_calcular= Button(FrameMeio, command=calcular,  text=' Calcular'.upper() ,relief=RIDGE, anchor=NW, font=('ivy 9'), bg=co1,fg=co0) 
botao_calcular.place(x=150, y=40)

# frame Baixo

app_=Label(FrameBaixo, text= '  Seus numeros de 40% 30% 30%' ,relief=FLAT, width=35, anchor=NW, font=('verdana 10'), bg=co3,fg=co1) 
app_.place(x=0, y=0)

# Necessidades

total_necessidades=Label(FrameBaixo, text= '  Necessidades' ,relief=FLAT, width=35, anchor=NW, font=('verdana 10'), bg=co9,fg=co0) 
total_necessidades.place(x=10, y=40)


total_necessidades=Label(FrameBaixo,relief=FLAT, width=22, anchor=NW, font=('verdana 12'), bg=co1,fg=co4) 
total_necessidades.place(x=10, y=75)


# Gastos

total_Gastos=Label(FrameBaixo, text= '  Gastos' ,relief=FLAT, width=35, anchor=NW, font=('verdana 10'), bg=co9,fg=co0) 
total_Gastos.place(x=10, y=115)


total_Gastos=Label(FrameBaixo,relief=FLAT, width=22, anchor=NW, font=('verdana 12'), bg=co1,fg=co4) 
total_Gastos.place(x=10, y=140)

# Investimentos

total_Investimentos=Label(FrameBaixo, text= '  Investimentos' ,relief=FLAT, width=35, anchor=NW, font=('verdana 10'), bg=co9,fg=co0) 
total_Investimentos.place(x=10, y=185)


total_Investimentos=Label(FrameBaixo,relief=FLAT, width=22, anchor=NW, font=('verdana 12'), bg=co1,fg=co4) 
total_Investimentos.place(x=10, y=215)



janela.mainloop()
