
from tkinter import *


win=Tk()
win.title('Calculator')

# FUNCTION SECTION

check=0

def click(a):
    global check
    if check==1:
        scr.delete(0,'end')
        scr.insert(100,a,)
        check=0
    else:
        scr.insert(100,a)


def clear():
    scr.delete(0,'end')

def equal():
    global check
    eqa=scr.get()
    ans=eval(eqa)
    scr.delete(0,'end')
    scr.insert(100,ans)
    check=1

def click1():
    per=scr.get()
    an=eval

 
# DESIGN SECTION

scr=Entry(win,width=20,borderwidth=5,font=('bold',15))
scr.grid(columnspan=6,column=0,row=0,ipadx=20,ipady=20)
scr.focus()

#buttons
bt9=Button(win,text='9',bg='grey',font=('arial bold',18),pady=10,padx=10,borderwidth=10,command=lambda:click(9))
bt8=Button(win,text='8',bg='grey',font=('arial bold',18),pady=10,padx=10,borderwidth=10,command=lambda:click(8))
bt7=Button(win,text='7',bg='grey',font=('arial bold',18),pady=10,padx=10,borderwidth=10,command=lambda:click(7))

bt6=Button(win,text='6',bg='grey',font=('arial bold',18),pady=10,padx=10,borderwidth=10,command=lambda:click(6))
bt5=Button(win,text='5',bg='grey',font=('arial bold',18),pady=10,padx=10,borderwidth=10,command=lambda:click(5))
bt4=Button(win,text='4',bg='grey',font=('arial bold',18),pady=10,padx=10,borderwidth=10,command=lambda:click(4))

bt3=Button(win,text='3',bg='grey',font=('arial bold',18),pady=10,padx=10,borderwidth=10,command=lambda:click(3))
bt2=Button(win,text='2',bg='grey',font=('arial bold',18),pady=10,padx=10,borderwidth=10,command=lambda:click(2))
bt1=Button(win,text='1',bg='grey',font=('arial bold',18),pady=10,padx=10,borderwidth=10,command=lambda:click(1))

bt0=Button(win,text='0',bg='grey',font=('arial bold',18),pady=5,padx=50,borderwidth=10,command=lambda:click(0))


bt9.grid(column=2,row=2)
bt8.grid(column=1,row=2)
bt7.grid(column=0,row=2)

bt6.grid(column=2,row=3)
bt5.grid(column=1,row=3)
bt4.grid(column=0,row=3)

bt3.grid(column=2,row=4)
bt2.grid(column=1,row=4)
bt1.grid(column=0,row=4)

bt0.grid(columnspan=2,column=0,row=5)

#Operators Button

pe=Button(win,text='%',font=('arial bold',15),pady=15,padx=10,borderwidth=10,command=lambda:click1)
ad=Button(win,text='+',font=('arial bold',15),pady=15,padx=10,borderwidth=10,command=lambda:click('+'))
su=Button(win,text='-',font=('arial bold',15),pady=10,padx=15,borderwidth=10,command=lambda:click('-'))
mu=Button(win,text='*',font=('arial bold',15),pady=10,padx=15,borderwidth=10,command=lambda:click('*'))
di=Button(win,text='/',font=('arial bold',15),pady=10,padx=15,borderwidth=10,command=lambda:click('/'))
p=Button(win,text='.',font=('arial bold',15),pady=10,padx=15,borderwidth=10,command=lambda:click('.'))
eq=Button(win,text='=',font=('arial bold',15),pady=60,padx=10,borderwidth=10,command=equal)
win.bind('<Return>',equal)
cl=Button(win,text='CE',font=('arial bold',13),pady=10,padx=10,borderwidth=10,command=clear)

cl.grid(column=0,row=1)
di.grid(column=1,row=1)
mu.grid(column=2,row=1)
su.grid(column=3,row=1)

pe.grid(column=3,row=3)
ad.grid(column=3,row=2)
eq.grid(rowspan=2,column=3,row=4)
p.grid(column=2,row=5)





win.mainloop()