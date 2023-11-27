# def swap(x, y):
#  t = x
#  x = y
#  y = t
#  return x, y
#
# #main program
# a = 3
# b = 4
# print("a = ", a)
# print("b = ", b)
# a, b = swap(a, b)
# print("a = ", a)
# print("b = ", b)


# import ListFunctions
# a = int(input("Enter a number (-1 to stop)"))
# list = []
# while a != -1:
#    list = list + [a]
#    a = int(input("Enter a number (-1 to stop)"))
#
# ListFunctions.numberList(list)
# ListFunctions.sumList(list)
# ListFunctions.findLowest(list)
# ListFunctions.findHighest(list)
# ListFunctions.averageList(list)


def clash(hr1, dur1, hr2, dur2):
   if hr1 < hr2 and hr1 + dur1 > hr2:
      return True
   elif hr1 > hr2 and hr2 + dur2 > hr1:
       return True
   else:
      return False
hr1, dur1, hr2, dur2 = map(int, input().split())
print(clash(hr1, dur1, hr2, dur2))


import dates
year, month, day = map(int, input().split())
print(dates.isValidDate(year, month, day))