#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-
import sqlite3
from time import sleep


def main() -> None:
    connection = sqlite3.connect("./jomle.sqlite")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS jomle
              (Id INTEGER, Esm TEXT, Matn TEXT)"""
    )
    connection.commit()
    connection.close()
    sleep(1)
    with open("./jomle_txt/esm.txt", "r") as esm:
        esm_line = esm.readlines()
        esm.close()
    sleep(1)
    with open("./jomle_txt/matn.txt", "r") as matn:
        matn_line = matn.readlines()
        matn.close()
    sleep(1)
    con = sqlite3.connect("./jomle.sqlite")
    cur = con.cursor()
    for i in range(len(matn_line)):
        cur.execute(
            f"INSERT INTO jomle VALUES ({i+1},'{esm_line[i]}','{matn_line[i]}')"
        )
        con.commit()
    con.close()
    print('tamam...')

if __name__ == "__main__":
    main()
