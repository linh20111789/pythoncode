from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)
    
ws = Tk()
ws.geometry('900x750+500+100')
ws.title('ToDo List - by TRUNG KIEN')
ws.config(bg="#ffffb3")
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=35,
    height=10,
    font=('Times', 16),
    bd=0,
    fg=("#000000"),
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)

task_file = open("todolist.txt", "r")

task_list = task_file.readlines()

task_file.close()

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=("Segoe UI", 30),
    )

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

def on_closing():
    task_list = [lb.get(i) + "\n" for i in range(lb.size())]
    task_file = open("todolist.txt", "w")
    task_file.writelines(task_list)
    task_file.close()
    ws.destroy()

ws.protocol("WM_DELETE_WINDOW", on_closing)

ws.mainloop()
