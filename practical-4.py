password = input("please enter your password: ")
lenth = len(password)
if lenth < 6:
    print(password, ' is not strong password')
else:
    cout1 = 0
    cout2 = 0
    cout3 = 0
    for x in password:
        if x >= 'a' and x <='z':
            cout1 += 1
        if x >= 'A' and x <='Z':
            cout2 += 1
        if x>='0' and x <= '9':
            cout3 += 1
    # print(cout1)
    # print(cout2)
    # print(cout3)
    if (cout1 + cout2 + cout3 )< lenth:
        print(password, ' is the strong password')
    else:
        print(password, ' is not strong password')
