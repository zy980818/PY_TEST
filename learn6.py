#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/4/28 8:47
# @Author  : yan
# @File    : learn6.py
alien_0 = {'color':'green','points':5}
print(alien_0['color'])
print(alien_0['points'])
new_points = alien_0['points']
print("You just earned "+str(new_points)+" points!")
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
alien_0 = {}
alien_0 = {'color':'green'}
alien_0 = {'points':'5'}
alien_0['color'] = 'yellow'
print("The alien is now "+alien_0['color']+".")
alien_0 ={'x_position':0,'y_position':25,'speed':'medium'}
print(alien_0)
print("Original x-position: " + str(alien_0['x_position']))
# alien_0['speed'] = input("Please input speed: ")
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
print("*********************")
alien_0 = {'color': 'green', 'point' : 5}
print(alien_0)
del alien_0['color']
print(alien_0)
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
favorite_languages['yan'] = 'c'
print(favorite_languages)
print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      "." )
message = {
    'first_name' : 'zhao',
    'last_name' : 'yan',
    'age' : '22',
    'city' : 'xian',
}
print(message['first_name'].title() + message['last_name'].title())
for key,value in message.items():
    print('key:' + key)
    print('value:' + value)
favorite_numbers = {
    'yan' : '7',
    'li' : '2',
    'fei': '3',
    'kui' : '4',
    'yi' : '5',
    'chao' : '6',
}
for key,value in favorite_numbers.items():
    print('key:' + key)
    print('value:' + value)
print("111111111111111111111111111111111111")
dics = {
    'list' : '1',
    'var' : '2',
    'int' : '3',
    'boolean' : '4',
    'str' : '5',
    }
print(dics)
print("dics['lsist]:\n\t" + dics['list'])
print("list : " + dics['list'])
for key,value in dics.items():
    print("key :" + key.title())
    print("value :" + value)
    print(f"{key.title()} :\n\t{value}")
user_0 = {
    'username' : 'efermi',
    'first' : 'enrico',
    'last' : 'fermi',
}
for key,value in user_0.items():
    print("\nkey: " + key)
    print("value : " + value)
for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
          language.title() + ".")

for name in favorite_languages.keys():
    print(name.title())
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print(" Hi " + name.title() +
              ", I see you favorite language is " +
              favorite_languages[name].title() + "!")
for name in sorted(favorite_languages.keys()):
    print(name.title() + ",thank you for taking the poll")
for language in favorite_languages.values():
    print(language.title())
print("222222222222222")
for language in set(favorite_languages.values()):
    print(language.title())
print("**********learn6-4********")
dics = {'list':'列表','var':'变量','int':'整型','boolean':'布尔','str':'字符串'}
for k,v in dics.items():
	print(k + ':' + v + '\n')
rivers ={
    'nile' : 'egypt',
    'huanghe' : 'china',
    'changjiang' : 'china',
}
for river,nation in rivers.items():
    print("The " + river.title() +
          " runs through " + name.title())
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
}
lists = ['jen','phil','yan','ma']

for k in lists:
    if k in favorite_languages.keys():
        print(k + ",thank you")
    else:
        print(k + ",take")
alien_0 = {'color' : 'green', 'points' : '5'}
alien_1 = {'color' : 'yellow', 'points' : '10'}
alien_2 = {'color' : 'red', 'points' : '15'}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
    print(alien)
# 创建一个用于存储外星人的空表
aliens = []
for alien_number in range(30):
    new_alien = {'color' : 'green', 'points' : '5', 'speed' : 'slow'}
    aliens.append(new_alien)
for alien in aliens[:30]:
    print(alien)
print("...")
print("Total number of aliens : " + str(len(aliens)))
for alien in aliens[ : 3]:
    alien['color'] = 'yellow'
    alien['speed'] = 'medium'
    alien['points'] = '10'
for alien in aliens[0:5]:
    print(alien)
print("...")
for alien in aliens[0:10]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'fast'
for alien in aliens[:10]:
    print(alien)
print("...")
# 存储所点比萨信息
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushrooms','extra cheese'],
}
print("You ordered a " + pizza['crust'] +
      "-crust pizza" +
      " with the following toppings:")
for toppping in pizza['toppings']:
    print("\t" + toppping)
favorite_languages = {
    'yan' : ['python','ruby'],
    'li' : ['c'],
    'wang' : ['go','ruby'],
    'zhou' : ['PYTHO','java'],
}
for name,languages in favorite_languages.items():
    print("\n" + name.title() +
          "'s favorite language are :")
    for language in languages:
        print("\t" + language.title())

print(str(len(favorite_languages['yan'])))
print("1111111111111111111111"
      "22222222222222222222")
users = {
    'aeinstein' : {
        'first' : 'albert',
        'last' : 'einstein',
        'location' : 'princeton',
        },
    'mcurie' : {
        'first' : 'marie',
        'last' : 'curie',
        'location' : 'pairs',
        }
}
for username,user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())
yan1 = {'first_name' : 'z1', 'last_name' : 'y1', 'age' : '12', 'city' : 'xian'}
yan2 = {'first_name' : 'z2', 'last_name' : 'y2', 'age' : '13', 'city' : 'xian'}
yan3 = {'first_name' : 'z3', 'last_name' : 'y3', 'age' : '14', 'city' : 'xian'}
people = [yan1, yan2, yan3]
for info in people:
    name = info['first_name'].title() + " " + info['last_name'].title()
    print("Name: " + name)
    print("Age: " + info['age'] )
    print("City: " + info['city'])
dog = {'name':'dog1','age':'3'}
cat = {'name':'cat1','age':'4'}
bird = {'name':'birds','age':'1'}
pet = [dog,cat,bird]
for p in pet:
    print(p)
favorite_places = {
    'yan':['1','2','3'],
    'li':['4','5','6'],
    'fei':['7','8','9'],
    }
for k,v in favorite_places.items():
    print(k +":" )
    for v1 in v:
        print(v1)
cities = {
    'beijing':{
        'country':'china',
        'population':'100',
        'fact':'超级堵'
        },
    'guangzhou':{
        'country':'china',
        'population':'300',
        'fact':'超级堵2'
        },
    'shanghai':
        {'country':'china',
         'population':'200',
         'fact':'超级堵1'
         }
         }
for k,v in cities.items():
	print('城市：'+k+ '的信息： ')
	for k1,v1 in v.items():
		print(k1 + " : " + v1)