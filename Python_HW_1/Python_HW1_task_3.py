
#  Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
#  Программа должна подсказывать “больше” или “меньше” после каждой попытки.
#  Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint
LOW_LIMIT = 0
UPP_LIMIT = 1000
TRY_NUM = 10
rand_num = randint(LOW_LIMIT, UPP_LIMIT)
count = 1
guess = None

while count <= TRY_NUM:
    print('Попытка', count)
    guess = int(input('Введите ваш вариант: '))

    if guess == rand_num:
        print('Угадали! Загаданное число:', guess)
        break

    elif guess > rand_num:
         print('Меньше!')
    elif guess < rand_num:
        print('Больше!')
    count += 1

print('Попытки закончились')
print('Случайное число:', rand_num)