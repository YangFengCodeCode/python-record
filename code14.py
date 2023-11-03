# password = input("please enter your password: ")
# lenth = len(password)
# if lenth < 6:
#     print('It is not strong password')
# else:
#     cout1 = 0
#     cout2 = 0
#     cout3 = 0
#     for x in password:
#         if x.islower():
#             cout1 += 1
#         if x.isupper():
#             cout2 += 1
#         if x.isdigit():
#             cout3 += 1
# if (cout1 + cout2 + cout3 )< lenth and cout1 != 0 and cout2 != 0 and cout3 != 0:
#     print('It is the strong password')
# else:
#     print('It is not strong password')
# #


# password = input("please enter your password: ")
# lenth = len(password)
# print(password, ' is of valid lenth:', lenth)
# # check rule 1
# if lenth < 6:
#     print(password, ' is not strong password')
# else:
#     cout1 = 0
#     cout2 = 0
#     cout3 = 0
#     for x in password:
#         # check rule 2
#         if x >= 'a' and x <='z':
#             cout1 += 1
#         # check rule 3
#         if x >= 'A' and x <='Z':
#             cout2 += 1
#         print(password, 'contain at least one uppercase letter')
#         # check rule 4
#         if x>='0' and x <= '9':
#             cout3 += 1
#         print(password, 'contain at least one digit')
#
#     if cout1 != 0:
#         print(password, 'contain at least one lowercase letter')
#     else:
#         print(password, 'does not contain any lowercase letter')
#
#     if cout2 != 0:
#         print(password, 'contain at least one lowercase letter')
#     else:
#         print(password, 'does not contain any lowercase letter')
#
#     if cout3 != 0:
#         print(password, 'contain at least one lowercase letter')
#     else:
#         print(password, 'does not contain any lowercase letter')
#
#
#     # check rule 5
#     if (cout1 + cout2 + cout3 )< lenth:
#         print(password, 'contain at least one punction ')
#         print(password, ' is the strong password')
#     else:
#         print(password, ' is not strong password')



password = input("input password: ")
lenth = len(password)
cout1 = 0
cout2 = 0
cout3 = 0
flag = 1

print("check rule 1")
print(f"{password} is of valid length: {lenth}")
if lenth < 6:
    flag = 0

for x in password:
        # check rule 2
    if x >= 'a' and x <='z':
            cout1 += 1
        # check rule 3
    if x >= 'A' and x <='Z':
            cout2 += 1
        # check rule 4
    if x>='0' and x <= '9':
            cout3 += 1
# print(cout1)
# print(cout2)
# print(cout3)

print("check rule 2")
print(f"number of lowercase letters: {cout1}")
if cout1 == 0:
    flag = 0
    print(f"{password} does not contain any lowercase letter")
else:
    print(f"{password} contains at least one lowercase letter")


print("check rule 3")
print(f"number of uppercase letters: {cout2}")
if cout2 == 0:
    flag = 0
    print(f"{password} does not contain any uppercase letter")
else:
    print(f"{password} contains at least one uppercase letter")


print("check rule 4")
print(f"number of digit: {cout3}")
if cout3 == 0:
    flag = 0
    print(f"{password} does not contain any digit")
else:
    print(f"{password} contains at least one digit")

print("check rule 5")
# character does not contain
if (cout1 + cout2 + cout3) < lenth and cout1!=0 and cout2 != 0 and cout3!=0:
    print(f"{password} contains at least one punctuation")
else:
    flag = 0
    print(f"{password} does not contain any punctuation")

print("Check for all the rules")
if flag == 1:
    print(f"Overall: {password} is valid")
else:
    print(f"Overall: {password} is not valid")