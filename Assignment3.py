import mysql.connector

try:
    #This is use for connect database
    db=mysql.connector.connect(host='localhost',user='root',database='assignmenttask',password='Hello@123')
    cursor=db.cursor()

    # for create table if table is not exist
    cursor.execute("create table if not exists students (student_id int auto_increment primary key ,first_name varchar(100),last_name varchar(50), age int , grade float)")

    print("Enter 1 For insert student Record : ")
    print("Enter 2 For Update student Record : ")
    print("Enter 3 For Delete student Record : ")
    print("Enter 4 For Show student Record : ")
    print("Enter 5 For Exit this operation : ")
    operation=int(input('Enter a Number : '))

    # Data Inserted
    if(operation==1):
        fname=str(input("Enter Your First Name : "))
        if not fname.isalpha():
            print("Wrong First Name")
        else:
            lname=str(input("Enter Your Last Name : "))
            if not lname.isalpha():
                print("Wrong Last Name")
            else:
                age=int(input("Enter Your Age : "))
                grade=float(input("Enter Your Grade : "))
                        
                cursor.execute("insert into students (first_name, last_name,age,grade) values (%s, %s, %s, %s)",(fname,lname,age,grade))
                print("Record inserted successfully!")

                cursor.execute("select * from students where first_name=%s and last_name=%s",(fname,lname))
                students=cursor.fetchall()
                print("Inserted Record is : ")
                for student in students:
                    print(student)

    # Data Updating
    elif(operation==2):
        fname=str(input("Enter Your First Name : "))
        grade=float(input("Enter Your New Grade : "))
        cursor.execute("update students set grade=%s where first_name=%s",(grade,fname))
        print("Record Updated Successfully!")

        cursor.execute("select * from students where first_name=%s and grade=%s",(fname,grade))
        students=cursor.fetchall()
        print("Updated Record is : ")
        for student in students:
            print(student)

    #Data Deleting
    elif(operation==3):
        lname=str(input("Enter Your Last Name : "))
        if lname.isalpha():
            cursor.execute("delete from students where last_name=%s",(lname,))

            print("Data Deleted where list_name is : ",lname)
            print("Record deleted successfully!")

            cursor.execute("select * from students")
            students=cursor.fetchall()
            for student in students:
                print(student)
        else:
            print("Wrong Input...")
        
    elif(operation==4):
        cursor.execute("select * from students")
        students=cursor.fetchall()
        print("All student Records")
        for student in students:
            print(student)

    elif(operation==5):
        exit
    else:
        print("Please write correct Number between given range 1 to 5")

except Exception as err:
    print(f'{err}')

finally:
    if 'db' in locals() and db.is_connected():
        db.commit()
        cursor.close()
        db.close()