import psycopg2

try:
    conn = psycopg2.connect("dbname='taxbot' user='lg1xld4snmf8' host='taxbotprodmaster.cjwxl5sq5edt.us-west-2.rds.amazonaws.com' password='W5Fzc8dSIYjj5hBtypMD'")
except:
    print("I am unable to connect to the database")
    exit(1)


cur = conn.cursor()

query = ""
