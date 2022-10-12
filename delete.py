#!/usr/bin/python3
import MySQLdb,cgi,cgitb

def database():
    global conn,curseur
    conn=MySQLdb.connect(user="nasry",passwd="passer",db="revision")
    curseur=conn.cursor()

def delete(id):
    req="delete from etudiant where id=%s"
    database()
    val=(id,)
    curseur.execute(req,val)
    conn.commit()
    print("Content-Type:text/plain")
    print("")
    print("suppression reussi")

form=cgi.FieldStorage()
id=form.getvalue('id')

delete(id)
