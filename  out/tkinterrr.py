import tkinter as tk
from PIL import Image , ImageTk


master = tk.Tk()
master.geometry('960x450')
master.title("Student detail")
# def submit_handler():
#   print("It has been submitted")
master.configure(bg='light pink')

def submit_handler():
    # print("It has been clicked")
    name = e1.get()
    age = e2.get()
    mark = e3.get()
    student_data = [name,age,mark]
    print(f"Name: {name} Age: {age} Mark: {mark}")
    # with open("student_data.csv",'a',newline='') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(student_data)

def clear():
  e1.delete(0, 'end')
  e2.delete(0, 'end')
  e3.delete(0, 'end')

def quitt():
    print("It has been cancelled")

tk.Label(master,text="Details",font=('Arial Bold',24)).place(x=150,y=5)
tk.Label(master,text="Name",fg='teal',font=('Arial',18)).place(x=0,y=70)
tk.Label(master,text="Age",fg='teal',font=('Arial',18)).place(x=0,y=140)
tk.Label(master,text="Breed",fg='teal',font=('Arial',18)).place(x=0,y=210)
e1 = tk.Entry()
e1.place(x=0,y=110)
e2 = tk.Entry()
e2.place(x=0,y=180)
e3 = tk.Entry()
e3.place(x=0,y=250)
btn1 = tk.Button(master,text="SUBMIT",bg='light blue',fg='black',font=('Arial',15),command=submit_handler).place(x=0,y=300)
btn2 = tk.Button(master,text="Cancel",bg='light blue',fg='black',font=('Arial',15), command=quitt).place(x=100,y=300)
btn1= tk.Button(master,text="Reset",bg="light blue",fg="black",font=('Arial',15), command=clear).place(x=190,y=300)


master.iconphoto(False,tk.PhotoImage(file='hello.png'))

image = Image.open("h1.jpg")
canvas = tk.Canvas(master , height=300 , width=300 , bg='white')
canvas.pack()
image = ImageTk.PhotoImage(image)
canvas.create_image(40 , 100 , image=image,anchor = 'w')


master.mainloop()

