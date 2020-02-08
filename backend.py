# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:59:41 2020

@author: Hitesh Pattanayak
"""

import sqlite3

def connect():
    try:
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        
def insert(title, author, year, isbn):
    try:
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",(title, author, year, isbn))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        
def view():
    try:
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book")
        rows=cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(e)
        
def search(title="", author="", year="", isbn=""):
    try:
        conn = sqlite3.connect("books.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
        rows=cur.fetchall()
        conn.close()
        return rows
    except Exception as e:
        print(e)
        
def delete(id):
    try:
        conn = sqlite3.connect("books.db")
        cur=conn.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        
def update(id, title, author, year, isbn):
    try:
        conn = sqlite3.connect("books.db")
        cur = conn.cursor() 
        cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id=?",(title, author, year, isbn, id))
        conn.commit()
        conn.close()
    except Exception as e:
        print(e)
        

connect()
#insert('The Sea', 'John Tablet', 1918, 913123132)
#insert('The Earth', 'John Smith', 1923, 913123135)
#print(view())
#update(2, 'The Mountain', 'John Smooth', 1917, 913123137)
#print(search(year=1918))
#delete(1)
#print(view())
