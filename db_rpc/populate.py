import names
import uuid
import sqlite3
import random

db_path = "db/testdb.sqlite"

def create_db():
    try:
        with sqlite3.connect(db_path) as con:
            sql_cmd = """
                CREATE TABLE person(
                    id integer PRIMARY KEY AUTOINCREMENT,
                    cardid text,
                    studentname text,
                    studentid text,
                    studentaccount text,
                    room text,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """
            con.execute(sql_cmd)
            print('Create table success !!!')
    except Exception as e:
        print(f'Error -> : {e}')
        exit()

def insert_db(params):
    try:
        with sqlite3.connect(db_path) as con:
            sql_cmd = f"""
                INSERT INTO person(
                    cardid,
                    studentname,
                    studentid,
                    studentaccount,
                    room
                ) values (?, ?, ?, ?, ?)
            """
            con.execute(sql_cmd, params)
            print(f'Insert: {params} , success !!!')
    except Exception as e:
        print(f'Error -> : {e}')
        exit()
        


def popData(size):
    rooms = [
        "room1",
        "room2",
        "room3",
        "room4",
        "room5",
    ]

    create_db()
    for i in range(1, size):
        fname = names.get_first_name()
        lname = names.get_last_name()
        fullname = f"{fname} {lname}"
        account = f"{str(fname).lower()}@email.com"
        cardid = uuid.uuid4().hex
        studentid = str(uuid.uuid4())
        room = random.choice(rooms)
        
        params = [
            cardid,
            fullname,
            studentid,
            account,
            room
        ]
        insert_db(params)

if __name__ == '__main__':
    popData(100)
        
