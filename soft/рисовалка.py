from tkinter import *
from turtle import *
root = Tk()
root.geometry("200x250")
root.title('Paint!')
window = Screen()
i = 10
def o():
    global j
    j += 10
    print("поворот на :",j,"градусов!")
def t():
    global j
    j -= 10
    print("поворот на :",j,"градусов")
# выход
def exit():
    window.bye()
    root.destroy()
# очистка
def clear():
    clearscreen()
# поднять перо
def up():
    penup()
    # goto(100,100)
# опустить  перо
def down():
    pendown()
    # goto(100,100)
def key_pressed(event):
    # print(f"Нажата клавиша: {event.char}")
    if event.char == "w":
        e.delete(0, END)
        e1.delete(0, END)
        forward(5)
    elif event.char == "d":
        e.delete(0, END)
        e1.delete(0, END)
        right(i)
        o()
    elif event.char == "a":
        e.delete(0,END)
        e1.delete(0, END)
        left(i)
        t()
    elif event.char == "q":
        e.delete(0, END)
        e1.delete(0, END)
        left(90)
        e2.delete(0, END)
        e2.insert(0, '90')
    elif event.char == "e":
        e.delete(0, END)
        e1.delete(0, END)
        right(90)
        e2.delete(0, END)
        e2.insert(0, '-90')
# color
def color():
    if e.get() == "красный":
        pencolor('green')
    elif e.get() == "синий":
        pencolor('blue')
    elif e.get() == "зелёный":
        pencolor('green')
    elif e.get() == "жёлтый":
        pencolor('yellow')
    else:
        pencolor('black')
# size
def size():
    if e1.get() == "10":
        pensize(10)
    elif e1.get() == "20":
        pensize(20)
    elif e1.get() == "30":
        pensize(30)
    elif e1.get() == "40":
        pensize(40)
    elif e1.get() == "50":
        pensize(50)
    elif e1.get() == "60":
        pensize(60)
    elif e1.get() == "70":
        pensize(70)
    elif e1.get() == "80":
        pensize(80)
    elif e1.get() == "90":
        pensize(90)
    elif e1.get() == "100":
        pensize(100)
    else:
        pensize(0)
def rub():
    undo()
root.bind("<Key>", key_pressed)  # Обработка всех нажатий клавиш
Button(root,text="Очистка!",command=clear).place(x=40,y=222)
Button(root,text="ластик",command=rub).place(x=120,y=222)
Button(root,text="Exit!",command=exit).pack(ipady=10,ipadx=100)
Button(root,text="поднять",command=up).place(x=0,y=50)
Button(root,text="опустить",command=down).place(x=140,y=50)
Label(root,text='Цвет: ').place(x=80,y=70)
Button(root,text="цвет!",command=color).place(x=160,y=98)
e = Entry()
e.place(x=35,y=100)
Label(root,text='размер шрифта: ').place(x=50,y=120)
Button(root,text="size!",command=size).place(x=160,y=145)
e1 = Entry()
e1.place(x=35,y=150)
e2 = Entry()
e2.place(x=35,y=190)
j = 0
root.mainloop()