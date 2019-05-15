#!/usr/bin/env python3

channel_list = []

while(True):
    print("what Channel Do you want: ")
    channel =int(input())
    if(channel >=1 and channel > 20):
        print(" you should purchase our standard package")
        channel_list.append(channel)

    elif(channel > 50 and channel <=100):
        print("you should purchase our premium package")
        channel_list.append(channel)
    
    elif(channel >100 and channel <=200):
        print("You should purchase our Premium HD package")
        channel_list.append(channel)
    
    elif(channel >200 and channel <=600)
       print("you should purchase our extra package")
       channel_list.append(channel)
    else:
        #print("would you like to price a different channel? Type 'No' to quit")
        end = input("would you like to price a diffeent channel? Type no to quit)
        if end.lower() =="q":
            break
print("Max channel:", max(channel_list)


