#!/usr/bin/env python3

from displayDict import *
from copy import deepcopy

myList = [
        {
            "fruit":"apple",
            "description":"red fruit",
            "shipped_from":"Utah",
            "isGMO":True,
            "shipVia":["FEDEX"],
            "codes":[2,8],
            "cust":[True,False],
            "quantity":400
        },
        {
            "fruit":"banana",
            "description":"yellow fruit",
            "shipped_from":"Hawaii",
            "isGMO":False,
            "shipVia":["FEDEX","UPS"],
            "codes":[981,94],
            "cust":[False,True,False],
            "quantity":1100
        },
        {
            "fruit":"blueberry",
            "description":"blue fruit",
            "shipped_from":"Florida",
            "isGMO":False,
            "shipVia":["USPS","FEDEX","UPS"],
            "codes":[399,8484],
            "cust":[True],
            "quantity":4000
        }
    ]

fields = ["fruit","quantity","isGMO","shipVia","cust","codes"]

o = showDict()

# ... do stuff ...

# Necessary because values of dictionary items are not all strings
listCopy = deepcopy(myList)

print("With only selected fields:")
o.show(listCopy,fields)

print("\nWith all fields:")
o.show(listCopy)

print("\nOriginal list of dictionaries:")
print(myList)

print("\nCopy of list of dictionaries:")
print(listCopy)
