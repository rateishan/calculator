import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

root= tk.Tk()
root.title("Calculator")
root.iconbitmap('sun.ico')  
root.config(bg='black')
root.geometry("400x400")
root.resizable(False,False)

def click(number):
    entryfield.insert(tk.END,number)
    
def clear():
    entryfield.delete(0,tk.END)

def answer():
    evaluation=entryfield.get()
    try :
       result=eval(evaluation)
       ans=round(result,3)
       entryfield.delete(0,tk.END)
       entryfield.insert(tk.END,ans)
    except SyntaxError:
        messagebox.showerror("Error","Invalid Input")
        entryfield.delete(0,tk.END)
    except ZeroDivisionError:
        messagebox.showerror("Error","Cannot divide by zero")
        entryfield.delete(0,tk.END)
    
frame1=tk.Frame(root,bg='black')
frame1.grid(row=0,column=0,padx=10,pady=10)

entryfield =tk.Entry(frame1,width=24,font=('arial',20,'bold'),bg='black',fg='white',bd=2)
entryfield.grid(row=0,column=0,padx=5,pady=5)

frame2=tk.Frame(root,bg='black')
frame2.grid(row=1,column=0,padx=10,pady=10)

b1=tk.Button(frame2,text='7',width=4,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= lambda:click('7'))
b1.grid(row=1,column=0,padx=3,pady=3)

b2=tk.Button(frame2,text='8',width=4,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= lambda:click('8'))
b2.grid(row=1,column=1,padx=3,pady=3)

b3=tk.Button(frame2,text='9',width=4,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= lambda:click('9'))
b3.grid(row=1,column=2,padx=3,pady=3)

b4=tk.Button(frame2,text='+',width=4,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= lambda:click('+'))
b4.grid(row=1,column=3,padx=3,pady=3)

b5=tk.Button(frame2,text='4',width=4,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= lambda:click('4'))
b5.grid(row=2,column=0,padx=3,pady=3)

b6=tk.Button(frame2,text='5',width=4,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= lambda:click('5'))
b6.grid(row=2,column=1,padx=3,pady=3)

b7=tk.Button(frame2,text='6',width=4,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= lambda:click('6'))
b7.grid(row=2,column=2,padx=3,pady=3)

b8=tk.Button(frame2,text='-',width=4,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= lambda:click('-'))
b8.grid(row=2,column=3,padx=3,pady=3)

b9=tk.Button(frame2,text='1',width=4,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= lambda:click('1'))
b9.grid(row=3,column=0,padx=3,pady=3)

b10=tk.Button(frame2,text='2',width=4,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= lambda:click('2'))
b10.grid(row=3,column=1,padx=3,pady=3)

b11=tk.Button(frame2,text='3',width=4,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= lambda:click('3'))
b11.grid(row=3,column=2,padx=3,pady=3)

b12=tk.Button(frame2,text='*',width=4,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= lambda:click('*'))
b12.grid(row=3,column=3,padx=3,pady=3)

b13=tk.Button(frame2,text='0',width=4,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= lambda:click('0'))
b13.grid(row=4,column=0,padx=3,pady=3)

b14=tk.Button(frame2,text='=',width=9,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= answer)
b14.grid(row=4,column=1,columnspan=2,padx=3,pady=3)

b15=tk.Button(frame2,text='/',width=4,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= lambda:click('/'))
b15.grid(row=4,column=3,padx=3,pady=3)

b16=tk.Button(frame2,text='c',width=19,font=('arial',20,'bold'),bg='gray',fg='white',bd=2,command= clear)
b16.grid(row=5,columnspan=5,padx=3,pady=3)


root.mainloop()