# Задание - 1
# Давайте опишем пару сущностей player и enemy через словарь,
# который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health - 100,
# damage - 50.
# Поэксперементируйте с значениями урона и жизней по желанию.
# Теперь надо создать функцию attack(person1, person2), аргументы можете указать свои,
# функция в качестве аргумента будет принимать атакующего и атакуемого,
# функция должна получить параметр damage атакующего и отнять это количество
# health от атакуемого. Функция должна сама работать с словарями и изменять их значения.

import random


def attack(x, y):
    health_1 = x.get('health') - random.randint(1, y.get('damage'))
    health_2 = y.get('health') - random.randint(1, x.get('damage'))
    x['health'] = health_1
    y['health'] = health_2
    return x, y


def date_player(z):
    date = f'Игрок {z.get("name")}, здоровье - {z.get("health")}, урон - {z.get("damage")}'
    return date


player_1 = {'name': input('Введите имя первого игрока '), 'health': 100, 'damage': 50}
player_2 = {'name': input('Введите имя второго игрока '), 'health': 100, 'damage': 50}

answer = input('Начнем бой? ')
i = 1
while player_1.get("health") > 0 and player_2.get("health") > 0 and answer.lower() == 'да':
    print('Ранунд', i)
    print(date_player(player_1))
    print(date_player(player_2))
    attack(player_1, player_2)
    i += 1
    if player_1.get("health") > 0 and player_2.get("health") > 0:
        answer = input('Продолжим? ')


if player_1.get("health") <= 0:
    print(f'Игра окончена. Победил игрок {player_2.get("name")} со здоровьем - {player_2.get("health")}!')
elif player_2.get("health") <= 0:
    print(f'Игра окончена. Победил игрок {player_1.get("name")} со здоровьем - {player_1.get("health")}!')
else:
    print(f'Игра окончена! {player_1.get("name")} со здоровьем - {player_1.get("health")}, {player_2.get("name")} со здоровьем - {player_2.get("health")}\nПобедителя нет!')
