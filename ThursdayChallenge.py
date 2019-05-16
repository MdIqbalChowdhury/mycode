#!/usr/bin/python3

#use this code...


import random
thursday=[]
for x in range(10000):
    thursday.append(random.randint(1,600))


def sort_it(chan):

    basic = []
    standard = []
    premium =[]
    premiumHD = []
    extras =[]
    for x in chan:
        if x <= 20:
            basic.append(x)
        elif x <= 50:
            standard.append(x)
        elif x <=100:
            premium.append(x)
        elif x <=200:
            premiumHD.append(x)
        else:

            extras:append(x)
   
    print(len(basic))
    print(len(standard))
    print(len(premium))
    print(len(premiumHD))
    print(len(extras))

sort_it(thursday)



    
    
    
    
    
#      if item >=1 and item<=20
#      basic.append(item)
 #    elif item >20 and item <=50
#     standard.append(item)
# elif item >50 and iteam <=100
# premium.append(item)
# elif iteam >100 and item <=200
# premiumHD.append(item)
 #else

#sort_it(thursday)

