#!/usr/bin/python3
import MySQLdb,cgi,cgitb

def database():
    global conn,curseur
    conn=MySQLdb.connect(user="nasry",passwd="passer",db="revision")
    curseur=conn.cursor()

def update(id,note):
    req="update etudiant set note=%s where id=%s"
    database()
    val=(note,id)
    curseur.execute(req,val)
    conn.commit()
    print("Content-Type:text/plain")
    print("")
    print("mis a jour reussi")

form=cgi.FieldStorage()
id=form.getvalue('id')
note=form.getvalue('note')

update(id,note)
