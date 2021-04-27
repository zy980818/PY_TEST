#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 9:19
# @Author  : yan
# @File    : even_numbers.py
import time
start = time.clock()
# 在此导入time库，并在开头设置开始时间
even_numbers = list(range(2,11,2))
print(even_numbers)
squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
    print(squares)
squares = [value**2 for value in range(1,11)]
print(squares)
for num in list(range(1,21)):
    print(num)
temp = list(range(1,1000001))
#for t in temp:
#    print(t)
print(min(temp))
print(max(temp))
print(sum(temp))
end = time.clock()
# 在程序运行结束的位置添加结束时间
print("运行耗时", end-start)
temp = list(range(1,20,2))
for t in temp:
    print(t)
# 再将其进行打印，即可显示出程序完成的运行耗时
temp = list(range(3,31))
temp2 = []
for t in temp:
    if t % 3 == 0:
        temp2.append(t)
print(temp2)
temp = list(range(1,11,1))
temp2 = []
for t in temp:
    t = t ** 3
    temp2.append(t)
print(temp2)
temp = [ value ** 3 for value in range(1,11)]
print(temp)
# players.py
players = ['charles','martina','michael','florence','eli']
print(players[1:])
print(players[-3:])
print("Here are the first three player on my team:")
for player in players[:3]:
    print(player.lower())
# foods.py 75
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print("The first three items in the list are:")
print(my_foods[0:3])
my_foods.append('1')
my_foods.append('3')
print(my_foods)
print("Three items from the middle of the list are:")
print(my_foods[1:4])
print("The last three items in the list are:")
print(my_foods[-3:])
pizzas = ['pizzaA','pizzaB','pizzaC']
friend_foods = pizzas[:]
pizzas.append('1')
friend_foods.append('2')
print('My favorite pizzas are')
for p in pizzas:
    print(p)
print("My frirnd's favorite pizzas are:")
for f_p in friend_foods:
    print(f_p)
# dimension.py
dimension = (20,50)
print(dimension[0])
print(dimension[1])
dimension = (40,100)
for dim in dimension:
    print(dim)
food = ('1','2','3','4','5')
for f in food:
    print(f)
food = ('1','2','4','6','7')
for f in food:
    print(f)
