
def createNetwork():
    with open("network.txt", "r") as myFile:
        stations = {}
        for line in myFile:
            stationInfo = line.split()
            nameStation = stationInfo[0]
            stations = addStation(stations,nameStation)
            del(stationInfo[0])
            for connection in stationInfo:
                stations = makeConnection(stations, connection, nameStation)
        return stations

def addStation(stations, name):
    if name not in stations:
        stations[name] = []
    return stations

def makeConnection(stations, station1, connectionName):
    stations = addStation(stations, station1)
    stations[station1].append(connectionName)
    return stations

#main program
network = createNetwork()
print("The network created is ", network)



# studentInfo1={'name':'MarieDeane', 'course':'ComputerScience','modules':'["PSP","FCS","BCPCN"]'}
# studentInfoDict = {}
# studentInfo = {}
# i = 1
# studentInfoDict[f'student{i}'] = studentInfo1
# def dictStore(studentInfo):
#     global i
#     i += 1
#     studentInfoDict[f'student{i}'] = studentInfo
#     print(studentInfoDict)
# def addStudent():
#     studentInfo['name'] = input("your name: ")
#     studentInfo['course'] = input("your course: ")
#     studentInfo['modules'] = list(input("your modules: ").split())
#     dictStore(studentInfo)
#
# while True:
#     option = input("do you want to add information? ")
#     if option == 'Yes':
#         addStudent()
#     elif option == 'No':
#         break
#     else:
#         print("wrong input, try again!")
