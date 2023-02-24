# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

# num = input('Enter a three-digit number: ')
# res = 0
# if len(num) == 3:
#    for i in num:
#       res += int(i)
#    print(res)
# else:
#    print('You entered a non-three-digit number')


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?
# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# S = int(input("Enter the total number of cranes: "))
# if not S % 6:
#     x = S // 6
#     print(f'Katya did {x * 4} ')
#     print(f'Seryozha did {x} ')
#     print(f'Petya did {x}')


# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет
# с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр
# равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

# s = input('Enter the six-digit ticket number: ')
# if len(s) != 6:
#    print(f'The number {s} is not six-digit')
# else:
#    res1 = 0
#    res2 = 0
#    for i in range(len(s)//2):
#        res1 += int(s[i])
#        res2 += int(s[len(s)//2 + i])
#    if res1 == res2:
#        print(f'{s} lucky number, congratulations!')
#    else:
#        print(f'{s} unfortunately, not a lucky number')


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Enter the first side: '))
m = int(input('Enter the second side: '))
k = int(input('Enter the number of slices you want to break off: '))
if k % n == 0 or k % m == 0:
    print('yes')
else:
    print('no')
