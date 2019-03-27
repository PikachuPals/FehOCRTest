import sqlite3
from sqlite3 import Error
from values import listOut

def connection(db_feh):
    try:
        conn = sqlite3.connect(db_feh, isolation_level=None)
        return conn
    except Error as e:
        print(e)
        return conn

def conncursor(db_feh):
    db = connection(db_feh)
    cursor = db.cursor()
    return cursor

def tablecreate(db_feh):
    db = connection(db_feh)
    cursor = conncursor(db_feh)
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS heroes(Id INTEGER PRIMARY KEY, Title TEXT, Name TEXT,
    Level TEXT, HP TEXT, Atk TEXT, Spd TEXT, Def TEXT, Res TEXT, SP TEXT, Weapon TEXT, Assist TEXT,
    Special TEXT, SkillA TEXT, SkillB TEXT, SkillC TEXT,Hidden INTEGER);
    ''')

def insertlist(output):
    db_feh = "fehdatabase.db"
    db = connection(db_feh)
    cursor = conncursor(db_feh)
    sql = ''' INSERT INTO heroes(Id,Title,Name,Level,HP,Atk,Spd,Def,Res,SP,Weapon,Assist,Special,SkillA,SkillB,SkillC,Hidden)
    Values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''
    cursor.execute(sql, output)

tablecreate("fehdatabase.db")

