#importing the important modules
import tkinter as tk       
from tkinter import ttk 
from tkinter  import messagebox 
import sqlite3 as sql

#defining the function to INSERT/ADD tasks to the list
def add_tsk():
    tsk_string=tsk_field.get()
    if len(tsk_string)==0:
        messagebox.showinfo('Error','Field is Empty.')
    else:
        tasks.append(tsk_string)
        the_cursor.execute('insert into tasks values (?)', (tsk_string,))
        list_update()
        tsk_field.delete(0,'end')

#defining the function to UPDATE the list 
def list_update():
    clear_list()
    for task in tasks:
        tsk_listbox.insert('end',task)

#Defining the funtion to Delete perticular task from the list
def delete_tsk():
    try:
        value = tsk_listbox.get(tsk_listbox.curselection())
        if value in tasks:
            tasks.remove(value)
            list_update()
            the_cursor.execute('delete from tasks where title = ?', (value,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')              

#defining function to delete all tasks from the list
def tsk_delete():
    mesg_box=messagebox.askyesno('Delete All','Are you sure?')
    if mesg_box == True:
        while(len(tasks))!=0:
            tasks.pop()
            the_cursor.execute("delete from tasks")
            list_update()
    
#Defining function to CLEAR the list
def clear_list():
    tsk_listbox.delete(0,'end')

#Defining function to close the application
def close():
    print(tasks)
    root.destroy()

#defining function to RETRIEVE the data from the database
def retrieve_database():
    while(len(tasks)!=0):
        tasks.pop()
        for row in the_cursor.execute('select title from tasks'):
            tasks.append(row[0])

#main function
if _name_ =="__main__":
    root=tk.Tk()
    root.title("TO_DO List Manager")
    root.geometry("500x450+750+250")
    root.resizable(0,0)
    root.configure(bg="violet")
    #using connect() method to connect to the database
    conn=sql.connect('listOfTasks.db')
    the_cursor=conn.cursor()
    the_cursor.execute('create table if not exists tasks(title text)')

    #defining an empty list
    tasks=[]

    #defining frames using the tk.Frame() widget

    header_frame=tk.Frame(root,bg="violet")
    func_frame=tk.Frame(root,bg="violet")
    listbox_frame=tk.Frame(root,bg="violet")

    #using the pack() method to place the frames in the application
    header_frame.pack(fill='both')
    func_frame.pack(side="left",expand=True,fill="both")
    listbox_frame.pack(side="right",expand=True,fill="both")

    #defining a label using the ttk.label widget
    header_label=ttk.Label(header_frame,text="the to-do list",font=("consolas","30","bold"),background="AntiqueWhite",foreground="green")
    tsk_label=ttk.Label(func_frame,text="Enter the task",font=("French Script MT","20","bold"),background="AntiqueWhite",foreground="black")
    
    #place & pack the labels
    header_label.pack(padx=20,pady=20)
    tsk_label.place(x=30,y=40)

    #defining an ENTRY field using the ttk.entry() widget
    tsk_field=ttk.Entry(func_frame,font=("Consolas","13"),background="Cornsilk",foreground="Brown",width=19)
    tsk_field.place(x=30,y=80)

    #defining BUTTONS to the application using the ttk.Button () widget
    add_button=ttk.Button(func_frame,text="Add Task",width=24,command=add_tsk)
    del_button=ttk.Button(func_frame,text="Delete Task",width=24,command=delete_tsk)
    tsk_del_all_button=ttk.Button(func_frame,text="Delete all Task",width=24,command=tsk_delete)
    exit_button=ttk.Button(func_frame,text="Exit",width=24,command=close)

    #using the place() method to set the position of the button
    add_button.place(x=30,y=120)
    del_button.place(x=30,y=160)
    tsk_del_all_button.place(x=30,y=200)
    exit_button.place(x=30,y=240)

    #defining a list box using the ttk.listbox() widget
    tsk_listbox=tk.Listbox(listbox_frame,width=26,height=13,selectmode="SINGLE",background="White",foreground="black",selectbackground="peru",selectforeground="white")
    tsk_listbox.place(x=10,y=20)

    retrieve_database()
    list_update()
    root.mainloop()
    conn.commit()
    the_cursor.close()
