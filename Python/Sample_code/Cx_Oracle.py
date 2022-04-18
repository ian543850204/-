# Python cx_Oracle
# create by Ian
# 2022/4/18

#套件
import cx_Oracle

#連線TNS
dsn_tns = cx_Oracle.makedsn('網域名', '埠號', '資料庫名稱')

#連線帳號和密碼
conn = cx_Oracle.connect(user='帳號', password='密碼', dsn=dsn_tns)
cur = conn.cursor()


#設立 List 將 DB 資料匯入
data_from_db=[]

#sql 語法
sql=(
"SELECT A "
"FROM TABLE "
"WHERE KEY = "+str(import_KEY)+" "
)

cur.execute(sql)

rows = cur.fetchall()
for row in rows:
    data_from_db.append(row) #將抓取資料庫的值存入變數。

#讀取 下完 sql 的資料 
for i in range(len(data_from_db)):
    KEY = data_from_db[i][0]
        
        
#關閉 DB 連線
cur.close()
conn.close()