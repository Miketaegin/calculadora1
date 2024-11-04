#calculadora lista.append(numero1+float(salvarnumero))
import tkinter as tk
from tkinter import *
tela = tk.Tk()
tela.title("Calculadora")
tela.geometry("500x600")
tela.resizable(width=False,height=False)
tela.config(bg="#7FFFD4")
valor = Entry(tela,width=50)
valor.place(x=100,y=25)
lista = []
Developer = Label(tela,text='Desenvolvido por Miguel Farias',bg='#000000',fg= '#008B8B',font=('Arial black', 10))
Developer.place(x=50,y=450)
def btnumero(numero):
    salvarnumero= valor.get()
    valor.delete(0,END)
    valor.insert(0,str(salvarnumero)+str(numero))
    return
def limparCalculadora():
    valor.delete(0,END)
def soma():
    salvarnumero= valor.get()
    global numero1
    global operação
    numero1=float(salvarnumero)
    operação='Soma'
    valor.delete(0,END)
    return 
def sub():
    salvarnumero= valor.get()
    global numero1
    global operação
    numero1=float(salvarnumero)
    operação='Subtração'
    valor.delete(0,END)
    return
def mult():
    salvarnumero= valor.get()
    global numero1
    global operação
    numero1=float(salvarnumero)
    operação='Multiplicação'
    valor.delete(0,END)
    return
def div():
    salvarnumero= valor.get()
    global numero1
    global operação
    numero1=float(salvarnumero)
    operação='Divisão'
    valor.delete(0,END)
    return
def ponten():
    salvarnumero= valor.get()
    global numero1
    global operação
    numero1=float(salvarnumero)
    operação='Potenciação'
    valor.delete(0,END)
    return
def porc():
    salvarnumero= valor.get()
    global numero1
    global operação
    numero1=float(salvarnumero)
    operação='Porcentagem'
    valor.delete(0,END)
    return
def raiz():
    salvarnumero= valor.get()
    global numero1
    global operação
    numero1=float(salvarnumero)
    operação='Raiz'
    valor.delete(0,END)
    return
def igual():
    salvarnumero=valor.get()
    valor.delete(0,END)
    if operação=='Soma':
         valor.insert(0, numero1+float(salvarnumero))
         lista.append(numero1+float(salvarnumero))
         resultado=Label(tela,text=lista)
         resultado.place(x=150,y=500)
    elif operação=='Subtração':
          valor.insert(0, numero1-float(salvarnumero))
          lista.append(numero1+float(salvarnumero))
          resultado=Label(tela,text=lista)
          resultado.place(x=150,y=500)
    elif operação=='Multiplicação':
          valor.insert(0, numero1*float(salvarnumero))
          lista.append(numero1+float(salvarnumero))
          resultado=Label(tela,text=lista)
          resultado.place(x=150,y=500)
    elif operação=='Divisão':
         valor.insert(0, numero1/float(salvarnumero))
         lista.append(numero1+float(salvarnumero))
         resultado=Label(tela,text=lista)
         resultado.place(x=150,y=500)
    elif operação=='Pontenciação':
         valor.insert(0, numero1**float(salvarnumero))
         lista.append(numero1+float(salvarnumero))
         resultado=Label(tela,text=lista)
         resultado.place(x=150,y=500)
    elif  operação== 'Porcentagem':
         valor.insert(0,(numero1*float(salvarnumero))/100)
         lista.append(numero1+float(salvarnumero))
         resultado=Label(tela,text=lista)
         resultado.place(x=150,y=500)
    elif operação== 'Raiz':
          valor.insert(0,numero1**(1/2)(salvarnumero))
          lista.append(numero1+float(salvarnumero))
          resultado=Label(tela,text=lista)
          resultado.place(x=150,y=500)
    return
bt1 = Button(tela, text='1', relief=FLAT, width=10, height=3, command=lambda: btnumero(1))
bt1.place(x=50, y=140)
bt2 = Button(tela, text='2', relief=FLAT, width=10, height=3, command=lambda: btnumero(2))
bt2.place(x=150, y=140)
bt3 = Button(tela, text='3', relief=FLAT, width=10, height=3, command=lambda: btnumero(3))
bt3.place(x=250, y=140)
bt4 = Button(tela, text='4', relief=FLAT, width=10, height=3, command=lambda: btnumero(4))
bt4.place(x=50, y=200)
bt5 = Button(tela, text='5', relief=FLAT, width=10, height=3, command=lambda: btnumero(5))
bt5.place(x=150, y=200)
bt6 = Button(tela, text='6', relief=FLAT, width=10, height=3, command=lambda: btnumero(6))
bt6.place(x=250, y=200)
bt7 = Button(tela, text='7', relief=FLAT, width=10, height=3, command=lambda: btnumero(7))
bt7.place(x=50, y=260)
bt8 = Button(tela, text='8', relief=FLAT, width=10, height=3, command=lambda: btnumero(8))
bt8.place(x=150, y=260)
bt9 = Button(tela, text='9', relief=FLAT, width=10, height=3, command=lambda: btnumero(9))
bt9.place(x=250, y=260)
bt0 = Button(tela, text='0', relief=FLAT, width=10, height=3, command=lambda: btnumero(0))
bt0.place(x=150, y=320)
btponto = Button(tela,text='.',relief= FLAT, width=10, height=3, command=lambda:btnumero('.'))
btponto.place(x=50,y=320)
btigual = Button(tela,text='=', relief=FLAT, width=10, height=3, command=lambda: igual())
btigual.place(x=250,y=320)
btdiv = Button(tela,text='÷', relief=FLAT, width=10,height=3, command=lambda: div())
btdiv.place(x=340,y=140)
btmult = Button(tela,text='x', relief=FLAT, width=10, height=3, command=lambda: mult())
btmult.place(x=340, y=200)
btsub = Button(tela,text='-', relief=FLAT, width=10,height=3, command=lambda: sub())
btsub.place(x=340, y= 260)
btsoma = Button(tela,text='+', relief=FLAT, width=10,height=3, command=lambda: soma())
btsoma.place(x=340, y= 320)
btC = Button(tela,text='C', relief= FLAT, width= 10, height=3, command=lambda:limparCalculadora())
btC.place(x=50, y= 75)
btporcen = Button(tela,text='%', relief= FLAT, width=10, height=3, command=lambda: porc())
btporcen.place(x=150,y=75)
btpoten = Button(tela,text='X²', relief= FLAT, width=10, height=3, command=lambda: ponten())
btpoten.place(x=250,y=75)
btraiz = Button (tela,text='√x', relief= FLAT, width=10, height=3, command=lambda: raiz())
btraiz.place(x=340,y=75)
tela.mainloop()