from tkinter import *
win=Tk()
def add():
    a=int(t1.get())
    b=int(t2.get())
    c=a+b
    l4.config(text=""+str(c))
    
def sub():
    a=int(t1.get())
    b=int(t2.get())
    c=a-b
    l4.config(text=""+str(c))
    
def mul():
    a=int(t1.get())
    b=int(t2.get())
    c=a*b
    l4.config(text=""+str(c))
    
def div():
    a=int(t1.get())
    b=int(t2.get())
    c=a/b
    l4.config(text=""+str(c))
    
win.title("Button Window")
f1 = ('arial',15,'bold')
l1=Label(win,text='Enter The Value of X',font=f1)
l1.place(x=100,y=50) 
    
t1=Entry(win,bd=3,font=f1)
t1.place(x=400,y=50)    
    
l2=Label(win,text='Enter The Value of Y',font=f1)
l2.place(x=100,y=100) 
    
t2=Entry(win,bd=3,font=f1)
t2.place(x=400,y=100)  
    
l3=Label(win,text='Ans',font=f1)
l3.place(x=280,y=150)    

l4=Label(win,text='_ _ _ _ _ _ ',font=f1)
l4.place(x=400,y=150)

b1=Button(win,text='Add',bg='yellow',fg='blue',font=f1,command=add)
b1.place(x=170,y=220)

b2=Button(win,text='Sub',bg='yellow',fg='blue',font=f1,command=sub)
b2.place(x=270,y=220)

b3=Button(win,text='Mul',bg='yellow',fg='blue',font=f1,command=mul)
b3.place(x=370,y=220)

b4=Button(win,text='Div',bg='yellow',fg='blue',font=f1,command=div)
b4.place(x=470,y=220)

win.geometry('500x500+100+50')
win.mainloop()
