#!/usr/bin/env python3

vowels = "aeiouAEIOU"
NoV = []
NoC = []
v=0
c=0


def my_math(a,b):
    ab=a*b
    print(ab)
    return ab

def my_string(MyString):
   for letter in Mystring:
       if letter in vowels:
           NoV.append(letter)
           v= v+1
       else:
           NoC.append(letter)
           c=c+1

return v,c 
print("Vowels: ", NoV, "Consonants: " NoC)
    
   
my_math(2,5)
my_string(" Look Out! I have learned enough Python to be dangerous!")
