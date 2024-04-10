# importando tkinter
from tkinter import *
from tkinter import ttk

# cores

cor1 = '#282229' # black
cor2 = '#ffffff' # white
cor3 = '#3f43bf' # dark blue
cor4 = '#363636' # grey
cor5 = '#f5a327' # orange
cor6 = '#a1a1a1' # light grey



# frames
janela =Tk()
janela.title('Calculator')
janela.geometry('273x368')
janela.config(bg=cor1)

frame_display = Frame(janela, width=273, height=50, bg=cor4)
frame_display.grid(row=0, column=0)

frame_corpo = Frame(janela, width=273, height=338)
frame_corpo.grid(row=1, column=0)


# variavel todos valores

todos_valores = ''

# label
valor_texto = StringVar()

# funcoes
def entrar_valores(event):
    
    global todos_valores

    todos_valores = todos_valores + str(event) 
    
    
    # passando valor para o display
    valor_texto.set(todos_valores)

# funcao para calcular

def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    
    valor_texto.set(str(resultado))


# funcao limpar display

def limpar_display():
    global todos_valores
    todos_valores =''
    valor_texto.set('')





app_label = Label(frame_display, textvariable=valor_texto, width=26, height=2, padx=7, relief=FLAT, anchor='e', justify=RIGHT, font=('Ivy 13'), bg=cor3, fg=cor2)
app_label.place(x=0,y=0)


# botoes

b_1 = Button(frame_corpo, command=limpar_display, text='C', width=12, height=2, bg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=3, y=0)
b_2 = Button(frame_corpo, command = lambda: entrar_valores('%'), text='%', width=4, height=2, bg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=137, y=0)
b_3 = Button(frame_corpo, command = lambda: entrar_valores('/'), text='/', width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=202, y=0)

b_4 = Button(frame_corpo, command = lambda: entrar_valores('7'), text='7', width=4, height=2, bg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=3, y=63)
b_5 = Button(frame_corpo, command = lambda: entrar_valores('8'), text='8', width=4, height=2, bg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=70, y=63)
b_6 = Button(frame_corpo, command = lambda: entrar_valores('9'), text='9', width=4, height=2, bg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=137, y=63)

b_7 = Button(frame_corpo, command = lambda: entrar_valores('*'), text='*', width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=202, y=63)

b_8 = Button(frame_corpo, command = lambda: entrar_valores('4'), text='4', width=4, height=2, bg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=3, y=126)
b_9 = Button(frame_corpo, command = lambda: entrar_valores('5'), text='5', width=4, height=2, bg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=70, y=126)
b_10 = Button(frame_corpo, command = lambda: entrar_valores('6'), text='6', width=4, height=2, bg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=137, y=126)

b_11 = Button(frame_corpo, command = lambda: entrar_valores('-'), text='-', width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=202, y=126)

b_12 = Button(frame_corpo, command = lambda: entrar_valores('1'), text='1', width=4, height=2, bg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=3, y=189)
b_13 = Button(frame_corpo, command = lambda: entrar_valores('2'), text='2', width=4, height=2, bg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=70, y=189)
b_14 = Button(frame_corpo, command = lambda: entrar_valores('3'), text='3', width=4, height=2, bg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=137, y=189)

b_15 = Button(frame_corpo, command = lambda: entrar_valores('+'), text='+', width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=202, y=189)

b_16 = Button(frame_corpo, command = lambda: entrar_valores('0'), text='0', width=12, height=2, bg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=3, y=252)
b_17 = Button(frame_corpo, command = lambda: entrar_valores('.'), text='.', width=4, height=2, bg=cor6, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=137, y=252)
b_18 = Button(frame_corpo, command = calcular, text='=', width=4, height=2, bg=cor5, fg=cor2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=202, y=252)



janela.mainloop()

