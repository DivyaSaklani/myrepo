import sqlite3

conn = sqlite3. connect('student_db.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Student_Name TEXT NOT NULL,
    College_Name Text NOT NULL,
    r1 FLOAT NOT NULL,
    r2 FLOAT NOT NULL,
    r3 FLOAT NOT NULL,
    Tech_r FLOAT NOT NULL,
    Total_Marks FLOAT NOT NULL,
    Result TEXT NOT NULL
    )
''')

conn.commit()

def get_verified_input(prompt,check_valid,error):
    while True:
        try:
            value=input(prompt)
            if check_valid(value):
              print(type(value))
              return value
            else:
                return error
        except Exception as e:
            print(f"Error:{e}") 

def verify_name(Student_Name):
    return 0 < len(Student_Name) and len(Student_Name) <=30

def verify_college(College_Name):
    return 0 < len(College_Name) and len(College_Name) <=50  

def verify_round1(r1):
    return 0.0 <= float(r1 )<=10.0

def verify_round2(r2):
    return 0.0 <= float(r2)<= 10.0

def verify_round3(r3):
    return 0.0<=float(r3)<=10.0

def verify_round(Tech_r):
    return 0.0<=float(Tech_r)<=20.0



Student_Name = get_verified_input("Enter your name -",verify_name,"Name should have 0-30 Characters")
College_Name = get_verified_input("Enter College name - ",verify_college,"College name should have 0-50 Characters")
r1 = float(get_verified_input("Round 1 -",verify_round1,"Enter in decimal"))
r2 = float(get_verified_input("Round 2 -",verify_round2,"Enter in decimal"))
r3 = float(get_verified_input("Round 3 -",verify_round3,"Enter in decimal"))
Tech_r = float(get_verified_input("Technical round -",verify_round,"Enter in decimal"))
Total_Marks = r1 + r2 + r3 + Tech_r
result=""
def calc_result(Total_Marks):
    
    if Total_Marks>=35:
       result = "Selected"
    else :
        result = "Rejected"

    return result

result=calc_result(Total_Marks)

""" def calc_rank(Total_Marks):
    l1=[]
    for i in id:
         """


cursor.execute(''' 
    INSERT INTO student(Student_Name,College_Name,r1 ,r2 ,r3,Tech_r ,Total_Marks,Result) VALUES(?,?,?,?,?,?,?,?)''',(Student_Name,College_Name,r1,r2,r3,Tech_r,Total_Marks, result))

conn.commit()

cursor.execute('SELECT * FROM student')
rows= cursor.fetchall()


print("\n All Records")
print("ID | STUDENT NAME |COLLEGE NAME | ROUND1 |ROUND2 | ROUND3 |TECHNICAL ROUND | TOTAL MARKS | RESULT")

for r in rows:
    print(f"{r[0]} | {r[1]} || {r[2]} || {r[3]} || {r[4]} |  {r[5]} | {r[6]} | {r[7]} | {r[8]} ")

conn.close()
    


    
        

