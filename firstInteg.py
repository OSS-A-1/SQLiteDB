import sqlite3
import datetime

def create_db():
    import sqlite3
    conn = sqlite3.connect("DataBase.db")
    cur = conn.cursor()

    table_create_sql = """Create table IF Not exists todo (
                id integer primary key autoincrement,
                importance text not null,
                finished text not null,
                due date not null,
                category text not null,
                what text not null);"""
    cur.execute(table_create_sql)

conn = sqlite3.connect("DataBase.db")
cur = conn.cursor()

# main program

def run_program():
    while True:
        act = input("Choose what to do: \n (a: Add Todo, l : List todo, m: Modify todo, d: Delete todo, q: Quit)?")
        if act == "a":
            add_todo()
        elif act == "l":
            list_todo()
        elif act == "m":
            modify_todo()
        elif act == "d":
            remove_todo()
        elif act == "q":
            break

# ADD

def add_todo():
    catin = input("Category: ")
    whatin = input("To do: ")
    duein = input("Due Date: ")
    while True:
        impin = input("Importance(Y or N): ")
        if impin == "y":
            imp = "★"
            break
        elif impin == "n":
            imp = "  "
            break
    finin = "×"
    sql = "insert into todo (importance, finished, due, category, what) values ('"+imp+"', '"+finin+"', '"+duein+"', '"+catin+"', '"+whatin+"')"

    cur.execute(sql)
    conn.commit()

    sql = "select * from todo where 1"
    cur.execute(sql)

# LIST
        
def list_todo():
    while True:
        act = input("Filter(a: All, i: Important, ni: Nonimportant, \n f: Finished, nf: Nonfinished, c: Category, q: Quit): ")
        if act == "a":
            list_all()
            break
        elif act == "f":
            list_finish()
            break
        elif act == "nf":
            list_nonfinish()
            break
        elif act == "i":
            list_important()
            break
        elif act == "ni":
            list_nonimportant()
            break
        elif act == "c":
            list_category()
            break
        elif act == "q":
            break

# List-SubFunction

def list_all():
    sql = "select * from todo where 1"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def list_finish():
    sql = "select * from todo where finished == '○'"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def list_nonfinish():
    sql = "select * from todo where finished == '×'"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def list_category():
    Catin = input("Input Category: ")
    sql = "select * from todo where category == '"+Catin+"'"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

def list_important():
    sql = "select * from todo where importance == '★'"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)
        
def list_nonimportant():
    sql = "select * from todo where importance == '  '"
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)

# MODIFY

def modify_todo():

    list_todo()

    sql = "select * from todo where ?"

    idin = input("Record ID: ")

    catin = input("Category: ")
    whatin = input("To do: ")
    duein = input("Due Date: ")
    while True:
        impin = input("Importance(Y or N): ")
        if impin == "y":
            imp = "★"
            break
        elif impin == "n":
            imp = "  "
            break
    while True:
        finin = input("Finished(Y or N)?: ")
        if finin == "y":
            fin = "○"
            break
        elif finin == "n":
            fin = "×"
            break

    sql = "update todo set importance='"+imp+"', finished='"+fin+"', due='"+duein+"', category='"+catin+"', what='"+whatin+"' where id == "+idin+""
    cur.execute(sql)
    conn.commit()

# DELETE

def remove_todo():

    list_todo()

    sql = "select * from todo where ?"

    idin = input("Record ID: ")
    sql = "delete from todo where id == "+idin+""
    cur.execute(sql)
    conn.commit()

# Activate
if __name__ == "__main__":
    create_db()
    run_program()
