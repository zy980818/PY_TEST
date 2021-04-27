#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/27 15:38
# @Author  : yan
# @File    : learn5.py
cars = ['audi','bwm','subaru','toyota']
for car in cars:
    if car == 'bwm':
        print(car.upper())
    else:
        print(car.title())
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies")
game_active = True
can_edit = False
age = 19
if age >= 18:
    print("you are old enough to vote!")
    print("Have you registered to vote yet?")
age = 17
if age >= 18:
    print("You are old enough to vote!")
    prinr("Have you registered to vote yet?")
else:
    print("Sorry,you are too young to vote.")
    print("Please regiser to vote as soon as you turn 18!")
age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10.")
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5
print("Your admission cost is $"+str(price)+".")
print('/******************/')
requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms'in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
alien_color = ['green']
if 'green' in alien_color:
    print("玩家获得了5个点The player get 5 points")
alien_color = ['yellow']
if 'green' in alien_color:
    print("The player get 5 points")
alien_color = ['green']
if 'green' in alien_color:
    print("The player get 5 points")
else:
    print("The player get 10 points")
if 'green'not in alien_color:
    print("The player get 10 points")
else:
    print("The player get 5 points")
alien_color = ['red']
if 'green' in alien_color:
    p = 5
elif 'yellow' in alien_color:
    p = 10
else:
    p = 15
print("The player get "+str(p)+" points.")
# ages = input('Please input your age:')
# age = int(ages)
age = 12
status = ['baby','toddler','children','teenager','adult','old man']
if age < 2:
    sta = status[0]
elif age >= 2 and age < 4:
    sta = status[1]
elif age >= 4 and age <13:
    sta = status[2]
elif age >= 13 and age < 20:
    sta = status[3]
elif age >= 20 and age < 65:
    sta = status[4]
elif age >= 65:
    sta = status[5]
print("He is a "+str(sta)+".")

favorite_fruits = ['apple','banana','orange']
if 'apple' in favorite_fruits:
    print("you really like apple")
if "orange" in favorite_fruits:
    print("you reallly like orange")
if 'strawberry'in favorite_fruits:
    print("you really like strawberrry")
requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,we are out of green pepper right now.")
    else:
        print("Adding "+requested_topping+".")

print("\n Finished making your pizza!")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding "+requested_topping+".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure want a plain pizza? ")
available_toppings = ['mushrooms','olives','green peppers','pepperoni','pineapple','extra cheese']
requested_toppings = ['french fries','mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding "+requested_topping+".")
    else:
        print("Sorry,we don't have "+requested_topping+".")
    print("\nFinished making your pizza!")
print("******************************")
user_names = ['admin','a','b','c','d','e']
user_names = []
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
             print("Hello admin,would you like to see a status report?")
        else:
             print("Hello "+str(user_name)+", thank you for logging in again")
else:
     print("We need to find some users!")
cuurent_users = ['addsd','ssss','ssad','aaaa','cccc','bbbb']
new_users =['ADDSD','Sssss','s','vdvddv','dds']
for new_user in new_users:
    if new_user.lower() in cuurent_users:
        print(new_user+" This username has been used!")
    else:
        print(new_user+" This username has  not been used!")
print("****************************")
nums = list(range(1,10))
for num in nums:
    if num == 1:
        print(str(num)+'st')
    elif num == 2:
        print(str(num)+'nd')
    elif num == 3:
        print(str(num)+'rd')
    else:
        print(str(num)+'th')
print(str(nums))