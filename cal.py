import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root= tk.Tk()
root.title("Calculator")
root.iconbitmap('sun.ico')  
root.config(bg='black')
root.geometry("400x400")
root.resizable(True,True)
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=5)
root.grid_columnconfigure(0,weight=1)

def addnum(num):
    entry.configure(state=tk.NORMAL)
    entry.insert(tk.END,num)
    entry.configure(state=tk.DISABLED)


def evaluvate():
    try:
        expresion=entry.get()
        result=eval(expresion)
        entry.configure(state=tk.NORMAL)
        entry.delete(0,tk.END)
        entry.insert(tk.END,result)
        entry.configure(state=tk.DISABLED)

    except:
        messagebox.showerror("Error","Invalid Input")

def clear():
    entry.configure(state=tk.NORMAL)
    entry.delete(0,tk.END)
    entry.configure(state=tk.DISABLED)


frame1=tk.Frame(root, width=400,height=200,background='black')
frame1.grid(row=0,column=0,sticky=tk.NSEW)

frame2=tk.Frame(root, width=400,height=200,background='gray')
frame2.grid(row=1,column=0,sticky=tk.NSEW)

for i in range(4):
    frame2.grid_rowconfigure(i,weight=1)
    frame2.grid_columnconfigure(i,weight=1) 

entry=tk.Entry(frame1,font=('Arial',30),state=tk.DISABLED, disabledbackground='white',bg='white',fg='black')
entry.pack(fill=tk.BOTH,expand=True)

b1=tk.Button(frame2,text='7',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('7'))
b1.grid(row=0,column=0,sticky=tk.NSEW)

b2=tk.Button(frame2,text='8',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('8'))
b2.grid(row=0,column=1,sticky=tk.NSEW)

b3=tk.Button(frame2,text='9',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('9'))
b3.grid(row=0,column=2,sticky=tk.NSEW)

b4=tk.Button(frame2,text='/',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('/'))
b4.grid(row=0,column=3,sticky=tk.NSEW)

b5=tk.Button(frame2,text='4',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('4'))
b5.grid(row=1,column=0,sticky=tk.NSEW)

b6=tk.Button(frame2,text='5',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('5'))
b6.grid(row=1,column=1,sticky=tk.NSEW)

b7=tk.Button(frame2,text='6',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('6'))
b7.grid(row=1,column=2,sticky=tk.NSEW)

b8=tk.Button(frame2,text='*',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('*'))
b8.grid(row=1,column=3,sticky=tk.NSEW)

b9=tk.Button(frame2,text='1',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('1'))
b9.grid(row=2,column=0,sticky=tk.NSEW)

b10=tk.Button(frame2,text='2',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('2'))
b10.grid(row=2,column=1,sticky=tk.NSEW)

b11=tk.Button(frame2,text='3',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('3'))
b11.grid(row=2,column=2,sticky=tk.NSEW)

b12=tk.Button(frame2,text='-',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('-')) 
b12.grid(row=2,column=3,sticky=tk.NSEW)

b13=tk.Button(frame2,text='0',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('0'))
b13.grid(row=3,column=0,sticky=tk.NSEW)

b14=tk.Button(frame2,text='.',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('.'))
b14.grid(row=3,column=1,sticky=tk.NSEW)

b15=tk.Button(frame2,text='c',font=('Arial',30),bg='white',fg='black',command= lambda: clear())
b15.grid(row=3,column=2,sticky=tk.NSEW)

b16=tk.Button(frame2,text='+',font=('Arial',30),bg='white',fg='black',command= lambda: addnum('+'))
b16.grid(row=3,column=3,sticky=tk.NSEW)

b17=tk.Button(frame2,text='=',font=('Arial',30),bg='white',fg='black',command= lambda:evaluvate())
b17.grid(row=4,column=0,columnspan=4,sticky=tk.NSEW)


root.mainloop()