import tkinter as tk
import csv

master = tk.Tk()
master.geometry('900x400')
master.title("Calculator")
master.configure(bg='light blue')

tk.Label(master,text="Calculator",bg="teal",fg="white",font=("Calibri",30,'bold')).place(x=300,y=10)

e1 = tk.result(font=('Arial',15,'bold','italic'))
e1.place(x=2,y=100)

btn1= tk.Button(master,text="1",bg="aqua",fg="black",font=("times new roman",10)).place(x=20,y=150)
btn2= tk.Button(master,text="2",bg="aqua",fg="black",font=("times new roman",10)).place(x=60,y=150)
btn3= tk.Button(master,text="3",bg="aqua",fg="black",font=("times new roman",10)).place(x=100,y=150)
btn4= tk.Button(master,text="4",bg="aqua",fg="black",font=("times new roman",10)).place(x=20,y=200)
btn5= tk.Button(master,text="5",bg="aqua",fg="black",font=("times new roman",10)).place(x=60,y=200)
btn6= tk.Button(master,text="6",bg="aqua",fg="black",font=("times new roman",10)).place(x=100,y=200)
btn7= tk.Button(master,text="7",bg="aqua",fg="black",font=("times new roman",10)).place(x=20,y=250)
btn8= tk.Button(master,text="8",bg="aqua",fg="black",font=("times new roman",10)).place(x=60,y=250)
btn9= tk.Button(master,text="9",bg="aqua",fg="black",font=("times new roman",10)).place(x=100,y=250)
btn10= tk.Button(master,text=".",bg="aqua",fg="black",font=("times new roman",10)).place(x=20,y=300)
btn11= tk.Button(master,text="0",bg="aqua",fg="black",font=("times new roman",10)).place(x=60,y=300)
btn12= tk.Button(master,text="=",bg="aqua",fg="black",font=("times new roman",10)).place(x=100,y=300)



master.mainloop()