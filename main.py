import sqlite3
from colorama import init, Fore, Style

init(convert=True)

is_login = 0
current_id = 0
data = []

def mainmenu_pre_login():
    create_login_db()

    while True:
        print(Fore.CYAN + """
          ***   *                    *         *   *  *
         *   *  *                    *         *   *  *
        *       ****    ***    ***   *  *      *  *** *
        *       *   *  *   *  *   *  * *       *   *  *
        *       *   *  *****  *      **        *   *  *
        *       *   *  *      *      **        *   *  *
         *   *  *   *  *   *  *   *  * *       *   *   
          ***   *   *   ***    ***   *  *      *   ** *
        """ + Style.RESET_ALL + "https://github.com/OSS-A-1/SQLiteDB\n")

        print("[0] 로그인")
        print("[1] 가입")
        print("[2] 종료")
        print("[3] 가입된 아이디 비밀번호 보기(테스트용)")
        cho = input(">> ")

        while (not cho.isdigit()) or (cho.isdigit() and not (0 <= int(cho) <= 3)):
            print(Fore.RED + "\n0 ~ 2 사이의 숫자만을 입력해야 합니다." + Style.RESET_ALL)
            cho = input(">> ")

        cho = int(cho)
        print()

        if cho == 0:
            login()
        elif cho == 1:
            register()
        elif cho == 2:
            return
        elif cho == 3:
            list_user()
        if is_login == 1:
            mainmenu_aft_login()
            return

def mainmenu_aft_login():
    while True:
        print("\n메인메뉴\n")
        print("[0] 할일 보기")
        print("[1] 할일 추가")
        print("[2] 할일 수정")
        print("[3] 할일 삭제")
        print("[4] 할일 정렬")
        print("[5] 사용자 정보 보기")
        print("[6] 프로그램 정보 보기")
        print("[7] 종료")
        cho = input(">> ")

        while (not cho.isdigit()) or (cho.isdigit() and not (0 <= int(cho) <= 7)):
            print(Fore.RED + "\n0 ~ 7 사이의 숫자만을 입력해야 합니다." + Style.RESET_ALL)
            cho = input(">> ")

        cho = int(cho)
        print()

        if cho == 0:
            print("할일 보기 함수 실행")
        elif cho == 1:
            print("할일 추가 함수 실행")
        elif cho == 2:
            print("할일 수정 함수 실행")
        elif cho == 3:
            print("할일 삭제 함수 실행")
        elif cho == 4:
            print("할일 정렬 함수 실행")
        elif cho == 5:
            user_info()
            return
        elif cho == 6:
            program_info()
        elif cho == 7:
            return

def logout():
    global current_id, is_login
    is_login = 0
    current_id = 0
    mainmenu_pre_login()

def user_info():
    while True:
        print("사용자 정보")
        print("현재 사용자 : {0}".format(data[1]))
        print("[0] 로그아웃")
        print("[1] 비밀번호 변경")
        print("[2] 취소")
        cho = input(">> ")

        while (not cho.isdigit()) or (cho.isdigit() and not (0 <= int(cho) <= 2)):
            print(Fore.RED + "\n0 ~ 2 사이의 숫자만을 입력해야 합니다." + Style.RESET_ALL)
            cho = input(">> ")

        cho = int(cho)

        if cho == 0:
            logout()
            return
        elif cho == 1:
            change_pw()
        elif cho == 2:
            mainmenu_aft_login()
            return

def change_pw():
    conn = sqlite3.connect("user_data.db")
    cur = conn.cursor()

    sql = "select * from user_data where 1"
    cur.execute(sql)

    print("\n비밀번호 변경")
    print("[0] 취소\n")

    while True:
        print("현재 비밀번호 입력")
        pw = input("PW >> ")

        if pw == '0':
            conn.close()
            return

        if data[2] == pw:
            break
        else:
            print(Fore.RED + "\n비밀번호를 다시 확인해 주세요\n")
            print("비밀번호가 잘못 입력되었습니다.\n" + Style.RESET_ALL)
            continue

    print("\n변경할 비밀번호 입력")
    ch_pw = input("PW >> ")

    if ch_pw == '0':
        conn.close()
        return

    while not (4 <= len(ch_pw) <= 20):
        print(Fore.RED + "\n4 ~ 20 자 사이로 입력해 주십시오." + Style.RESET_ALL)
        ch_pw = input("PW >> ")

    print("\n비밀번호 확인")
    con_pw = input("PW >> ")

    if con_pw == '0':
        conn.close()
        return

    while ch_pw != con_pw:
        print(Fore.RED + "\n비밀번호를 잘못 입력하셨습니다." + Style.RESET_ALL)
        con_pw = input("PW >> ")

    cur.execute("UPDATE user_data SET pw = ? WHERE id = ? ",
                (ch_pw, current_id))
    conn.commit()

    print()

    conn.close()

