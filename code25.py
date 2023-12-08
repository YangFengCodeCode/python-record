def readTests():
    """Read the text files, and create a list of all test cases"""
    try:
        myFile = open("sensors.txt")  #Open the file and get the data
        numberTests = int(myFile.readline()) #get number of the test cases
        testCases = []
        for i in range(numberTests):
            numberSensors = int(myFile.readline()) #get number of the sensors
            sensors = myFile.readline().split()
            for i in range(numberSensors):
                sensors[i] = int(sensors[i])#get the data of each sensors
            testCases.append(sensors)
    except Exception as err:
        print(err)
        testCases = []
    finally:
        if "myFile" in locals():
            myFile.close()
        return testCases

def calculateFreeze(sensors):
    """Calculate when the microcontroller will freeze for each test case"""
    freezeTime = 0
    sensorActive = 0
    while sensorActive < 2: #Less than 2 sensors activate at the same time
        freezeTime += 1
        sensorActive = 0
        for s in sensors: #Check how many sensors will activate at the same time
            if freezeTime % s == 0:
                sensorActive += 1
    return freezeTime

testCases = readTests()
print(testCases)
for i in range(len(testCases)):
    freezeTime = calculateFreeze(testCases[i])
    print("Test Case", i+1, ": The Microcontroller will freeze at", freezeTime, "ms")