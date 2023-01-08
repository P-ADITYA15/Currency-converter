from tkinter import *
from tkinter import ttk
from tkinter import messagebox

d=Tk()
d.title("THE CONVERTER")
d.geometry("800x800")

#create tab
m = ttk.Notebook(d)
m.pack(pady=6)

#create frame
cf = Frame(m,width=500,height=500)
cv = Frame(m,width=600,height=600)

cf.pack(fill="both",expand=1)
cv.pack(fill="both",expand=1)

#add tab
m.add(cf,text="Currencies")
m.add(cv,text="convert")


m.tab(1,state="disabled")

def lock():
    if not he.get() or not cone.get() or not cr.get():
        messagebox.showwarning("WARNING!", "You didn't fill all")
    else:
        he.config(state="disabled")
        cone.config(state="disabled")
        cr.config(state="disabled")
        m.tab(1, state="normal")
        al.config(text=f'amount of {he.get()} to convert to {cone.get()}')
        cl.config(text=f'equals this many {cone.get()}')
        cb.config(text=f'convert from {he.get()}')
def unlock():
    he.config(state="normal")
    cone.config(state="normal")
    cr.config(state="normal")
    m.tab(1, state="disabled")


h = LabelFrame(cf,text="your home currency")
h.pack(pady=14)

he = Entry(h,font=("Helvetica",24))
he.pack(pady=10,padx=15)


con = LabelFrame(cf,text="conversion currency")
con.pack(pady=22)

conl = Label(con,text="Currency to convert to")
conl.pack(pady=22)

cone = Entry(con,font=("Helvetica",24))
cone.pack(pady=10,padx=15)

conr = Label(con,text="Current currency rate")
conr.pack(pady=22)

cr = Entry(con,font=("Helvetica",24))
cr.pack(pady=10,padx=15)


bf = Frame(cf)
bf.pack(pady=15)

lb = Button(bf,text="Lock",command=lock)
lb.grid(row=0,column=0,pady=10)

lb = Button(bf,text="Unlock",command=unlock)
lb.grid(row=0,column=3,pady=10,padx=10)



#2nd tab

def convert():
    ce.delete(0,END)
    q=float(cr.get())
    r=float(ae.get())
    pro = q*r
    ce.insert(0,pro)
def clr():
    ae.delete(0,END)
    ce.delete(0, END)


al = LabelFrame(cv,text="amount to convert")
al.pack(pady=20)

ae = Entry(al,font=("Helvetica",24))
ae.pack(padx=10,pady=10)

cb = Button(cv,text="Convet",command=convert)
cb.pack(pady=20)

cl = LabelFrame(cv,text="converted currency")
cl.pack(pady=20)

ce = Entry(cl,font=("Helvetica",24),bd=0,bg="systembuttonface")
ce.pack(padx=10,pady=10)

clb = Button(cv,text="clear",command=clr)
clb.pack(pady=10)

sp = Label(cv,text="",width=68)
sp.pack()




d.mainloop()