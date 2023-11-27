# list = [1,4,2,6,3]
# for i in range(0, len(list)-1):
#     end = i
#     tmp = list[end+1]
#     while end >= 0:
#         if list[end] > tmp:
#             list[end+1] = list[end]
#         else:
#             break
#         end -= 1
#     list[end + 1] = tmp
#
# print(list)



# year = int(input("please input the year: "))
# month = int(input("please input the month: "))
# list = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# if (year % 100 != 0 and year % 4 == 0) or year % 400 == 0:
#     list[2] = 29
# print(list[month])



# day = int(input("day? "))
# suffix = ""
#
# if day in (11, 12, 13) or day % 10 not in(1,2,3):
#     suffix = "th"
# else:
#     if day % 10 == 1:
#         suffix = "st"
#     if day % 10 == 2:
#         suffix = "nd"
#     if day % 10 == 3:
#         suffix = "rd"
#
# print(day, suffix)

# reverse a list
# s = ["a", "b", "c", "d", "e"]
# print("The list is ", s)
#
# left = 0
# right = len(s) - 1
# while left < right:
#     tmp = s[left]
#     s[left] = s[right]
#     s[right] = tmp
#     left += 1
#     right -= 1
# print("The reversed list is ", s)



# while True:
#     email = input("Please input your email: ")
#     format = "@student.zy.cdut.edu.cn"
#     if email[len(email)-len(format):] == format:
#         print("The email you entered is correct")
#         break
#     else:
#         print("Email format incorrect")



password = input("please enter your password ")
gap = 1
while gap*2 <= len(password):
    flag = 0
    i = 0
    j = i + gap
    while password[i:j] != password[j:j+gap]:
        i += 1
        j = i + gap
        if j >= len(password):
            flag = 1
            break
    if flag == 0:
        break
    gap += 1

if flag == 1:
    print("acceptable")
else:
    print("not acceptable")

