# Задание - 1
# Вам даны 2 списка одинаковой длины, в первом списке имена людей, во втором зарплаты,
# вам необходимо получить на выходе словарь, где ключ - имя, значение - зарплата.
# Запишите результаты в файл salary.txt так, чтобы на каждой строке было 2 столбца,
# столбцы разделяются пробелом, тире, пробелом. в первом имя, во втором зарплата, например: Vasya - 5000


def card_index(name, money):
	return dict(zip(name, money))


names = ['Иван', 'Петр', 'Ирина', 'Ольга', 'Кирилл']
salary = [2000000, 90000, 15000, 70000, 25000]

workers = card_index(names, salary)

with open('salary.txt', 'w') as f:
	for key,val in workers.items():
		f.write('{} - {}\n'.format(key,val))

# После чего прочитайте файл, выведите построчно имя и зарплату минус 13% (налоги ведь),
# Есть условие, не отображать людей получающих более зарплату 500000, как именно
#  выполнить условие решать вам, можете не писать в файл
# можете не выводить, подумайте какой способ будет наиболее правильным и оптимальным,
#  если скажем эти файлы потом придется передавать.


with open('salary.txt', 'r') as f:
	workers_list = f.readlines()

salary_tax = []
for i in range(len(workers_list)):
	a = workers_list[i].split()
	salary_tax.append(int(a[-1]) * 0.87)

workers_tax = card_index(names, salary_tax)

workers_tax_sort = workers_tax.copy()
for i in workers_tax:
	if workers_tax.get(i) > 500000:
		workers_tax_sort.pop(i)

with open('salary.txt', 'a') as f:
	f.write('\n\nПосле вычета налога и сортировки\n\n')
	for key,val in workers_tax_sort.items():
		f.write('{} - {}\n'.format(key,val))

