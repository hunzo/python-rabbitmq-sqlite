import sqlite3
import logging

DB_PATH = "db/db.sqlite"

def create_db():
    try:
        with sqlite3.connect(DB_PATH) as con:
            sql_cmd = """
                CREATE TABLE person(
                    id integer PRIMARY KEY AUTOINCREMENT,
                    cardid text,
                    studentname text,
                    studentid text,
                    studentaccount text,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            """
            con.execute(sql_cmd)
            ret = {
                "status": "success"
            }
            return ret
    except Exception as e:
        return {
            "status": "error",
            "info": f"error create_db : {e}"
        }

def insert_db(params):
    try:
        with sqlite3.connect(DB_PATH) as con:
            sql_cmd = f"""
                INSERT INTO person(
                    cardid,
                    studentname,
                    studentid,
                    studentaccount
                ) values (?, ?, ?, ?)
            """
            con.execute(sql_cmd, params)
            return {
                "status": "success",
                "data": params
            }
    except Exception as e:
        return {
            "status": "error",
            "info": f"error insert_db: {e}"
        }

def select_db():
    try:
        with sqlite3.connect(DB_PATH) as con:
            con.row_factory = sqlite3.Row
            sql_cmd = f"""
                SELECT
                id,
                studentname,
                studentid,
                studentaccount,
                cardid,
                datetime(timestamp, 'localtime')
                from 
                person
            """
            result = []
            for row in con.execute(sql_cmd):
                temp = {
                    "id": row["id"],
                    "cardid": row["cardid"],
                    "studentname": row["studentname"],
                    "studentid": row["studentid"],
                    "studentaccount": row["studentaccount"],
                }
                result.append(temp)
            # print(result) 
            return result

    except Exception as e:
        return {
            "status": "error",
            "info": f"error select_db: {e}"
        }


def delete_db(id):
    try:
        with sqlite3.connect(DB_PATH) as con:
            sql_cmd = f"""
                DELETE FROM person WHERE id = '{id}'
            """
            con.execute(sql_cmd)
            return {
                "status": "success",
                "info": f"delete id: {id}"
            }

    except Exception as e:
        return {
            "status": "error",
            "info": f"error delete_db: {e}"
        }


def drop_table():
    try:
        with sqlite3.connect(DB_PATH) as con:
            sql_cmd = f"""
                DROP TABLE person
            """
            con.execute(sql_cmd)
            return {
                "status": "success",
                "info": "drop table person success"
            }

    except Exception as e:
        return {
            "status": "error",
            "info": f"error drop_table: {e}"
        }

