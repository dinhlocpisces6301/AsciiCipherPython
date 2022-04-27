from cProfile import label
from enum import auto
from inspect import trace
from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD, ITALIC
from turtle import color
from setuptools import Command
import asciishift
import vietnameseaccent as vn
import vnchar
import random

def btn_start():
    sentence = tbword.get()
    sentence = vn.preprocess(sentence)          # Tiền xử lí
    _sentence = vn.remove_vn_accent(sentence)   # Bỏ dấu câu
    ekey = random.randrange(1, 255) # Cho random một key bất kì từ 1 đến 255 để thực hiện Ascii shift cipher
    _sentence = asciishift.encode(ekey, _sentence)
    encodeRes.set(_sentence)

def btn_decode(_sentence):
    tree.delete(*tree.get_children())
    results = asciishift.decode(_sentence)
    length = len(_sentence)
    index = 0
    for result in results:
        index += 1
        # Chấm điểm dựa trên nhóm ký tự phổ biến của Tiếng Việt
        point = vnchar.checkSentence(result.lower())
        if(point > length/4):  # Lựa chọn mức độ điểm tương đối, nếu điểm càng cao thì số đề xuất sẽ ít
            tree.insert('', 'end', values=(
                str(index), str(result), str(point)))

win = Tk()
win.geometry("600x700")
win.resizable(height=FALSE, width=FALSE)
tree = ttk.Treeview(win, column=(1, 2, 3), show='headings', height=5)
style = ttk.Style()
style.configure("Treeview.Heading", font=("Segue UI", 12))

encodeRes = StringVar()

win.title("ASCII Shift Cipher")

lbTitle = Label(win, text="ASCII Shift Cipher", font=("Segue UI", 24, BOLD))
lbTitle.grid(row=0, column=0, columnspan=2)
# section1
lb0 = Label(win, text="Enter a sentence:", font=("Segue UI", 14))
lb0.grid(row=1, column=0, sticky=W, padx = 20)

tbword = Entry(win, width=48, font=('Segue UI', 14), justify=CENTER)
tbword.grid(row=2, column=0, columnspan=2, pady=10)

btn0 = Button(win, text='Encrypt (Random Key)', height=2, command=btn_start)
btn0.grid(row=3, column=0, columnspan=2, pady=10)

# encode section
lb2 = Label(win, text="Encrypt result:", font=("Segue UI", 14))
lb2.grid(row=4, column=0, columnspan=2)
lb2_1 = Label(win, font=("Segue UI", 14), textvariable=encodeRes)
lb2_1.grid(row=5, column=0, columnspan=2)


# decode section
lb4 = Label(win, text="Decrypt result(s)", font=("Segue UI", 14))
lb4.grid(row=6, column=0, sticky=W, padx = 20, pady = 10)

# encode section - List View
tree = ttk.Treeview(win, column=(1, 2, 3), show='headings', height=5)
tree.grid(row=7, column=0, columnspan=2, pady=10, padx = 20)

tree.heading(1, text="Key", anchor=CENTER)
tree.column(1, anchor=CENTER, minwidth=0, width=70)
tree.heading(2, text="Value", anchor=CENTER)
tree.column(2, anchor=CENTER, minwidth=0, width=400)
tree.heading(3, text="Point", anchor=CENTER)
tree.column(3, anchor=CENTER, minwidth=0, width=80)

def vn_sugguest(event):
    for it in tree.selection():
        item = tree.item(it)
        words = item['values'][1]
        try:
            words = words.split()
            k = 3
            vn_results = vn.beam_search(words, k)
            tree1.delete(*tree1.get_children())

            for i in range(0, k):
                tempwrd = (' '.join(vn_results[i][0]))
                tree1.insert('', 'end', values=(
                    str(i+1), str(tempwrd)))
        except:
            tree1.insert('', 'end', values=(''))

tree.bind('<ButtonRelease-1>', vn_sugguest)

btn3 = Button(win, text='Decrypt', height=2,
              command=lambda: btn_decode(str(lb2_1['text'])))
btn3.grid(row=8, column=0, columnspan=2, pady=10)

# suggest to vietnamese
lb5 = Label(win, text="Vietnamese word suggestion", font=("Segue UI", 14))
lb5.grid(row=9, column=0, sticky=W, padx = 15)

tree1 = ttk.Treeview(win, column=(1, 2), show='headings', height=5)
tree1.grid(row=10, column=0, columnspan=2, pady=10, padx = 20)
tree1.heading(1, text="Index", anchor=CENTER)
tree1.column(1, anchor=CENTER, minwidth=0, width=70)
tree1.heading(2, text="Result(s)", anchor=CENTER)
tree1.column(2, anchor=CENTER, minwidth=0, width=480)

win.mainloop()
