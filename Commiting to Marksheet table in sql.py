import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Nigger@0509",
    database = "niggerdb"
)

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
               StudentID int primary key,
               Name varchar(225),
               Maths int,
               Chem int,
               Phy int,
               Total int
               )
            """)
print("table created")

num_stu = int(input("enter number of students whose marks r to be added: "))

values = []
for i in range(num_stu):
    try:
        StudentID = int(input("enter student ID: "))
        Name = input("enter the name of student: ")
        Maths = int(input("Enter the marks in maths: "))
        Chem = int(input("enter marks in chem: "))
        Phy = int(input("enter the marks in Phy: "))
        Total = Maths + Chem + Phy
        
        sql = "insert into students (StudentID, Name, Maths, Chem, Phy, Total) values(%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (StudentID, Name, Maths, Chem, Phy, Total))
        conn.commit()
        print(f"Student {Name} (ID: {StudentID}) inserted successfully!")

    except Exception as e:
        print(f"error inserting data {e}")

cursor.execute("select * from students")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
