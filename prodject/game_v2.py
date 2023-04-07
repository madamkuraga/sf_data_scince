"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def guess_number(number):
    min = 1
    max = 100
    guess = None
    attempts = 0
    max_attemps = 20
    
    while attempts < max_attemps:
        guess = (min + max) // 2
        attempts += 1

        if guess == number:
            return f"Загаданное число {number} найдено за {attempts} попыток"
        elif guess < number:
            min = guess + 1
        else:
            max = guess - 1

    return f"Загаданное число {number} не было найдено за {max_attemps} попыток"
    
print(guess_number(99))    