def program_info():
    print("프로그램 이름 : Check It!")
    print("깃 허브 주소 : https://github.com/OSS-A-1/SQLiteDB")

def list_user():
    conn = sqlite3.connect("user_data.db")
    cur = conn.cursor()

    sql = "select * from user_data where 1"
    cur.execute(sql)

    rows = cur.fetchall()

    print()
    for row in rows:
        list(row)
        for val in row:
            print(val, end=" ")
        print()
    print()

    conn.close()

def login():
    conn = sqlite3.connect("user_data.db")
    cur = conn.cursor()

    sql = "select * from user_data where 1"
    cur.execute(sql)

    rows = cur.fetchall()

    global data

    cor_id = 0
    data = []

    print("로그인"
          "\n[0] 로그인 취소\n")

    while True:
        id = input("ID >> ")

        if id == '0':
            conn.close()
            return

        for row in rows:
            list(row)
            if row[1] == id:
                data = row
                cor_id = 1
                break

        if cor_id == 0:
            print(Fore.RED + "아이디를 다시 확인하세요.\n"
                  "아이디를 잘못 입력하셨거나 등록되지 않은 아이디 입니다.\n" + Style.RESET_ALL)
            continue
        elif cor_id == 1:
            break

    while True:
        pw = input("PW >> ")

        if pw == '0':
            conn.close()
            return

        if data[2] == pw:
            print("\n로그인 성공")
            global is_login, current_id
            current_id = id
            is_login = 1
            conn.close()
            return
        else:
            print(Fore.RED + "비밀번호를 다시 확인하세요.\n"
                  "비밀번호를 잘못 입력하셨습니다.\n" + Style.RESET_ALL)
            continue

def register():
    conn = sqlite3.connect("user_data.db")
    cur = conn.cursor()

    sql = "select * from user_data where 1"
    cur.execute(sql)

    rows = cur.fetchall()

    cor_id = 0

    print("\n가입"
          "\n[0] 가입 취소\n")

    while True:
        val_id = input("ID >> ")

        if val_id == '0':
            conn.close()
            return

        while not (4 <= len(val_id) <= 20):
            print(Fore.RED + "\n4 ~ 20 자 사이로 입력해 주십시오." + Style.RESET_ALL)
            val_id = input("ID >> ")

        for row in rows:
            list(row)
            if row[1] == val_id:
                cor_id = 1
                break

        if cor_id == 1:
            print(Fore.RED + "이미 존재하는 아이디 입니다.\n"
                  "다시 입력해 주십시오.\n" + Style.RESET_ALL)
            cor_id = 0
            continue
        elif cor_id == 0:
            break

    val_pw = input("PW >> ")

    if val_pw == '0':
        conn.close()
        return

    while not (4 <= len(val_pw) <= 20):
        print(Fore.RED + "\n4 ~ 20 자 사이로 입력해 주십시오." + Style.RESET_ALL)
        val_pw = input("ID >> ")

    print("비밀번호 확인")
    con_pw = input("PW >> ")

    if con_pw == '0':
        conn.close()
        return

    while val_pw != con_pw:
        print(Fore.RED + "비밀번호를 잘못 입력하셨습니다.\n" + Style.RESET_ALL)
        con_pw = input("PW >> ")

    cur.execute("insert into user_data (id, pw) values (?, ?)",
                (val_id, val_pw))
    conn.commit()

    conn.close()

def create_login_db():
    conn = sqlite3.connect("user_data.db")
    cur = conn.cursor()

    table_create_sql = """create table if not exists user_data (
                                num integer primary key autoincrement,
                                id text not null,
                                pw text not null);"""

    cur.execute(table_create_sql)

    cur.close()

if __name__ == "__main__":
    mainmenu_pre_login()
