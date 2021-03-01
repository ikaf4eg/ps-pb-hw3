def FizzBuzz (min_var,max_var):
    FizzBuzz_list = []
    FizzBuzz_sum = 0
    if min_var != None and max_var != None:
        i = min_var
        while i >= min_var and i <= max_var:
            x = i % 3
            y = i % 5
            if x == 0 and y == 0:
                FizzBuzz_list.append(i)
            i+=1
    else:
        FizzBuzz_list = 'не хватает краевых условий'
    f = 0
    while f < len(FizzBuzz_list):
        FizzBuzz_sum += FizzBuzz_list[f]
        f+=1
    return FizzBuzz_sum


print(FizzBuzz(1000,20000))