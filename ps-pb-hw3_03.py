def sum_4et(var_chet):
    if var_chet != None:
        sum_chet = 0
        f = 1
        while f < len(var_chet):
            sum_chet += var_chet[f]
            f += 2
    else:
        sum_chet = 'Ошибка!'
    return sum_chet


def print_4et(var_chet_list):
    if var_chet_list != None:
        chet_list = []
        f = 1
        while f < len(var_chet_list):
            chet_list.append(var_chet_list[f])
            f += 2
    return chet_list

i = 1
fib_list = [1,1]
while i < 10000000:
    x = len(fib_list)-1
    if i == (fib_list[x] + fib_list[x-1]):
        fib_list.append(i)
    i+=1
print (fib_list)
print(len(fib_list))
print(sum_4et(fib_list))
print(print_4et(fib_list))
print(fib_list[len(fib_list)-2])