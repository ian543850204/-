# Python Data From_DB
# create by Ian
# 2022/4/26
#DB資料需先設定


#匯入套件
import cx_Oracle

#連線TNS
dsn_tns = cx_Oracle.makedsn('XXXXX', 'XXX', 'XXX')

#連線帳號和密碼
conn = cx_Oracle.connect(user='XXX', password='XXX', dsn=dsn_tns)
cur = conn.cursor()


''' ================= 呼叫後傳入的參數 ======================'''
print("'''--------------DPS_SC_VERSION_KEY傳入----------------'''")
#DPS_SC_VERSION_KEY

#被第三方程式呼叫後 傳入Key值
#傳入引數DPS_VERSION_KEY
#sys.argv[0] 為 檔案名
#sys.argv[1] 為 第一個引數
try:
    DPS_SC_VERSION_KEY=int(sys.argv[1])
    print("SC_version KEY is"+str(sys.argv[1]))
except:
    print("無傳入DPS_SC_VERSION_KEY引數")
    

''' ================= 從DB 讀取RULE 規則 ======================'''
#從 DW_MRP_MT_DPS_SC_RULE 讀取此次排程規則
wo_rule_from_db=[]

#使用引數的 Key 值做為讀取 DB 的 唯一Key。
sql=(
"SELECT * "
"FROM xxx "
"WHERE DPS_SC_VERSION_KEY = "+str(DPS_SC_VERSION_KEY)+" "
)
cur.execute(sql)

rows = cur.fetchall()
for row in rows:
    wo_rule_from_db.append(row) #將抓取資料庫的值存入變數。 
#工單 KEY
wo_key=[]
#工單的名稱
wo_name=[]

#存取規則 from DB
for i in range(len(wo_rule_from_db)):
    wo_key.append(wo_rule_from_db[i][0])
    wo_name.append(wo_rule_from_db[i][1])
    #.....

    
#關閉 DB 連線
cur.close()
conn.close()