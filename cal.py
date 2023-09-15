import tkinter as tk
import tkinter.messagebox
root=tk.Tk()
f=tk.Frame(root,bg="gray",height=500,width=500,borderwidth=5)
f.pack()
e=tk.Entry(f,bg="lightgray",borderwidth=3,width=15,font=("courier",25,"bold"))
e.place(x=100,y=30)

def myclick(num):
    e.insert(tk.END,num)

def equal():
    try:
        y=str(eval(e.get()))
        e.delete(0,tk.END)
        e.insert(0,y)
    except:
        tkinter.messagebox.showinfo("Error","Syntax Error")

def clear():
    e.delete(0,tk.END)


b1=tk.Button(f,height=3,width=8,text=1,bg="lightgray",command=lambda:myclick(1))
b1.place(x=100,y=100)

b2=tk.Button(f,height=3,width=8,text=2,bg="lightgray",command=lambda:myclick(2))
b2.place(x=180,y=100)

b3=tk.Button(f,height=3,width=8,text=3,bg="lightgray",command=lambda:myclick(3))
b3.place(x=260,y=100)

b4=tk.Button(f,height=3,width=8,text=4,bg="lightgray",command=lambda:myclick(4))
b4.place(x=100,y=200)

b5=tk.Button(f,height=3,width=8,text=5,bg="lightgray",command=lambda:myclick(5))
b5.place(x=180,y=200)

b6=tk.Button(f,height=3,width=8,text=6,bg="lightgray",command=lambda:myclick(6))
b6.place(x=260,y=200)

b7=tk.Button(f,height=3,width=8,text=7,bg="lightgray",command=lambda:myclick(7))
b7.place(x=100,y=300)

b8=tk.Button(f,height=3,width=8,text=8,bg="lightgray",command=lambda:myclick(8))
b8.place(x=180,y=300)

b9=tk.Button(f,height=3,width=8,text=9,bg="lightgray",command=lambda:myclick(9))
b9.place(x=260,y=300)

b10=tk.Button(f,height=3,width=8,text=0,bg="lightgray",command=lambda:myclick(0))
b10.place(x=100,y=400)

b11=tk.Button(f,height=3,width=8,text="+",bg="lightgray",command=lambda:myclick("+"))
b11.place(x=340,y=100)

b12=tk.Button(f,height=3,width=8,text="-",bg="lightgray",command=lambda:myclick("-"))
b12.place(x=340,y=200)

b13=tk.Button(f,height=3,width=8,text="*",bg="lightgray",command=lambda:myclick("*"))
b13.place(x=340,y=300)

b14=tk.Button(f,height=3,width=8,text="/",bg="lightgray",command=lambda:myclick("/"))
b14.place(x=340,y=400)

b15=tk.Button(f,height=3,width=8,text="=",bg="lightgray",command=equal)
b15.place(x=260,y=400)

b16=tk.Button(f,height=3,width=8,text="C",bg="lightgray",command=clear)
b16.place(x=180,y=400)

root.mainloop()
