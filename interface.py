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

def btn_Encode():
    sentence = tb_plainText.get()
    _sentence = vn.preprocess(sentence)          # Tiền xử lí
    _sentence = vn.remove_vn_accent(_sentence)   # Bỏ dấu câu
    ekey = random.randrange(1, 255) # Cho random một key bất kì từ 1 đến 255 để thực hiện Ascii shift cipher
    key.set(ekey)
    _sentence = asciishift.encode(ekey, _sentence)
    cipherText.set(_sentence)
    cb.set(0)
    isChecked()

def btn_decode(sentence):
    tree.delete(*tree.get_children())
    results = asciishift.decode(sentence)
    for result in results:
        if(result[2] > 0):  # Lựa chọn mức độ điểm tương đối, nếu điểm càng cao thì số đề xuất sẽ ít
            tmp = result[1].encode('utf-8').replace(b'\x00', b'\xe2\x96\xa1')
            tree.insert('', 'end', values=(
                str(result[0]), str(tmp, 'utf-8'), str(result[2])))

def vn_sugguest(event):
    for it in tree.selection():
        item = tree.item(it)
        words = item['values'][1].lower()
        try:
            words = words.split()
            k = 5
            vn_results = vn.beam_search(words, k)
            tree1.delete(*tree1.get_children())
            for i in range(0, k):
                tempwrd = (' '.join(vn_results[i][0]))
                tree1.insert('', 'end', values=(
                    str(i+1), str(tempwrd)))
        except:
            tree1.insert('', 'end', values=(''))

def isChecked():
    if cb.get() == 1:
        tb_key.configure(text=key.get())
    if cb.get() == 0:
        tb_key.configure(text='***')

win = Tk()
win.geometry("600x700")
win.resizable(height=FALSE, width=FALSE)
style = ttk.Style()
DEFAULT_FONTSIZE = 14
style.configure("Treeview.Heading", font=("Segue UI", DEFAULT_FONTSIZE))
style.configure("Treeview", font=("Segue UI", DEFAULT_FONTSIZE))

cipherText = StringVar()
key = IntVar()
results = []

#Heading
win.title("ASCII Shift Cipher")
lb_Title = Label(win, text="ASCII Shift Cipher", font=("Segue UI", 24, BOLD))
lb_Title.grid(row=0, column=0, columnspan=2)

#Encode section
lb0 = Label(win, text="Enter a sentence:", font=("Segue UI", DEFAULT_FONTSIZE))
lb0.grid(row=1, column=0, sticky=W, padx=25)

tb_plainText = Entry(win, width=48, font=('Segue UI', DEFAULT_FONTSIZE), justify=CENTER)
tb_plainText.grid(row=2, column=0, columnspan=2, pady=10)

btn0 = Button(win, text='Encrypt (Random Key)', height=2, width=24, command=btn_Encode)
btn0.grid(row=3, column=0, columnspan=2, pady=10)

lb2 = Label(win, text="Encrypt result", font=("Segue UI", DEFAULT_FONTSIZE))
lb2.grid(row=4, column=0, sticky=W, padx=25)

lb_key = Label(win, text="Key:", font=("Segue UI", DEFAULT_FONTSIZE))
lb_key.grid(row=4, column=0, sticky=E)
tb_key = Label(win,text='***', width=4, font=('Segue UI', DEFAULT_FONTSIZE), justify=CENTER)
tb_key.grid(row=4, column=1, sticky=W)

cb = IntVar(value=0)
ckb = Checkbutton(win, text="Show", variable=cb, onvalue=1, offvalue=0, command=isChecked)
ckb.grid(row=4, column=1, sticky=E, padx=20)

lb2_1 = Entry(win, width=48, font=('Segue UI', DEFAULT_FONTSIZE), justify=CENTER, textvariable=cipherText)
lb2_1.grid(row=5, column=0, columnspan=2)

#Decode section
btn3 = Button(win, text='Decrypt', height=2, width=24,
              command=lambda: btn_decode(cipherText.get()))
btn3.grid(row=6, column=0, columnspan=2, pady=10)

lb4 = Label(win, text="Decrypt result(s)", font=("Segue UI", DEFAULT_FONTSIZE))
lb4.grid(row=7, column=0, sticky=SW, padx = 20, pady=10)

tree = ttk.Treeview(win, column=(1, 2, 3), show='headings', height=5)
tree.grid(row=8, column=0, columnspan=2, padx=20)

tree.heading(1, text="Key", anchor=CENTER)
tree.column(1, anchor=CENTER, minwidth=0, width=70)
tree.heading(2, text="Value", anchor=CENTER)
tree.column(2, anchor=CENTER, minwidth=0, width=400)
tree.heading(3, text="Point", anchor=CENTER)
tree.column(3, anchor=CENTER, minwidth=0, width=80)

tree.bind('<ButtonRelease-1>', vn_sugguest)

#Suggest to vietnamese
lb5 = Label(win, text="Vietnamese Word Suggestion", font=("Segue UI", DEFAULT_FONTSIZE))
lb5.grid(row=9, column=0, sticky=SW, padx=15, pady=10)

tree1 = ttk.Treeview(win, column=(1, 2), show='headings', height=5)
tree1.grid(row=10, column=0, columnspan=2, padx=20)
tree1.heading(1, text="Index", anchor=CENTER)
tree1.column(1, anchor=CENTER, minwidth=0, width=70)
tree1.heading(2, text="Result(s)", anchor=CENTER)
tree1.column(2, anchor=CENTER, minwidth=0, width=480)

win.mainloop()
