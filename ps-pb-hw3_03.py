'''Задача на анализ последовательности Фибоначчи, состоящей из чисел, 
которые меньше 10.000.000 (десять миллионов). 
'''
# Функция вычисления суммы всех четных элементов последовательности
def sum_even_numb(var_even):
    sum_even = 0
    f = 0
    while f < len(var_even):
        if var_even[f] % 2 == 0:
            sum_even += var_even[f]
        f += 1
    return sum_even

# Функция получения списка всех четных элементов
def even_numb(var_even_list):
    if var_even_list != None:
        even_list = []
        f = 0
        while f < len(var_even_list):
            if var_even_list[f] % 2 == 0:
                even_list.append(var_even_list[f])
            f += 1
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

even_list = even_numb(fib_list)
x = 0
sum_even = 0
while x < len(even_list):
    sum_even += even_list[x]
    x += 1

print('Всего элементов в последовательности - ' + str(len(fib_list)))
print('Сумма всех четных элементов в последовательности - ' + str(sum_even))
print('Список всех четных элементов в последовательности:')
print(even_list)
print('Предпоследний элемент в последовтальности - ' + str(fib_list[len(fib_list)-2]))