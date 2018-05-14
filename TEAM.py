import sqlite3

def create_db():
    import sqlite3
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    table_create_sql = """Create table IF Not exists todo (
                id integer primary key autoincrement,
                category text not null,
                what text not null,
                due text not null,
                finished integer);"""

    cur.execute(table_create_sql)
    
def run_program():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()
    
    while True:
        act = input("Choose what to do: \n (a: Add todo, l: List todo, m: Modify todo, d: Delete todo, q: Quit)?")
        if act == "a":
            add_todo()
        elif act == "l":
            list_todo()
        elif act == "m":
            modify_todo()
        elif act == "d":
            delete_todo()
        elif act == "q":
            break
        
def list_todo():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    sql = "select* from todo where 1"
    cur.execute(sql)
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

def finishlist_todo():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    sql = "select * from todo where finished == 1 "
    cur.execute(sql)
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

def unfinishlist_todo():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    sql = "select * from todo where finished == 0 "
    cur.execute(sql)
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

def categorylist_todo():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    CatIn = input("Input Category that you want look: ")
    sql = "select * from todo where category == "+CatIn+" "
    cur.execute(sql)
    
    rows = cur.fetchall()
    for row in rows:
        print(row)

def add_todo():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()

    CatIn = input("Category? ")
    WhatIn = input("Todo? ")
    DueIn = input("Due date? ")

    sql = "insert into todo (category, what, due, finished) values ('"+CatIn+"','"+WhatIn+"','"+DueIn+"','0')"

    cur.execute(sql)
    conn.commit()
    
    sql = "select  * from todo where 1"
    cur.execute(sql)

def modify_todo():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()
    
    list_todo()
    
    sql = "select * from todo where ?"
    
    IDIn = input("Record id? ")
    CatIn = input("Category? ")
    WhatIn = input("Todo? ")
    DueIn = input("Due date? ")
    while True:
        FinishIn = input("Finished (1: yes, 0: no)? ")
        if FinishIn == "0" or FinishIn == "1":
            break
        
    sql = "update todo set category='"+CatIn+"', what='"+WhatIn+"', due='"+DueIn+"', finished='"+FinishIn+"' where id == "+IDIn+""
    cur.execute(sql)
    conn.commit()
    
def delete_todo():
    conn = sqlite3.connect("lab.db")
    cur = conn.cursor()
    
    list_todo()

    sql = "select * from todo where ?"
    
    IDIn = input("Record id? ")
    sql = "delete from todo where id == "+IDIn+""
    cur.execute(sql)
    conn.commit()

if __name__ == "__main__":
    create_db()
    run_program()
