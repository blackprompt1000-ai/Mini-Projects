import tkinter as t
from tkinter import messagebox  #give pop up messages like warnings and task added

main = t.Tk()                    #open a blank window 
main.title("My To-Do List")
main.geometry("400x400")        #set the main window size
main.resizable(True, True)    #make the window resizable

tasks_listbox = t.Listbox(main, width=40, height=10, selectmode=t.SINGLE)   #defining the size and type of listbox (i.e single selection)
tasks_listbox.pack(pady=10)    #pady give space above and below of this particular task box

task_entry = t.Entry(main, width=30) #entry box to enter the task
task_entry.pack(pady=5)              #pady give space above and below of this particular task in the list


def add_task():
    task = task_entry.get()   #get take all text u type in the entry box
    if task != "":
        tasks_listbox.insert(t.END, task)
        task_entry.delete(0, t.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")


def delete_task():
    try:
        index = tasks_listbox.curselection()[0]  #get the index of the selected task in the listbox 
        tasks_listbox.delete(index)              # with cursor and 0 is for first selected element and futher delete that element
    except:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_all():
    tasks_listbox.delete(0, t.END)


add = t.Button(main, text="Add Task", width=20, command=add_task)
add.pack(pady=5)

delete= t.Button(main, text="Delete Task", width=20, command=delete_task)
delete.pack(pady=5)

clear= t.Button(main, text="Clear All", width=20, command=clear_all)
clear.pack(pady=5)

main.mainloop()