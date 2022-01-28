from tkinter import *
from tkinter import ttk
from translator import translate
from data import keys,languages


m = Tk()
m.title = "Translator"
m.geometry("400x300")

tkvarq = StringVar(m)
tkvarq.set(keys[0])


def submit():
    input_txt = input_.get(index1="1.0", index2=END)
    lang = option.get()
    output = translate(input_txt, to_lang=languages[lang])
    output_.delete("1.0", END)
    output_.insert(END, output)


l1 = Label(text="From :")
l2 = Label(text="To :")

l1.grid(column=0, row=1)
l2.grid(column=0, row=2)

input_ = Text(height=5, width=40)
input_.grid(row=1, column=1, columnspan=3, pady=20, padx=10)

button1 = Button(width=10, height=1, text="submit", command=submit)
button1.grid(sticky="w", row=2, column=2)

output_ = Text(m, height=5, width=40)
output_.grid(row=3, columnspan=2, column=1, pady=20, padx=10)

option = ttk.Combobox(m, width=20, textvariable=tkvarq)
option["values"] = keys
option.grid(row=2, column=1)


m.mainloop()
