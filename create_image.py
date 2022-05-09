#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-


import sqlite3, random


def main() -> None:
    global rnd
    rnd = str(random.randint(1, 10243))
    con = sqlite3.connect("./jomle.sqlite")
    cur = con.cursor()
    cur.execute("SELECT * FROM jomle WHERE Id= '%s'" % rnd)
    db = cur.fetchall()
    esm = db[0][1]
    matn = db[0][2]
    con.close()
    html_text = f"""
<!DOCTYPE html>
<html dir="rtl" lang="en">
<head>
    <meta charset="UTF-8">
    <title>insta_story</title>
    <link rel="stylesheet" href="./style.css">
</head>
<body>
    <div class="row" id="ck">
        <img id="img-id" class="row" src="./story_theme.jpg" alt="Error Load Image">
        <div class="bottom">{esm}</div>
        <div class="text">{matn}</div>
    </div>
</body>
</html>
    """
    with open("./format/index.html", "w") as index:
        index.write(html_text)
        index.close()


if __name__ == "__main__":
    main()
    rnd = rnd
