def loadStudents():
    try:
        students =[]
        myFile = open("students.txt", "r")
        for line in myFile:
            ID, name, GPA = line.strip('\n').split(',')
            ID = int(ID)
            GPA = float(GPA)
            students.append([ID, name, GPA])
    except Exception as err:
        print("err")
    finally:
        if "myFile" in locals():
            myFile.close()
        return students

def printStudents(students):
    """ list all the student records in the database"""
    for i in range(0, len(students)):
        print("students", students[i][0],'-',students[i][1],'-',students[i][2])

def addStudents(students):
    """add a student record to the database, print and return the database"""
    ID = int(input("Please enter students ID:"))
    name = input("Please enter student name: ")
    GPA = float(input("Please enter student GPA: "))
    students.append([ID, name, GPA])
    print(students)
    return students

def orderedByGPA(students):
    """make the student records in descending order based on GPA from highest to lowest and print database"""
    orderedStudents = sorted(students, key=lambda x: (x[2]), reverse=True)
    print("Ordered students:", orderedStudents)
    return orderedStudents

def saveStudents(students):
    """ save the student records in a database to a new file named "newStudents.txt". """
    try:
        myFile = open("newStudents.txt","w")
        for student in students:
            myFile.write(str(student[0]) + ',' + str(student[1]) + ',' + str(student[2]) + "\n")
    except Exception as err:
        print(err)
    finally:
        print("Save to file newStudents.txt correctly")
        if "newFile" in locals():
            myFile.close()

students = loadStudents()
printStudents(students)
students = addStudents(students)
students = orderedByGPA(students)
saveStudents(students)