# Напишите программу, которая по заданному номеру четверти, показывает диапазон
# возможных точек в этой четверти (х и у)

d = int(input('Введите номер четверти: '))

if d == 1: 
    print('Значения X > 0, значения Y > 0')
if d == 2: 
    print('Значения X < 0, значения Y > 0')
if d == 3: 
    print('Значения X < 0, значения Y < 0')
if d == 4: 
    print('Значения X > 0, значения Y < 0')
if d > 4:
    print('Указанного значения не существует')
