import Encoder
import Decoder
import clipboard
from tkinter import *

def go():
    s=t.get(1.0,END)
    print(s)

def encode():
    sentence=t1.get(1.0,END)
    x=Encoder.encode_sent(sentence)
    t2.configure(state="normal")
    t2.delete(1.0,END)
    t2.insert(1.0,x)
    t2.configure(state="disabled")

def decode():
    sentence=t1.get(1.0,END)
    x=Decoder.decode_sent(sentence)
    t2.configure(state="normal")
    t2.delete(1.0,END)
    t2.insert(1.0,x)
    t2.configure(state="disabled")

def sweep():
    t1.delete(1.0,END)
    t2.configure(state="normal")
    t2.delete(1.0,END)
    t2.configure(state="disabled")

def copy_foo():
    copy_text=""
    t2.configure(state="normal")
    copy_text=t2.get(1.0,END)
    t2.configure(state="disabled")
    clipboard.copy(copy_text)

window=Tk()
window.resizable(0,0)
window.geometry("400x320")
window.title("Encode and Decode Machine")

l=Label(window,text="Encoding and Decoding Machine",font=("Arial",19))
l.grid(row=0,column=0,columnspan=3,padx=10)

t1=Text(window,font=("Arial",12),width=27,height=7)
t1.grid(row=1,column=0,columnspan=2,rowspan=2,padx=10,pady=5)

t2=Text(window,font=("Arial",12),width=27,height=7)
t2.configure(state="disabled")
t2.grid(row=3,column=0,columnspan=2,rowspan=2,padx=10,pady=5)

b1=Button(window,text="Encode",font=("Arial",20),width=7,command=encode)
b1.grid(row=1,column=2,padx=3,pady=1)

b2=Button(window,text="Decode",font=("Arial",20),width=7,command=decode)
b2.grid(row=2,column=2,padx=3)

b3=Button(window,text="Copy",font=("Arial",20),width=7,command=copy_foo)
b3.grid(row=3,column=2,padx=3)

b4=Button(window,text="Clear",font=("Arial",20),width=7,command=sweep)
b4.grid(row=4,column=2,padx=3)

window.mainloop()