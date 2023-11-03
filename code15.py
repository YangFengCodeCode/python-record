# Input names
# name = input("Input a name(STOP, to stop):")
# count = 0
# nameList = [ ]
# while name != "STOP":
#     nameList = nameList + [name]
#     count = count + 1
#     name = input("Input a name(STOP, to stop):")
# print("You typed", count, "names")
# print(nameList)



# a = { }
# b = dict()
# print(type(a))
# print(type(b))



# student = { 'id': 1, 'name': 'zhangsan' }
# print(student)

# student = {
#     'id' : 1,
#     'name' : 'zhang san'
# }
# print(student)
# print(student['id'])
# print(student['name'])



# student = {
#     'id': 1,
#     'name': 'zhangsan',
# }
# print('id' in student)
# print('score' in student)





# student = {
#     'id': 1,
#     'name': 'zhangsan',
# }
# student['score'] = 90
# print(student)
# student['score'] = 100
# print(student['score'])


# student = {
#     'id': 1,
#     'name': 'zhangsan',
#     'score': 80
# }
# student.pop('score')
# print(student)



# student = {
#     'id': 1,
#     'name': 'zhangsan',
#     'score': 80
# }
# for key in student:
#     print(key, student[key])


student = {
    'id': 1,
    'name': 'zhangsan',
    'score': 80
}
print(student.items())
