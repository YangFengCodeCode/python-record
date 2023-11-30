
def judge(list, n):
    flag = 0
    while True:
        for j in range(0, len(list)):
            for i in range(j+1, len(list)):
                   if list[j] == list[i]:
                      flag = 1
                      print(f"Test Case {n} : The Microcontroller will freeze at {list[j]} ms ")
                      break
            if flag == 1:
                break
        for k in range(0, len(list)):
            list[k] = list[k]*2
        if flag == 1:
            break


T = int(input("please input T "))
listA = [1]*T
for i in range(0, T):
    N = int(input("please input N "))
    A = input("please enter A ").split()
    A = [int(a) for a in A ]
    listA[i] = A
    print(A)
print(listA)
for i in range(0, len(listA)):
    judge(listA[i], i)




