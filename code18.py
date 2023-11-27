# def printinfo(name, age):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
#
#
# # 调用printinfo函数
# printinfo(age=50, name="runoob")


# def printinfo(name, age=35):
#     "打印任何传入的字符串"
#     print("名字: ", name)
#     print("年龄: ", age)
#     return
#
#
# # 调用printinfo函数
# printinfo(age=50, name="runoob")
# print("------------------------")
# printinfo(name="runoob")


# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vartuple)
#
# # 调用printinfo 函数
# printinfo(70, 60, 50)


# def printinfo(arg1, *vartuple):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     for var in vartuple:
#         print(var)
#     return
#
# # 调用printinfo 函数
# printinfo(10)
# printinfo(70, 60, 50)


# def printinfo(arg1, **vardict):
#     "打印任何传入的参数"
#     print("输出: ")
#     print(arg1)
#     print(vardict)
#
#
# # 调用printinfo 函数
# printinfo(1, a=2, b=3)

# x = lambda a : a + 10
# print(x(5))

# sum = lambda arg1, arg2: arg1 + arg2
# # 调用sum函数
# print("相加后的值为 : ", sum(10, 20))
# print("相加后的值为 : ", sum(20, 20))


# def myfunc(n):
#     return lambda a: a * n
#
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
#
# print(mydoubler(11))
# print(mytripler(11))


# list = ['Google', 'Runoob', 1997, 2000]
# print("原始列表 : ", list)
# del list[2]
# print("删除第三个元素 : ", list)

# tup = ('Google', 'Runoob', 1997, 2000)
#
# print(tup)
# del tup
# print("删除后的元组 tup : ")
# print(tup)