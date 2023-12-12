# studentInfo=["MarieDeane","ComputerScience",["PSP","FCS","BCPCN"]]
# print(studentInfo[0])
# print(studentInfo[1])
# print(studentInfo[2][0])


# def printStudent(studentInfo):
#     print(studentInfo)


# def printStudent(studentInfo):
#     for x in studentInfo:
#         print(x)


# def printStudent(studentInfo):
#    for x in studentInfo:
#        if type(x) == list:
#            for i in x:
#                print(i)
#        else:
#            print(x)
# printStudent(studentInfo)

studentInfo1={'name':'MarieDeane', 'course':'ComputerScience','modules':'["PSP","FCS","BCPCN"]'}
studentInfoDict = {}
studentInfo = {}
i = 1
studentInfoDict[f'student{i}'] = studentInfo1
def dictStore(studentInfo):
    global i
    i += 1
    studentInfoDict[f'student{i}'] = studentInfo
    print(studentInfoDict)
def addStudent():
    studentInfo['name'] = input("your name: ")
    studentInfo['course'] = input("your course: ")
    studentInfo['modules'] = list(input("your modules: ").split())
    dictStore(studentInfo)

while True:
    option = input("do you want to add information? ")
    if option == 'Yes':
        addStudent()
    elif option == 'No':
        break
    else:
        print("wrong input, try again!")






