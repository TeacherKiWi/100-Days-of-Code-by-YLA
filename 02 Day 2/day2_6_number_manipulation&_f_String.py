# Number Manipulation and f-Strings

print(8/3)  # float
print(int(8/3))  # integer
print(round(8/3,2))  # round at 2 decimal point
print(round(2.6666666666666,1))  # round at 1 decimal point
print(8//3)  # // is floor division, it gives integer

print(4/2)   # float
print(type(4/2))   # float
result = 4/2
print(result)   # float
result /=2
print(result)   # float

score = 0
# User scores a point
score += 1  # score = score+1
print(score)
score -= 1  # score = score-1
print(score)
# *=, /= can be used.

score = 0
height = 1.8
isWinning = True
# f-String
print(f" Your score is {score}, your height is {height}, you are winning is {isWinning}.")