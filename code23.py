# 程序展示在一个文本文件中读取和写入数据的不同方法。

file = open("myfile.txt", "w")
L = ["This is Lagos\n", "This is Python\n", "This is Fcc\n"]

# 我把 ["This is Lagos \n","This is Python \n","This is Fcc \n"] 赋给变量 L

# \n 表示行的末尾

file.write("Hello There\n")
file.writelines(L)
file.close()
# 使用 close() 改变文件读取模式


file = open("myfile.txt", "r+")
print("Output of the Read function is ")
print(file.read())
print()
# # seek(n) 将文件句柄放到从开头开始的第 n 个字节。file.seek(0)
file.seek(0)
print("The output of the Readline function is ")
print(file.readline())
print()
#
file.seek(0)
#
# # 展示 read 和 readline 的区别
#
print("Output of Read(12) function is ")
print(file.read(12))
print()
#
file.seek(0)
#
print("Output of Readline(8) function is ")
print(file.readline(8))
#
file.seek(0)  # readlines 函数print("Output of Readlines function is ")
print(file.readlines())
print()
file.close()