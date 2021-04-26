#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/21 13:49
# @Author  : yan
# @File    : bicycles.py
bicycles = [ 'trek', 'cannodale', 'redline', 'specialized']
print(bicycles)
list = ['add','1',2,3]
print(list)
print(list[0].lower())
print(list[-4])
message = "my first bicycle was a " +bicycles[0].title()+"."
print(message)
name = ['yan','wang','li']
print(name[-1].title()+',ni hao')
message = 'I would like to own a bike'
print(message+' '+name[0])
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles[0])
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
print(motorcycles)
motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)
motorcycles.insert(0,'ducati')
print(motorcycles)
# del motorcycles[1]
# del motorcycles[0]
print(motorcycles)
# poped_motorcycles = motorcycles.pop()
print(motorcycles)
# print(poped_motorcycles)
# last_owned = motorcycles.pop()
# first_owned = motorcycles.pop(0)
# print("The last motorcycles I owned was a " + last_owned.title()+".")
# print("The last motorcycles I owned was a " + first_owned.title()+".")
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA "+ too_expensive.title()+" is too expensive for me.")
inv_list = ['yan', 'zhou', 'chao']
for inv_name  in inv_list:
    print('尊敬的：'+inv_name+'(先生/女士)，诚挚的邀请您参加今晚的宴会')
print(inv_list[0] +'因故无法赴宴')
inv_list[0] = 'li'
for inv_name in inv_list:
       print('尊敬的：'+inv_name+'(先生/女士)，诚挚的邀请您参加今晚的宴会')
inv_list.insert(0,'lei')
inv_list.insert(2,'liu')
inv_list.append('zhao')
for inv_name in inv_list:
    print('尊敬的：'+inv_name+'(先生/女士)，诚挚的邀请您参加今晚的宴会')
print('-----------------------')
print('抱歉，只能邀请两位嘉宾共进晚餐')
n = int(len(inv_list))
while n >2:
    last_name = inv_list.pop()
    print(last_name +',别来了')
    n = n - 1
for inv_name in inv_list:
    print(inv_name + '接着来！混蛋')
print("/********************/")
cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
#cars.sort(reverse=True)
print("Here is the original list:")
print(cars)
print("/********************/")
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the sorted list:")
print(sorted(cars,reverse=True))
print("\nHere is the original list again:")
print(cars)
print("/********************/")
print(cars)
cars.reverse()
cars.reverse()
print(cars)
print(len(cars))
traver_place = ["BeiJing","NanJing","XiAn","LuoYang","GuangZhou"]
print(traver_place)
print(sorted(traver_place))
print(sorted(traver_place,reverse=True))
print(traver_place)
traver_place.reverse()
print(traver_place)
traver_place.reverse()
print(traver_place)
traver_place.sort()
print(traver_place)
traver_place.sort(reverse=True)
print(traver_place)
print('共邀请了：'+str(len(inv_list))+'位宾客！')
print(str(len(motorcycles)))
print(motorcycles[2])
