# Простая тестовая программа: угадай число

import random

secret = random.randint(1, 10)
print("Я загадал число от 1 до 10. Попробуй угадать!")

while True:
    guess = int(input("Твой вариант: "))

    if guess < secret:
        print("Мало, попробуй больше")
    elif guess > secret:
        print("Много, попробуй меньше")
    else:
        print("Угадал! 🎉")
        break
