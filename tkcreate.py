from flask import Flask, request, render_template, session,redirect,url_for
from datetime import datetime , date,time,timedelta
import sqlite3
from Crypto.Cipher import AES
from binascii import b2a_hex,a2b_hex
import random
import traceback
import importlib
def encrypt(text,key):
    key=key+'\0'*(16-len(key)%16)
    cryptor=AES.new(key.encode('utf-8'),AES.MODE_CBC,key.encode('utf-8'))
    text=text+'\0'*(16-len(text.encode("utf-8"))%16)
    try:return b2a_hex(cryptor.encrypt(text.encode('utf-8'))).decode('utf-8')
    except:
        traceback.print_exc()
        return "ERROR"
def decrypt(text,key):
    key=key+'\0'*(16-len(key)%16)
    cryptor=AES.new(key.encode('utf-8'),AES.MODE_CBC,key.encode('utf-8'))
    try:return cryptor.decrypt(a2b_hex(text.encode('utf-8'))).decode('utf-8').rstrip('\0')
    except:return "ERROR"

base=input("请输入数据库文件名：")
conn=sqlite3.connect(base)
cursor=conn.cursor()
tk=input("请输入题库文件名")
sheet=input("请输入表名")
with open(tk,'r',encoding='gbk') as tkf:
    text=tkf.read()
    for each in text.split("|||||"):
        print(each.find("["),each.find("]"))
        a=each[each.find("["):each.find("]")+1]
        print(a[a.find("（")+1:a.find("）")])
        print(each.replace(a,"（   ）"))
        try:cursor.execute("insert into "+sheet+" (question,answer,scorecalc) values ('"+each.replace(a,"（   ）")+"','"+encrypt(a[a.find("（")+1:a.find("）")],"qddedtling")+"','standard')")
        except:pass
cursor.execute("commit")
cursor.close()
conn.close()

    
