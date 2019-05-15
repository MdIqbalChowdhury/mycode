#!/usr/bin/env python3
#open file
dnsfile= open("dnsservers.txt")

#create list of lines
dnslist = dnsfile.readlines()
for svr in dnslist:
    print(svr, end="")
dnsfile.close()

