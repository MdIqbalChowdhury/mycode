#!/usr/bin/env python3
a="Hello"
b="Sam"
c="my student number is"
num=230
d="\n*************************"
#num=input("my student number")
#'Hello Sam, my student number is 221.
# **********************************'
print(a + " " + b + ", " + c + " " + str(num) + "." + "\n************************")
print("'", a, b, ",", c, num, ".", end="\n***************************'\n")

print("' {} {},{} {}.\n*********************'\n".format(a, b, c, num))
print(f" '{a} {b}, {c} {num}.", end=f"{d}'\n")

#print(num)
#print(a, b, c, int(num))
#print (a, b, sep=" ")
#print(f" {a} {b} {c}:{num}")
