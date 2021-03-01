'''Залача по выводу суммы чисел из диапазона от min_var до max_var 
включительно, которые делятся и на 3 и на 5 без остатка.
'''
# Функция получения списка чисел из диапазона, 
# которые делятся на 3 и на 5 без остатка
def FizzBuzz (min_var,max_var):
    FizzBuzz_list = []
    i = min_var
    while i >= min_var and i <= max_var:
        x = i % 3
        y = i % 5
        if x == 0 and y == 0:
            FizzBuzz_list.append(i)
        i+=1
    return FizzBuzz_list

# Функция вычисления суммы чисел из диапазона, 
# которые делятся и на 3 и на 5 без остатка
def FizzBuzz_sum(list):
    f = 0
    FizzBuzz_sum = 0
    while f < len(list):
        FizzBuzz_sum += list[f]
        f+=1
    return FizzBuzz_sum


# Проверка работы функций
try: 
    FB_list = FizzBuzz(1000,20000)
    print(FizzBuzz_sum(FB_list))
# В случаен ошибки в функции FizzBuzz ->
except:
    print('Ошибка! Не зватает аргументов')
