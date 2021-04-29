#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 18:50
# @Author  : yan
# @File    : learn7.py
# message = input("Tell me something,and I wil repeat it back to you: \n\t")
# print(message)
# name = input("Please enter your name: ")
# print("Hello, " + name + "!")
prompt = "If you tell me who you are,we can personalize the messages you see."
prompt += "\nWhat is your first name?"
# name = input(prompt + "\n")
# print("Hello, " + name + "!")
# number = input("Enter a number,and I'll tell you if it's even or  odd:")
# number = int(number)
# if number % 2 == 0:
#     print("\nThe number" + str(number) + " is even.")
# else:
#     print("\nThe number" + str(number) + " is odd")
# car = input("What kind of car you like to rent?")
# print("\nLet me see if I can find you a " + str(car).upper() + ".")
# people = input("Please tell me how many people will have dinner: ")
# num = int(people)
# if num > 8:
#     print("\nWithout empty desk")
# else:
#     print("\nhave desk")
# num = input("Please enter a number: ")
# number = int(num)
# if number % 10:
#     print( num + " is  an integer multiple of ten ")
# else:
#     print("no")
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
# prompt = "\nTell me something,and I will repeat it back to yoj: "
# prompt += "\nEnter 'quit' to end the program.\n"
# message = ''
# while message != 'quit':
#     message = input(prompt)
#     if message != 'quit':
#         print(message)
# prompt = "\nTell me something,and I will repeat it back to yoj: "
# prompt += "\nEnter 'quit' to end the program.\n"
# active = True
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False
#     else:
#         print(message)
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     else:
#         print(current_number)
# prompt = ("Please enter ingredients list .")
# prompt += ("\nEnter 'quit' to end the program.\n:")
# toppings = ""
# while toppings != 'quit':
#     toppings = input(prompt)
#     print("We will add this to the pizza\n")
# info = ("Please enter your age ,we will let know how much it costs\n: ")
# active = True
# age = ""
# while active:
#     age = input(info)
#     age = int(age)
#     if age > 0 and age < 3:
#         print("FREE")
#     elif age >= 3  and age < 12:
#         print("10$")
#     elif age >= 12:
#         print("15$")
# unconfirm_users = ['alice','brain','candace']
# confirm_users = []
# while unconfirm_users:
#     current_user = unconfirm_users.pop()
#     print("Verifying user:" + current_user.title())
#     confirm_users.append(current_user)
# print("\nThe following users have been confirmed :")
# for confirm in confirm_users:
#     print(confirm.title())
# num = [1,2,3,4,5,2,2,2,26,7,8]
# print(num)
# while 2 in num:
#     num.remove(2)
# print(num)
# responses = {}
# polling_active = True
# while polling_active:
#     name = input("\n What is your name?")
#     response = input("Which mountain would you like climb someday?")
#     responses[name] = response
#
#     repeat = input("Would you like to let another person respon?(yes/no)")
#     if repeat == 'no':
#         polling_active = False
# print("\n---Poll Result ---")
# for name,response in responses.items():
#     print(name + " would like to climb " + response + ".")
sandwich_orders = ['Tuna sandwich','Ham cheese sandwich','Chicken wandwich','pastrami','pastrami','pastrami']
finished_sandwiches = []
# while sandwich_orders:
#     current_orders = sandwich_orders.pop()
#     print("I made your " + current_orders.title() + ".")
#     finished_sandwiches.append(current_orders)
#
# print("\nAll the sandwiches have been finished")
# for finished_sandwiche in finished_sandwiches:
#     print(finished_sandwiche.title())
# print("pastrami is 0")
# while sandwich_orders:
#     if 'pastrami' in sandwich_orders:
#         sandwich_orders.remove('pastrami')
#     else:
#          current_orders = sandwich_orders.pop()
#          print("I made your " + current_orders.title() + ".")
#          finished_sandwiches.append(current_orders)
# for finished_sandwiche in finished_sandwiches:
#     print(finished_sandwiche.title())
responses={}
active = True
while active:
     # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")
    # 将答卷存储在字典中
    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        active = False
# 调查结束，显示结果
print("\n---  Results ---")
for name, response in responses.items():
    print(name + " would like to visit " + response + ".")


