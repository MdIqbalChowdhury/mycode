#!/usr/bin/env python3
##sudo apt install python3-pip


import pyexcel
import datetime as dt
#Reqest data from user

def get_ip_data():
    input_ip = input("\nWhat is the IP address?")
    input_driver = input("What is the driver associated with this device?")
    d= { "IP":input_ip, "driver": input_driver}
    return d


mylistdict = []
print("Hello ! This program will make you a *.xls file ")

while(True):
    mylistdict.append(get_ip_data())
    keep_going = input("\n Would you like to add another value?Enter to Continue, or enter 'q' toquit")
    if(keep_going.lower() =='q'):
        break

today = dt.datetime.now().strftime("%Y-%m-%d")

filename=input("\n what is the name of the *.xls file?")
filename = today + "." + filename + ".xls"
pyexcel.save_as(records=mylistdict, dest_file_name=filename)
print(f"The file {filename} should be in your local directory")
#print( "The file " + filename + ".xls should be in your local directory")
print(mylistdict)

