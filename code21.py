# def addThree(a, b, c):#actual
#     print("The sum is ", a+b+c)
#     return a + b + c


# def foo(x, y):
#     tmp = x
#     x = y
#     y = tmp
#     a = 20
#     b = 30
#     c = 40
#     print(a, b, c, x, y)
#
# a = 1
# b = 2
# c = 3
# x = 4
# y = 5
# foo(50, 60)
# print(a, b, c, x, y)


# def addValues(numbers):
#     total = 0
#     for i in numbers:
#         total += i
#     return total
#
# myList = [10, 20, 30, 40]
# print("The sum of all the numbers is:", addValues(myList))
#
#
# def gameOver(s1, s2, s3, s4, s5):
#     """ Return True if one of the score
#     is more or equal to 100 """
#     over = False
#     if s1 >= 100 or s2 >= 100 or s3 >= 100 or s4 >= 100 or s5 >= 100:
#         over = True
#     return over
#
#
# def castDice():
#     """ Return the value of 2 randomly casted dice,
#     or 0 if any of the dice is 1,
#     or -1 if both dice are 1 """
#     import random
#     die1 = random.randint(1, 6)
#     die2 = random.randint(1, 6)
#     points = 0
#     print("die 1-->", die1, "Die2 -->", die2)
#     # total of dice 1 + dice 2, 0 or -1 if both dice are 1
#     if die1 == 1 and die2 == 1:
#         points = -1
#     elif die1 != 1 and die2 != 1:
#         points = die1 + die2
#     return points
#
#
# def updateScore(score, points):
#     """ Return the updated score with the points.
#     Return 0 if the points is -1"""
#     if points != -1:
#         score += points
#     else:
#         score = 0
#     return score
#
#
# def displayWinner(s1, s2, s3, s4, s5):
#     """ Display the player with the highest score,
#     or if both have a tie """
#     list = [s1, s2, s3, s4, s5]
#     max_score = max(list)
#     winner_list = []
#     for i in range(0, len(list)):
#         if list[i] == max_score:
#             winner_list += [i+1]
#     if len(winner_list) == 5:
#         print("both players have the same score ", max_score)
#     else:
#         print(f"The winner is player {winner_list} :score {max_score}")
#
#
#
# # main program
# # define two players' socre varibales
# score1 = 0
# score2 = 0
# score3 = 0
# score4 = 0
# score5 = 0
# while not gameOver(score1, score2, score3, score4, score5):
#     points = castDice()
#     score1 = updateScore(score1, points)
#
#     points = castDice()
#     score2 = updateScore(score2, points)
#
#     points = castDice()
#     score3 = updateScore(score3, points)
#
#     points = castDice()
#     score4 = updateScore(score4, points)
#
#     points = castDice()
#     score5 = updateScore(score5, points)
#
#     print("player 1: ", score1, "player 2: ", score2, "player 3: ",score3, "player 4: ", score4, "player 5: ", score5)
#
# displayWinner(score1, score2, score3, score4, score5)







