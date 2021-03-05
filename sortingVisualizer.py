import tkinter as tk
import random as rand
import time
import sys


def init_rect_dict():
    for i in range(N):
        h = rand.randint(0,550)
        height_list.append(h)
    global is_sorted
    update()

def _shuffle():
    global height_list
    height_list = []
    canvas.delete("all")
    for i in range(N):
        h = rand.randint(0,550)
        height_list.append(h)
        x1 = 1000//N * (i + .5)
        y1 = 800
        x2 = 1000//N * (i + 1.5)
        y2 = height_list[i]
        canvas.create_rectangle(x1, y1, x2, y2, fill=color_list[i], outline='white')
        yield
    global is_sorted

def update():
    canvas.delete("all")
    for i in range(N):
        x1 = 1000//N * (i + .5)
        y1 = 800
        x2 = 1000//N * (i + 1.5)
        y2 = height_list[i]
        canvas.create_rectangle(x1, y1, x2, y2, fill=color_list[i], outline='white')

def bubble_sort():
    n = len(height_list)
    for i in range(n):
        for j in range(0, n-i-1):
            h1 = height_list[j]
            h2 = height_list[j+1]
            if h1 < h2:
                height_list[j] = h2
                height_list[j+1] = h1
            color_list[j+1] = 'red'
            update()
            color_list[j+1] = 'black'
            yield
    global is_sorted

def sort():
    global func
    global is_sorted
    try:
        next(func)
        canvas.after(1, sort)    
    except StopIteration:            
        update()
        is_sorted = True
    finally:
        canvas.after_cancel(sort)


def shuffle():
    global shuff
    global is_sorted
    try:
        next(shuff)
        canvas.after(1, shuffle)
    except StopIteration:
        is_sorted = False
    finally:
        canvas.after_cancel(shuffle)

def main():
    root = tk.Tk()
    w = tk.Frame(root, height = 750, width=1005)
    w.pack()
    w.grid(row=0, column=0, padx=10, pady=5)
    global canvas
    canvas = tk.Canvas(root, width=1005, height=550)
    canvas.grid(row=1, column=0, padx=10, pady=5)

    global is_sorted
    is_sorted = False

    global N
    N = 50
    global height_list
    height_list = list()
    global color_list
    color_list = ['black' for i in range(N)]

    global shuff
    shuff = _shuffle()

    # alg_label = tk.Label(w, text="Algorithm", font="comic")
    # alg_label.grid(row=0, column=1, padx=10, pady=5)
    # alg_select = tk.Listbox(w, selectmode='single', height=2, bg='light blue', font="comic")
    # alg_select.insert(0, "Bubble Sort")
    # alg_select.insert(1, "Merge Sort")
    # alg_select.grid(row=1, column=1, padx=10, pady=5)
    
    # shuffle_but = tk.Button(w, text='Shuffle', bg='light grey', font='comic', command=shuffle)
    # shuffle_but.grid(row=1, column=0, padx=5, pady=5)
    sort_but = tk.Button(w, text='Sort', bg='light grey', font='comic', command=sort)
    sort_but.grid(row=2, column=0, padx=5, pady=5)





    

    init_rect_dict()
    global func
    func = bubble_sort()
    canvas.mainloop()

main()






