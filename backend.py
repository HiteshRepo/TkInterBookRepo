# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 11:59:41 2020

@author: Hitesh Pattanayak
"""

import sqlite3

class Database:
    
#    def connect():
    def __init__(self, db):
        try:
            self.conn = sqlite3.connect(db)
            self.cur = self.conn.cursor()
            self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
            self.conn.commit()
            
        except Exception as e:
            print(e)
            
    def insert(self,title, author, year, isbn):
        try:
            self.cur.execute("INSERT INTO book VALUES (NULL, ?, ?, ?, ?)",(title, author, year, isbn))
            self.conn.commit()
            
        except Exception as e:
            print(e)
            
    def view(self):
        try:
            self.cur.execute("SELECT * FROM book")
            rows=self.cur.fetchall()
            
            return rows
        except Exception as e:
            print(e)
            
    def search(self,title="", author="", year="", isbn=""):
        try:
            self.cur.execute("SELECT * FROM book WHERE title = ? OR author = ? OR year = ? OR isbn = ?", (title, author, year, isbn))
            rows=self.cur.fetchall()
            return rows
        except Exception as e:
            print(e)
            
    def delete(self,id):
        try:
            self.cur.execute("DELETE FROM book WHERE id=?",(id,))
            self.conn.commit()
            
        except Exception as e:
            print(e)
            
    def update(self,id, title, author, year, isbn):
        try:
            self.cur.execute("UPDATE book SET title = ?, author = ?, year = ?, isbn = ? WHERE id=?",(title, author, year, isbn, id))
            self.conn.commit()
            
        except Exception as e:
            print(e)
            
    def __del__(self):
        self.conn.close()
        

    #connect()
    #insert('The Sea', 'John Tablet', 1918, 913123132)
    #insert('The Earth', 'John Smith', 1923, 913123135)
    #print(view())
    #update(2, 'The Mountain', 'John Smooth', 1917, 913123137)
    #print(search(year=1918))
    #delete(1)
    #print(view())
