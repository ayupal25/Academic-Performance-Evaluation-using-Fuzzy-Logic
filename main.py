from fuzzy import enter_details
import mysql.connector
import pandas as pd

mydb=mysql.connector.connect(
    host="localhost", 
    user="ayupal2001", 
    password="ayupal2001@", 
    db="fuzzy", 
    auth_plugin="mysql_native_password")

mycursor=mydb.cursor()

def insert_values():
    usn=input("Insert USN: ")
    name=input("Insert student name: ")
    sem=input("Insert student semester: ")
    sec=input("Insert student section: ")
    marks=float(input("Insert student marks: "))
    attendance=float(input("Insert student attendance: "))
    score=enter_details(marks,attendance)
    sql = "INSERT INTO student (usn,name,sem,sec,marks,attendance,score) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (usn,name,sem,sec,marks,attendance,score)
    mycursor.execute(sql, val)

def read_values(usn):
    sql = "SELECT * FROM student WHERE usn = %s"
    u = (str(usn), )
    mycursor.execute(sql, u)
    myresult = mycursor.fetchone()
    data = [myresult]
    df = pd.DataFrame(data, columns=['USN', 'Name', 'Semester', 'Section', 'Marks', 'Attendance', 'Score'])
    print(df)
    
def update_value(usn):
    print("Enter field to be updated:\n1. USN\n2. Name\n3. Semester\n4. Section\n5. Marks\n6. Attendance")
    option=int(input("Enter option:"))
    if option==1:
        value=input("Enter new USN: ")
        sql = "UPDATE student SET usn = %s WHERE usn = %s"
        val = (value,usn)
        mycursor.execute(sql, val)
        newusn=value
    elif option==2:
        value=input("Enter new name: ")
        sql = "UPDATE student SET name = %s WHERE usn = %s"
        val = (value,usn)
        mycursor.execute(sql, val)
    elif option==3:
        value=int(input("Enter new semester: "))
        sql = "UPDATE student SET sem = %s WHERE usn = %s"
        val = (value,usn)
        mycursor.execute(sql, val)
    elif option==4:
        value=input("Enter new section: ")
        sql = "UPDATE student SET sec = %s WHERE usn = %s"
        val = (value,usn)
        mycursor.execute(sql, val)
    elif option==5:
        value=float(input("Enter new marks: "))
        sql = "UPDATE student SET marks = %s WHERE usn = %s"
        val = (value,usn)
        mycursor.execute(sql, val)

        sqlm = "SELECT marks FROM student where usn=%s"
        addr = (usn,)
        mycursor.execute(sqlm, addr)
        m = mycursor.fetchone()
        sqla = "SELECT attendance FROM student where usn=%s"
        addr = (usn,)
        mycursor.execute(sqla, addr)
        a = mycursor.fetchone()
        score = enter_details(m,a)
        print("New score: ", score)
        sql = "UPDATE student SET score = %s WHERE usn = %s"
        val = (score,usn)
        mycursor.execute(sql, val)

    elif option==6:
        value=float(input("Enter new attendance: "))
        sql = "UPDATE student SET attendance = %s WHERE usn = %s"
        val = (value,usn)
        mycursor.execute(sql, val)

        sqlm = "SELECT marks FROM student where usn=%s"
        addr = (usn,)
        mycursor.execute(sqlm, addr)
        m = mycursor.fetchone()
        sqla = "SELECT attendance FROM student where usn=%s"
        addr = (usn,)
        mycursor.execute(sqla, addr)
        a = mycursor.fetchone()
        score = enter_details(m,a)
        print("New score: ", score)
        sql = "UPDATE student SET score = %s WHERE usn = %s"
        val = (score,usn)
        mycursor.execute(sql, val)

    else:
        print("Enter valid option")
        exit()

def delete_value(usn):
    sql = "DELETE FROM student WHERE usn = %s"
    adr = (usn, )
    mycursor.execute(sql, adr)

mydb.commit()

print("Academic Performance Evaluation using Fuzzy Logic")

while(True):
    print("Select the operation to be performed:\n1.Create\n2.Read\n3.Update\n4.Delete\n5.Exit")
    ch=int(input("Enter choice: "))
    if ch==1:
        insert_values()
        mydb.commit()
    elif ch==2:
        usn=input("Enter USN to be read: ")
        read_values(usn)
        mydb.commit()
    elif ch==3:
        usn=input("Enter USN to be updated: ")
        update_value(usn)
        mydb.commit()
    elif ch==4:
        usn=input("Enter USN of the field to be deleted: ")
        delete_value(usn)
        mydb.commit()
    elif ch==5:
        mydb.commit()
        exit()
    else:
        print("Enter valid option: ")
