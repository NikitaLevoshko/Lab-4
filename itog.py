from tkinter import *
from tkinter import messagebox

def clicked():
    input_txt = txt.get()
    if len(input_txt) != 6:
        messagebox.showerror('Error', 'Длина ключевого слова должна быть 6 символов')
        txt_key = ""
        entry_text.set(txt_key)
        return
    import random
    nabor = list(input_txt)
    a = random.choice(nabor)
    b = random.choice(nabor)
    c = random.choice(nabor)
    d = [str(a), str(b), str(c), ]
    g = random.sample(d, k=3)
    key1 = ''.join(g) + '-'
    a = random.choice(nabor)
    a1 = (ord(a) - 96)%10
    b = random.choice(nabor)
    b1 = (ord(b) - 96)%10
    c = random.choice(nabor)
    c1 = (ord(c) - 96)%10
    d = random.choice(nabor)
    d1 = (ord(d) - 96)%10
    e = random.choice(nabor)
    e1 = (ord(e) - 96)%10
    f = random.choice(nabor)
    f1 = (ord(f) - 96)%10
    d = [str(a1), str(b1), str(c1), str(d1), str(e1), str(f1)]
    g = random.sample(d, k=6)
    key2 = ''.join(g) + '-'
    a = random.choice(nabor)
    b = random.choice(nabor)
    c = random.choice(nabor)
    d = [str(a), str(b), str(c), ]
    g = random.sample(d, k=3)
    key3 = ''.join(g) + '-'
    txt_key = key1 + key2 + key3
    entry_text.set(txt_key)
window = Tk()
window.title("Fortnite Keygen")
window.geometry('400x210')
window.resizable(0, 0)

bg = PhotoImage(file = "bg.png")
bg_lbl = Label(window, image=bg)
bg_lbl.pack()

lbl = Label(window, text="Key word (6 symbols)")
lbl.place(x=0, y=0)
txt = Entry(window,width=6)
txt.focus()
txt.place(x=120, y=0)
btn = Button(window, text="Generate key", command=clicked)
btn.place(x=150, y=0)
lblkey = Label(window, text="Key:")
lblkey.place(x=0, y=25)

entry_text = StringVar()
key = Entry(window,width=16, textvariable=entry_text)
key.place(x=60, y=25)

window.mainloop()
print(key)