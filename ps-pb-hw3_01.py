'''Функция согласования окончаний существительных 
в зависимости от переданного числа. 
Функция принимает 4 параметра:
1. число
2. форма слова 1
3. форма слова 2
4. форма слова 3
Функция возвращает строку вида {число} {нужная форма}'''
def plural_form(number,*args):
    plural_arg = None
    if len(args) == 3:
        if number == 1:
            plural_arg = 0
        elif number > 1 and number < 5:
            plural_arg = 1
        elif number == 0 or number > 4:
            plural_arg = 2
        plural_form_text = str(number) + ' ' + args[plural_arg]
    else:
        plural_form_text = 'Не хватает аргументов функции!'
    return plural_form_text


print(plural_form(1, 'яблоко', 'яблока'))
print(plural_form(1, 'яблоко', 'яблока', 'яблок'))
print(plural_form(2, 'яблоко', 'яблока', 'яблок'))
print(plural_form(11, 'студент', 'студента', 'студентов'))
print(plural_form(15, 'студент', 'студента', 'студентов'))
print(plural_form(3, 'студент', 'студента', 'студентов'))
