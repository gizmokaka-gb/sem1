# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

S = int(input("Введите количество готовых журавливов: "))
boys = S // 6
Kate = boys * 4
teacher = S - Kate - boys * 2
if S < 6:
    print("На журавликов бумаги не хватило!")
elif teacher == 0:
    print(f'Петя и Сережа сделали по {boys} шт, а Катя целых {Kate}!')
else:
    print(f'Петя и Сережа сделали по {boys} шт, а Катя целых {Kate}! {teacher} шт сделал учитель для примера.')