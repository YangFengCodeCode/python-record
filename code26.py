# try:
#     file = open("example1.txt", "r")
#     print(file.readline())
#     #print(file.read())
#     file.close()
# except:
#     print("error")


# try:
#     file = open("example1.txt", "r")
#
#     print(file.readlines())
#     file.seek(0)
#
#     print(file.read())
#     file.seek(0)
#
#     print(file.readline())
#     print(file.readline())
#
#     file.seek(0)
#     for line in file:
#         print(line)
#
#     file.close()
#
# except:
#     print("error")



# try:
#     f = open("example1.txt", "r")
#     line = f.readlines()
#     print(line[1])
#     print(line[0])
#     f.close()
# except:
#     print("error")


# try:
#     f = open("example1.txt", "r")
#     words = f.readlines()
#     wordFirst = words[0].split()
#     wordSecond = words[1].split()
#     print(wordFirst)
#     print(wordSecond)
#     i = 0
#     while i < len(wordFirst):
#         if i < len(wordSecond):
#             print(wordFirst[i], wordSecond[i])
#         else:
#             print(wordFirst[i])
#         i += 1
#
#     f.close()
# except:
#     print("error")



# try:
#     file1 = open("example1.txt", "r")
#     file2 = open("exercise5.txt", "w")
#     s = file1.read()
#     file2.write(s)
#     file1.close()
#     file2.close()
# except:
#     print("error")


# try:
#     file1 = open("example1.txt", "r")
#     file2 = open("exercise5.txt", "a")
#     s = file1.read()
#     file2.write('\n')
#     file2.write(s)
#     file1.close()
#     file2.close()
# except:
#     print("error")
#

# try:
#     n = int(input("please enter first number "))
#     m = int(input("please enter second number "))
#     c = 7/0
# except ValueError:
#     print("value wrong")
# except ArithmeticError:
#     print("ArithmeticError")
# except:
#     print("error")


# try:
#     file = open("info.txt", "w")
#     print("please input your name, age, class, hometown: ")
#     infoList = list(input().split())
#     print(infoList)
#     for info in infoList:
#         file.write(info+' ')
#     file.close()
#
# except Exception as err:
#     print(err)

while True:
    try:
        file = open("info.txt", "a")
        print("please input your name, age, class, hometown: ")
        infoList = list(input().split())
        print(infoList)
        for info in infoList:
            file.write(info+' ')
        file.write('\n')
        option = input("Do you want to add another information: Yes/No ")
        assert option == 'Yes' or 'No'
        if option == "No":
            file.close()
            break

    except Exception as err:
        print(err)



#

# file = open("students.txt", "r")
# studentsList = []
# for line in file:
#     line.strip('\n')
#     str = line.split(',')
#     infoList = [int(str[0]), str[1], float(str[2].strip('\n'))]
#     print(infoList)
#     studentsList += [infoList]
# print(studentsList)
# print(len(studentsList))
# print(studentsList[0][0])

#
# file = open("students.txt", "a")
# ID = int(input("Please enter student ID: "))
# name = input("Please enter student name: ")
# GPA = int(input("Please enter student GPA: "))
# infoList = [ID, name, GPA]
# for x in infoList:
#     file.write(x)
# file.close()

# file = open("students.txt", "a")
# ID = int(input("Please enter student ID: "))
# name = input("Please enter student name: ")
# GPA = int(input("Please enter student GPA: "))
# infoList = [ID, name, GPA]
# file.write('\n')
# for i in range(0, len(infoList)):
#     if i == len(infoList) - 1:
#         file.write(str(infoList[i]))
#     else:
#         file.write(str(infoList[i]) + ',')


students =[]
myFile = open("students.txt", "r")
# data = myFile. readlines()#open the file and get the data
for line in myFile:
    ID, name, GPA = line.strip('\n').split(',')
    ID = int(ID)
    GPA = float(GPA)
    students.append([ID, name, GPA])
print(students)