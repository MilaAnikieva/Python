# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.

fruts = ['яблоко', 'груша', 'апельсин', 'лимон', 'папая']

x = max(fruts, key=len)
print(len(x))


for z in range(len(fruts)):
    num = f'{z + 1}.'
    f_n = fruts[z]
    print(num, f_n.rjust(len(x), ' '))


# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.


list_1 = [1, 2, 3, 5, 6]
list_2 = [2, 6, 0, 9, 4]

for i in list_2:
    for j in list_1:
        if i == j:
            list_1.remove(j)

print(list_1)

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

numb_list = [1, 2, 3, 4, 5]
for g in range(len(numb_list)):
    if numb_list[g] % 2 == 0:
        numb_list[g] /= 4
    else:
        numb_list[g] *= 2

print(numb_list)
