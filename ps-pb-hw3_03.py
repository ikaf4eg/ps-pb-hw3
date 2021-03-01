'''Задача на анализ последовательности Фибоначчи, состоящей из чисел, 
которые меньше 10.000.000 (десять миллионов). 
'''
# Функция вычисления суммы всех четных элементов последовательности
def sum_even_numb(var_even):
    sum_even = 0
    f = 1
    while f < len(var_even):
        sum_even += var_even[f]
        f += 2
    return sum_even

# Функция получения списка всех четных элементов
def print_even_numb(var_even_list):
    if var_even_list != None:
        even_list = []
        f = 1
        while f < len(var_even_list):
            even_list.append(var_even_list[f])
            f += 2
    return even_list


fib_list = [1,1] # задание начала последовательности Фибоначчи
i = 1
# Получение последовательности Фибоначчи 
# в диапазоне положительных чисел до 10 000 000
while i < 10000000:
    x = len(fib_list)-1
    if i == (fib_list[x] + fib_list[x-1]):
        fib_list.append(i)
    i+=1

print('Всего элементов в последовательности - ' + str(len(fib_list)))
print('Сумма всех четных элементов в последовательности - ' + str(sum_even_numb(fib_list)))
print('Список всех четных элементов в последовательности:')
print(print_even_numb(fib_list))
print('Предпоследний элемент в последовтальности - ' + str(fib_list[len(fib_list)-2]))