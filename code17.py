# def justDoIt():
#     print("I have done it!")
# justDoIt()

#


# def anotherMasterpieceBy(name):
#     print(f"another master piece by {name}")
# a = input()
# anotherMasterpieceBy(a)


# import math
# def distanceBetween(x1,y1, x2, y2):
#     result = math.sqrt((x1-x2)**2 + (y1-y2)**2)
#     print(result)
#
# x1, y1 = map(int, input().split())
# x2, y2 = map(int, input().split())
# distanceBetween(x1, y1, x2, y2)


# def isLeapYear(year):
#     return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#
# def daysIn(year, month):
#     assert year > 1753
#     assert month >= 1 and month <= 12
#     day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if month == 2 and isLeapYear(year):
#         day[month] += 1
#     return day[month]
# year, month = map(int, input().split())
# ret = daysIn(year, month)
# print(ret)





def isLeapYear(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def daysIn(year, month):
    assert year > 1753
    assert month >= 1 and month <= 12
    day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and isLeapYear(year):
        day[month] += 1
    return day[month]

def isValidDate(year, month, day):
    if year <= 1753:
        return False
    elif not(month >= 1 and month <= 12):
        return False
    elif daysIn(year, month) != day:
        return False
    else:
        return True;
year, month, day = map(int, input().split())
print(isValidDate(year, month, day))

