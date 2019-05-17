#!/usr/bin/env python3
""" Alta3 Reasearch | Author "RZFeeser@alta3.com"""

#imports a;ways go at the top of code

import requests

def main():
    """Run time code"""
    #create r which is our request object
    r= requests.get("https://cat-fact.herokuapp.com/facts")
    print(dir(r))
main()

