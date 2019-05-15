#!/usr/bin/env python3

#This library allows us to generate uuid values.

import uuid
howmany= int(input("How Many UUIDs should be generated?"))
print("Generating UUIDs...")
for rando in range(howmany):
    print(uuid.uuid4())

