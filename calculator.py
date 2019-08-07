#!/usr/bin/python3

from tkinter import *

# note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
root = Tk()
# Code to add widgets will go here...
root.title('Calculator')
# root.geometry("640x640")
# tk.grid()

bottomframe = Frame(root)
bottomframe.pack(side=TOP)

def button_value(arg):
    print(arg)

name = StringVar()
e1 = Entry(bottomframe, textvariable=name, width=33)
e1.pack(side=TOP)

def calculate_result():
    ip = str(name.get())
    if('+' in ip):
        list1 = ip.split('+')
        num1 = float(list1[0])
        num2 = float(list1[1])
        ans = num1+num2
        if(ans.is_integer()):
            ans1 = "=" + str(int(ans))
        else:
            ans1 = "=" + str(ans)
        e1.insert('end',ans1)
    elif ('-' in ip):
        list1 = ip.split('-')
        num1 = float(list1[0])
        num2 = float(list1[1])
        ans = num1 - num2
        if (ans.is_integer()):
            ans1 = "=" + str(int(ans))
        else:
            ans1 = "=" + str(ans)
        e1.insert('end', ans1)
    elif ('x' in ip):
        list1 = ip.split('x')
        num1 = float(list1[0])
        num2 = float(list1[1])
        ans = num1 * num2
        if (ans.is_integer()):
            ans1 = "=" + str(int(ans))
        else:
            ans1 = "=" + str(ans)
        e1.insert('end', ans1)
    elif ('/' in ip):
        list1 = ip.split('/')
        num1 = float(list1[0])
        num2 = float(list1[1])
        ans = num1 / num2
        if (ans.is_integer()):
            ans1 = "=" + str(int(ans))
        else:
            ans1 = "=" + str(ans)
        e1.insert('end', ans1)
    elif ('%' in ip):
        list1 = ip.split('%')
        num1 = float(list1[0])
        num2 = float(list1[1])
        ans = num1 % num2
        if (ans.is_integer()):
            ans1 = "=" + str(int(ans))
        else:
            ans1 = "=" + str(ans)
        e1.insert('end', ans1)

button = Button(bottomframe, text="(", bg="yellow", width=6, height=2, activebackground="red", command=lambda:e1.insert('end',"("))
button.pack(side=LEFT)
button = Button(bottomframe, text=")", bg="yellow", width=6, height=2, activebackground="red", command=lambda:e1.insert('end',")"))
button.pack(side=LEFT)
button = Button(bottomframe, text="%", bg="yellow", width=6, height=2, activebackground="red", command=lambda:e1.insert('end',"%"))
button.pack(side=LEFT)
button = Button(bottomframe, text="CE", bg="steelblue", activebackground="blue", width=6, height=2, fg='yellow', command=lambda:e1.delete(0,'end'))
button.pack(side=LEFT)

bottomframe = Frame(root)
bottomframe.pack(side=TOP)

button1 = Button(bottomframe, text=7, width=6, height=2, command=lambda:e1.insert('end',7))
button1.pack(side=LEFT)
button1 = Button(bottomframe, text=8, width=6, height=2, command=lambda:e1.insert('end',8))
button1.pack(side=LEFT)
button1 = Button(bottomframe, text=9, width=6, height=2, command=lambda:e1.insert('end',9))
button1.pack(side=LEFT)

button = Button(bottomframe, text="/", bg="yellow", width=6, height=2, activebackground="red", command=lambda:e1.insert('end',"/"))
button.pack(side=LEFT)


bottomframe1 = Frame(root)
bottomframe1.pack(side=TOP)


button1 = Button(bottomframe1, text=4, width=6, height=2, command=lambda:e1.insert('end',4))
button1.pack(side=LEFT)
button1 = Button(bottomframe1, text=5, width=6, height=2, command=lambda:e1.insert('end',5))
button1.pack(side=LEFT)
button1 = Button(bottomframe1, text=6, width=6, height=2, command=lambda:e1.insert('end',6))
button1.pack(side=LEFT)


button = Button(bottomframe1, text="x", bg="yellow", width=6, height=2, activebackground="red", command=lambda:e1.insert('end',"x"))
button.pack(side=LEFT)

bottomframe2 = Frame(root)
bottomframe2.pack(side=TOP)

button1 = Button(bottomframe2, text=1, width=6, height=2, command=lambda:e1.insert('end',1))
button1.pack(side=LEFT)
button1 = Button(bottomframe2, text=2, width=6, height=2, command=lambda:e1.insert('end',2))
button1.pack(side=LEFT)
button1 = Button(bottomframe2, text=3, width=6, height=2, command=lambda:e1.insert('end',3))
button1.pack(side=LEFT)

button = Button(bottomframe2, text="-", bg="yellow", width=6, height=2, activebackground="red", command=lambda:e1.insert('end',"-"))
button.pack(side=LEFT)

bottomframe3 = Frame(root)
bottomframe3.pack(side=TOP)
button = Button(bottomframe3, text=0, width=6, height=2, command=lambda:e1.insert('end',0))
button.pack(side=LEFT)
button = Button(bottomframe3, text=".", width=6, height=2, command=lambda:e1.insert('end',"."))
button.pack(side=LEFT)
button = Button(bottomframe3, text="=", bg="steelblue", activebackground="blue", width=6, height=2, fg='yellow', command=calculate_result)
button.pack(side=LEFT)
button = Button(bottomframe3, text="+", bg="yellow", width=6, height=2, activebackground="red", command=lambda:e1.insert('end',"+"))
button.pack(side=LEFT)

bottomframe4 = Frame(root)
bottomframe4.pack(side=TOP)
button3 = Button(bottomframe4, text='Stop', width=28, bg="green", activebackground="red", activeforeground="yellow",
                    command=root.destroy)
button3.pack()

root.mainloop()