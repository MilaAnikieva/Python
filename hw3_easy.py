# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


def anketa(name, age, city):
	return '{}, {} год(а), проживает в городе {}.'.format(name, age, city)


name = input('Введите имя ')
age = int(input('Введите возраст '))
city = input('Введите город проживания ')

print(anketa(name, age, city))

#Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них

def max_numb(x, y, z):
	numb = x
	if y > numb:
		numb = y
	elif z > numb:
		numb = z
	return numb


x, y, z = int(input()), int(input()), int(input())
print('Максимальное число:', max_numb(x, y, z))

#Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def max_len_str(*args):
	return max(args, key=len)


print('Самая длинная строка: ', max_len_str('GeekBrains', 'Python', 'Lesson 3', 'Home work'))
