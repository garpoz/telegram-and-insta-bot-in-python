#! /usr/bin/python3
# behrouz_ashraf
# garpozir@gmail.com
# -*- coding: utf-8 -*-


import sqlite3, random, glob


def main() -> None:
    global rnd, noe
    while True:
        print("1)rooz")
        print("2)shab")
        noe = input("1 ya 2: ")
        if noe in ("12") and len(noe) == 1:
            break
    if noe == "1":
        noe = "roze"
    else:
        noe = "shab"
    rnd_png = glob.glob(f"./format/{noe}*.png")
    rnd_png = random.choice(rnd_png)
    rnd_png = rnd_png.replace("format/", "")
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
        <img id="img-id" class="row" src="{rnd_png}" alt="Error Load Image">
        <div class="bottom">{esm}</div>
        <div class="text">{matn}</div>
    </div>
</body>
</html>
    """
    with open("./format/index.html", "w", encoding="utf8") as index:
        index.write(html_text)
        index.close()


if __name__ == "__main__":
    main()
    rnd = rnd
    noe = noe
