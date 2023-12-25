
def loadStudents():
    try:
        file = open("students.txt", "r")
        studentsList = []
        for line in file:
            line.strip('\n')
            str = line.split(',')
            infoList = [int(str[0]), str[1], float(str[2].strip('\n'))]
            # need to convert str to int and float
            studentsList += [infoList]
            #in list have sublist

    except Exception as err:
        print(err)
    finally:
        if "file" in locals():
            file.close()
        return studentsList

def printStudents(students):
    for i in range(0, len(students)):
        print("student ", students[i][0], ' - ', students[i][1], ' - ', students[i][2])

def addStudents(students):
    ID = int(input("Please enter student ID: "))
    name = input("Please enter student name: ")
    GPA = float(input("Please enter student GPA: "))
    # put information into a list
    infoList = [ID, name, GPA]
    students += [infoList]
    print(students)
    return students

def orderedByGPA(students):
    students.sort(key=lambda x: x[2], reverse= True)
    # x means a sublist  True means descending order
    print("Ordered students: ", students)
    return students

def saveStudents(students):
    try:
        myFile = open("newStudents.txt", "w")
        for student in students:
            myFile.write(str(student[0]) + ',' + str(student[1]) + ',' + str(student[2]) + "\n")
    except Exception as err:
        print(err)
    finally:
        print("Save to file newStudents.txt correctly")
        myFile.close()


students = loadStudents()
printStudents(students)
students = addStudents(students)
students = orderedByGPA(students)
saveStudents(students)







