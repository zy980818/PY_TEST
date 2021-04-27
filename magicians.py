#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/25 11:13
# @Author  : yan
# @File    : magicians.py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, "+ magician.title()+ ".\n")
print("Thank you,everyone.That was a great magic show!")
pizzas = ['pizzaA','pizzaB','pizzaC']
for temp in pizzas:
    print(temp)
for temp2 in pizzas:
    print('I like: '+temp2+ '!')
print('老喜欢吃披萨了，比如：'+str(pizzas)+',I really love pizza!')
print(str(pizzas))
animals = ['dog','cat','bird']
for temp in animals:
    print(temp)
print('A '+animals[0]+' would make a great pet1')
print('A '+animals[1]+' would make a great pet2')
print('A '+animals[2]+' would make a great pet3')
print('Any of these animals would make a great pet')
for value in range(1,6):
    print(str(value))
number = list(range(1,6))
print(number)