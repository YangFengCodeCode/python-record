numberList = [2, 0, 2, 3, 0, 7, 0, 8]
def menu():
    print(f"numberList: {numberList}")# list has changed
    print("1. Add the number to the list and return.")
    print("2. Delete the number in the list and return.")
    print("3. check if the number is in the list and return all the position.")
    print("4. Change the oldNumber of the list to newNumber and return.")

def addNumber(numberList, number):
    numberList.append(number)
    return numberList

def deleteNumber(numberList, number):
    for x in numberList:
       if x == number:
          numberList.remove(x)
    return numberList

def findNumber(numberList, number):
    list = []
    for i in range(0, len(numberList)):
        if numberList[i] == number:
            list += [i+1] #not the subscript
    return list #return a list including the position of numbers

def changeNumber(numberList, oldNumber, newNumber):
    for i in range(0, len(numberList)):
        if numberList[i] == oldNumber:
            #change to the newNumber
            numberList[i] = newNumber
    return numberList

while True:
   menu()
   option = int(input("Please enter an option (0, 1, 2, 3, 4): "))
   #check the range
   assert option >= 0 and option <= 4

   if option == 1:
       number = int(input("Enter a number to add: "))
       addNumber(numberList, number)

   if option == 2:
        number = int(input("Enter a number to delete: "))
        assert number in numberList
        deleteNumber(numberList, number)

   if option == 3:
       number = int(input("Enter a number to find: "))
       assert number in numberList
       print(f"The position of the number in numberList is: {findNumber(numberList, number)}")

   if option == 4:
       oldNumber = int(input("Enter oldNumber to change: "))
       assert oldNumber in numberList
       newNumber = int(input("Enter newnumber: "))
       changeNumber(numberList, oldNumber, newNumber)

   if option == 0:
       print("exit")
       break








