import tkinter
from tkinter import *


def cypher():
   fin=[]
   b=a.get()
   s = [char for char in b]
   for i in range(len(s)):
       if 1072<=ord(s[i])<=1103:
           fin.append(chr(1072 + (1103 - ord(s[i]))))
       elif 1040<=ord(s[i])<=1071:
           fin.append(chr(1040 + (1071 - ord(s[i]))))
       elif 97<=ord(s[i])<=122:
          fin.append(chr(97 + (122 - ord(s[i]))))
       elif 65<=ord(s[i])<=90:
          fin.append(chr(65 + (90 - ord(s[i]))))
       else:
           fin.append(s[i])
   g=''.join(map(str, fin))
   return a.set(g)

window = Tk()
window.title("Шифр Атбаш")
window.geometry('300x150')
window["bg"]="gray22"

x = (window.winfo_screenwidth() - window.winfo_reqwidth()) / 2
y = (window.winfo_screenheight() - window.winfo_reqheight()) / 2
window.wm_geometry("+%d+%d" % (x, y))

a =StringVar()
pole = Entry(window,width=46 ,textvariable=a, bg='#000000', fg='#ffffff')
pole.place(x=10,y=10)
button = tkinter.Button(window,background="#555",foreground="#ccc", text = "Зашифровать",command = cypher)
button.place(x=115,y=50)

window.mainloop()
