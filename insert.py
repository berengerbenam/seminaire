#!/usr/bin/python3
import MySQLdb,cgi,cgitb

def database():
    global conn,curseur
    conn=MySQLdb.connect(user="nasry",passwd="passer",db="revision")
    curseur=conn.cursor()

def insertion(nom,prenom,note):
    req="insert into etudiant(nom,prenom,note) values(%s,%s,%s)"
    database()
    val=(nom,prenom,note)
    curseur.execute(req,val)
    conn.commit()
    print("Content-Type:text/plain")
    print("")
    print("insertion reussi")

form=cgi.FieldStorage()
nom=form.getvalue('nom')
prenom=form.getvalue('prenom')
note=form.getvalue('note')

insertion(nom,prenom,note)
