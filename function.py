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
            u = ''
            while u not in ['a','f','uf','i','ui','c','q']:
                u = input("What items are you looking at (a: All, f: Finished only, uf : Unfinished only,\n i: Important only, ui: unimportant only, c: category, q: break) :")
                if u == 'q':
                    break
                elif u in ['a','f','uf','i','ui','c']:
                    filter_todo(filter=u)
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

def filter_todo(filter):
    sql = "select * from todo where 1"
    cur.execute(sql)
    
    rows = cur.fetchall()

    data = []

    if filter == 'a':
        for row in rows:
            data.append(row)
    elif filter == 'f':
        for row in rows:
            if row[2] == "○":
                data.append(row)
    elif filter == 'uf':
        for row in rows:
            if row[2] == "×":
                data.append(row)
    elif filter == 'i':
        for row in rows:
            if row[1] == "★":
                data.append(row)
    elif filter == 'ui':
        for row in rows:
            if row[1] == "  ":
                data.append(row)
    elif filter == 'c':
        ci = input("Category?: ")
        for row in rows:
            if row[4] == ci:
                data.append(row)         
    list_todo(data)
    return data
        
def list_todo(data):
    print(data)

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
