import tkinter as tk
master = tk.Tk()
master.geometry('960x450')
master.title("Student detail")
# def submit_handler():
#   print("It has been submitted")
#

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


def quitt():
    print("It has been cancelled")

tk.Label(master,text="Name",fg='teal',font=('Arial',18)).place(x=0,y=0)
tk.Label(master,text="Age",fg='teal',font=('Arial',18)).place(x=0,y=70)
tk.Label(master,text="Mark",fg='teal',font=('Arial',18)).place(x=0,y=140)
e1 = tk.Entry()
e1.place(x=0,y=40)
e2 = tk.Entry()
e2.place(x=0,y=110)
e3 = tk.Entry()
e3.place(x=0,y=180)
btn1 = tk.Button(master,text="SUBMIT",bg='light blue',fg='black',font=('Arial',15),command=submit_handler).place(x=0,y=220)
btn2 = tk.Button(master,text="Cancel",bg='light blue',fg='black',font=('Arial',15),command=quitt).place(x=100,y=220)



master.mainloop()
