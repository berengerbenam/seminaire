#!/usr/bin/python3
import MySQLdb

def database():
    global conn,curseur
    conn=MySQLdb.connect(user="nasry",passwd="passer",db="revision")
    curseur=conn.cursor()

def affiche():
    req="select * from etudiant"
    database()
    curseur.execute(req)
    print("Content-Type:text/html")
    print("")
    print("<body><table border='1px'><tr><td>nom</td><td>prenom</td><td>note</td></tr>")
    for row in curseur.fetchall():
        print(f"<tr><td>{row[1]}</td><td>{row[2]}</td><td>{row[3]}</td></tr>")
    print("</table></body>")

affiche()
