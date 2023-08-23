pole = [[' ', '1', '2', '3'],
        ['1', ' ', ' ', ' '],
        ['2', ' ', ' ', ' '],
        ['3', ' ', ' ', ' ']]
TOTAL = 1
print()
print(f'ПРИВЕТ! Добро пожаловать в игру КРЕСТИКИ - НОЛИКИ!\nВводите '
      f'координаты используя цифры от 1 до 3\nХод первого игрока(Х):')
print()
i = 0
while i < 4:
        print(*pole[i], sep='  |  ', end='  | \n')
        print('----------------------')
        i += 1
print()
i_gor = input('Горизонтальная координата: ')
i_ver = input('Вертикальная координата: ')

while TOTAL < 10:
    if (i_gor == '1' or i_gor == '2' or i_gor == '3') and (i_ver == '1' or i_ver == '2' or i_ver == '3'):
        if (pole[int(i_gor)][int(i_ver)] == 'X') or (pole[int(i_gor)][int(i_ver)]) == '0':
            print('Такие координаты уже заняты, попробуй ещё раз!')
            i_gor = input('Горизонтальная координата: ')
            i_ver = input('Вертикальная координата: ')
        else:
            if TOTAL % 2 != 0:
                pole[int(i_gor)][int(i_ver)] = 'X'
                TOTAL += 1
                if ((pole[1][1] == pole[1][2] == pole[1][3] == 'X') or
                    (pole[2][1] == pole[2][2] == pole[2][3] == 'X') or
                    (pole[3][1] == pole[3][2] == pole[3][3] == 'X') or
                    (pole[1][1] == pole[2][2] == pole[3][3] == 'X') or
                    (pole[1][3] == pole[2][2] == pole[3][1] == 'X') or
                    (pole[1][1] == pole[2][1] == pole[3][1] == 'X') or
                    (pole[1][2] == pole[2][2] == pole[3][2] == 'X') or
                    (pole[1][3] == pole[2][3] == pole[3][3] == 'X')):
                    i = 0
                    while i < 4:
                        print(*pole[i], sep='  |  ', end='  | \n')
                        print('----------------------')
                        i += 1
                    print('ПОЗДРАВЛЯЮ! Победа первого игрока (Х)')
                    question = input('Отличная игра! Хотите сыграть ещё раз? Y/N: ')
                    if question == 'Y' or question == 'y':
                        pole = [[' ', '1', '2', '3'],
                                ['1', ' ', ' ', ' '],
                                ['2', ' ', ' ', ' '],
                                ['3', ' ', ' ', ' ']]
                        TOTAL = 1
                    else:
                        print('Пока!')
                        break
            else:
                pole[int(i_gor)][int(i_ver)] = '0'
                TOTAL += 1
                if ((pole[1][1] == pole[1][2] == pole[1][3] == '0') or
                    (pole[2][1] == pole[2][2] == pole[2][3] == '0') or
                    (pole[3][1] == pole[3][2] == pole[3][3] == '0') or
                    (pole[1][1] == pole[2][2] == pole[3][3] == '0') or
                    (pole[1][3] == pole[2][2] == pole[3][1] == '0') or
                    (pole[1][1] == pole[2][1] == pole[3][1] == '0') or
                    (pole[1][2] == pole[2][2] == pole[3][2] == '0') or
                    (pole[1][3] == pole[2][3] == pole[3][3] == '0')):
                    i = 0
                    while i < 4:
                        print(*pole[i], sep='  |  ', end='  | \n')
                        print('----------------------')
                        i += 1
                    print('ПОЗДРАВЛЯЮ! Победа второго игрока (0)')
                    question = input('Отличная игра! Хотите сыграть ещё раз? Y/N: ')
                    if question == 'Y' or question == 'y':
                        pole = [[' ', '1', '2', '3'],
                                ['1', ' ', ' ', ' '],
                                ['2', ' ', ' ', ' '],
                                ['3', ' ', ' ', ' ']]
                        TOTAL = 1
                    else:
                        print('Пока!')
                        break
            print()
            i = 0
            while i < 4:
                print(*pole[i], sep='  |  ', end='  | \n')
                print('----------------------')
                i += 1
            print()
            if TOTAL % 2 == 0 and TOTAL != 10:
                print('Ход второго игрока(0):')
                i_gor = input('Горизонтальная координата: ')
                i_ver = input('Вертикальная координата: ')
            elif TOTAL % 2 != 0 and TOTAL != 10:
                print('Ход первого игрока(Х):')
                i_gor = input('Горизонтальная координата: ')
                i_ver = input('Вертикальная координата: ')
    else:
        print('Введены некорректные координаты, напоминаю, используйте числа от 1 до 3')
        i_gor = input('Горизонтальная координата: ')
        i_ver = input('Вертикальная координата: ')
    if TOTAL == 10:
        print('Ничья!')
        question = input('Спасибо за игру! Хотите сыграть ещё раз? Y/N: ')
        if question == 'Y' or question == 'y':
            pole = [[' ', '1', '2', '3'],
                    ['1', ' ', ' ', ' '],
                    ['2', ' ', ' ', ' '],
                    ['3', ' ', ' ', ' ']]
            TOTAL = 1
            i = 0
            while i < 4:
                print(*pole[i], sep='  |  ', end='  | \n')
                print('----------------------')
                i += 1
            print('Ход первого игрока(Х):')
            i_gor = input('Горизонтальная координата: ')
            i_ver = input('Вертикальная координата: ')
        else:
            print('Всего хорошего!')
            break





