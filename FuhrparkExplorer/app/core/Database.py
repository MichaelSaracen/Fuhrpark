from typing import List, Tuple, Any

import mysql.connector
from mysql.connector import MySQLConnection, ProgrammingError

from app.core.Utils import get_db_config


def call_procedures(*callbacks: Any, commit: bool=False):
    """
    Hilf Runnable's Database Transactions durchzuführen.
    Die Callbacks sind die Methoden die, die Queries durchführen.
    Mit commit **True** wird in die Datenbank gespeichert.
    :param callbacks:
    :param commit:
    :return:
    """
    from app.core.Utils import get_db_config
    cfg = get_db_config()
    conn = mysql.connector.connect(
        host=cfg["host"],
        user=cfg["user"],
        password=cfg["password"],
        database=cfg["database"]
    )

    cursor = conn.cursor()
    for callback in callbacks:
        callback(cursor)

    if commit:
        conn.commit()
    cursor.close()
    conn.close()
    

class Database:
    _instance: MySQLConnection|None = None
    # pw: str

    @classmethod
    def check_connection(cls, user: str, pw: str, success_cb, error_cb):
        """
        Überprüft die Verbindung zur Datenbank.

        :param user:
        :param pw:
        :param success_cb:
        :param error_cb:
        :return:
        """
        try:
            mysql.connector.connect(
                host="212.227.60.60",
                user=user,
                password=pw,
                database="fuhrpark"
            )
            success_cb()
            # cls.pw = pw
        except ProgrammingError:
            error_cb()

    @classmethod
    def connection(cls) -> MySQLConnection:
        if cls._instance is None or not cls._instance.is_connected():
            try:
                cfg = get_db_config()
                cls._instance = mysql.connector.connect(
                    host=cfg["host"],
                    user=cfg["user"],
                    password=cfg["password"],
                    database=cfg["database"]
                )
            except Exception as e:
                print(f"Verbindungsfehler: {e}")
        return cls._instance

    @classmethod
    def close(cls):
        conn: MySQLConnection = cls.connection()
        conn.close()

    @classmethod
    def execute(cls, procname: str, values: tuple=()):
        conn = cls.connection()
        cursor = conn.cursor()
        cursor.callproc(procname, values)
        conn.commit()
        cursor.close()
        #conn.close()


    @classmethod
    def call_procedure(cls, procname: str, values: tuple = (), commit: bool=False) -> List[List[Tuple[Any]]]:
        conn = cls.connection()
        cursor = conn.cursor()
        try:
            cursor.callproc(procname, values)
            results = [
                result.fetchall() for result in cursor.stored_results()
            ]
            return results
        except mysql.connector.Error as e:
            print(f"❌ Fehler beim Aufruf von {procname}: {e}")
            return []
        finally:
            if commit:
                conn.commit()
            cursor.close()
            #conn.close()
