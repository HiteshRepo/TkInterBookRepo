# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:40:41 2020

@author: Hitesh Pattanayak


A program that stores these book information:
    Title, Author,
    Year and ISBN
    
User can do below operations:
    View all records
    Add an entry
    Search an entry
    update an entry
    delete an entry
    close
"""

from tkinter import *
import backend


def getSelectedRow(event):
    try:
        global selected_row
        index=list1.curselection()
        selected_row = list1.get(index)
        
        e1.delete(0, END)
        e1.insert(END, selected_row[1])
        
        e2.delete(0, END)
        e2.insert(END, selected_row[2])
        
        e3.delete(0, END)
        e3.insert(END, selected_row[3])
        
        e4.delete(0, END)
        e4.insert(END, selected_row[4])
        
#        return (selected_row)
        
    except Exception as e:
        print(e)

def view_command():
    try:
        list1.delete(0,END)
        for row in backend.view():
            list1.insert(END, row)
    except Exception as e:
        print(e)

def search_command():
    try:
        list1.delete(0,END)
        for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
            list1.insert(END, row)
    except Exception as e:
        print(e)

def add_command():
    try:
        backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
#        view_command()
        list1.delete(0,END)
        list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    except Exception as e:
        print(e)
        
def delete_command():
    try:
        backend.delete(selected_row[0])
        view_command()
    except Exception as e:
        print(e)
        
def update_command():
    try:
        backend.update(selected_row[0],title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
        view_command()
    except Exception as e:
        print(e)




window = Tk()
window.wm_title("Book Store")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

title_text = StringVar()
e1 = Entry(window, text=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, text=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, text=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, text=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2) 
list1.bind('<<ListboxSelect>>', getSelectedRow)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1 = Button(window, text="View All", width=12, command=view_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Search Entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Add Entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)



window.mainloop()

