import random

randomInteger = random.randint(1,10)
print(randomInteger)

# random.random() gives random float between 0 and 1 ---> (0.0000...-0.99999...)
randomFloat = random.random() * 5  # (0.000000...-4.99999...)
print(randomFloat)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}.")