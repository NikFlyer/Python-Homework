# Задайте список из вещественных сил. Напишите программу,
# которая найдет разницу между максимальным и минимальным значением
# дробной части элиментов

source_list = [1.1, 1.5, 3.1, 5, 10.01]
new_list = [round(i % 1, 2) for i in source_list if i % 1 != 0]
print(f'{source_list} => {max(new_list) - min(new_list)}')