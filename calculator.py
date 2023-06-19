from tkinter import *

root = Tk()
root.geometry('250x270')
root.title('Калькулятор')

global abc
abc = ''

pole = Label(root, bg='black', fg = 'white', width = 12, height=3, justify = 'left', font = 'Times 20', text=abc)
pole.grid(row=0, column=0, columnspan=4)

def number0():
    global abc
    abc=abc
    pole['text']=abc
def number1():
    global abc
    abc=abc+'1'
    pole['text']=abc
def number2():
    global abc
    abc=abc+'2'
    pole['text']=abc
def number3():
    global abc
    abc=abc+'3'
    pole['text']=abc
def number4():
    global abc
    abc=abc+'4'
    pole['text']=abc
def number5():
    global abc
    abc=abc+'5'
    pole['text']=abc
def number6():
    global abc
    abc=abc+'6'
    pole['text']=abc
def number7():
    global abc
    abc=abc+'7'
    pole['text']=abc
def number8():
    global abc
    abc=abc+'8'
    pole['text']=abc
def number9():
    global abc
    abc=abc+'9'
    pole['text']=abc
def c():
    global abc
    abc = ''
    pole['text']=abc
def ravno():
    global abc
    abc=eval(abc)
    pole['text']=abc
def minus():
    global abc
    abc=abc+'-'
    pole['text']=abc
def plus():
    global abc
    abc=abc+'+'
    pole['text']=abc
def umn():
    global abc
    abc=abc+'*'
    pole['text']=abc
def dele():
    global abc
    abc=abc+'/'
    pole['text']=abc

but1 = Button(text='1',width=5,height=2,command= number1).grid(row=1,column=0)
but2 = Button(text='2',width=5,height=2,command= number2).grid(row=1,column=1)
but3 = Button(text='3',width=5,height=2,command=number3).grid(row=1,column=2)
but4 = Button(text='4',width=5,height=2,command= number4).grid(row=2,column=0)
but5 = Button(text='5',width=5,height=2,command=number5).grid(row=2,column=1)
but6 = Button(text='6',width=5,height=2,command=number6).grid(row=2,column=2)
but7 = Button(text='7',width=5,height=2,command=number7).grid(row=3,column=0)
but8 = Button(text='8',width=5,height=2,command=number8).grid(row=3,column=1)
but9 = Button(text='9',width=5,height=2,command=number9).grid(row=3,column=2)
but0 = Button(text='0',width=5,height=2, command=number0).grid(row=4,column=1)
butx = Button(text='*',width=5,height=2,command=umn).grid(row=1,column=4)
butf = Button(text='/',width=5,height=2,command=dele).grid(row=2,column=4)
butplus = Button(text='+',width=5,height=2,command=plus).grid(row=3,column=4)
butminus = Button(text='-',width=5,height=2,command=minus).grid(row=4,column=4)
butc = Button(text='c',width=5,height=2, command=c).grid(row=4,column=0)
butravno = Button(text='=',width=5,height=2, command=ravno).grid(row=4,column=2)

root.mainloop()