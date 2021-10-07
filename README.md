# displayDict
Prints the specified fields out of the list of dictionaries that is passed in.  If no list of specified fields are passed in, it defaults to all fields.

## Assumptions ##
1. The list of dictionaries is in the format:
```
[
  {
    "<field_one>":"some string",
    "<field_two>":<boolean>,
    "<field_three>":<int>,
    "<field_four>":<list>
  },
  {
    "<field_one>":"some string",
    "<field_two>":<boolean>,
    "<field_three>":<int>,
    "<field_four>":<list>
  },
  {
    "<field_one>":"some string",
    "<field_two>":<boolean>,
    "<field_three>":<int>,
    "<field_four>":<list>
  }
]
```
1. All of the field names in each record are the same.

## Use Case ##
This class can be used to display a list of dictionaries.  Why is it called "displayDict" then?  Because I don't feel like fixing it. :)
This class can output the values as found in the results of a "scan" operation on a dynamodb table.

## Known Issues ##
* The data is a list of dictionaries.  In each dictionary is a set of key/value pairs.  If the value is a list, the values in the list must be of type string, integer, or boolean.  Additional levels of lists and dictionaries are not supported.
* Python passes the incoming list of dictionaries by reference and not by value. This is a problem because this class changes all item values in each dictionary to type 'string'. This means that when the 'show' function returns, inside the calling function, the list of dictionaries will be changed. Because of this, it is recommended to use the 'deepcopy' (from copy import deepcopy) function to make a copy of the list of dictionaries that you want to display, and pass the copy into the 'show' function. You don't need to do this if all item values are of type 'string'.

## Imports needed ##
```
from copy import deepcopy
```
## Usage ##
1. Import the module.
```
from displayDict import *
```
2. Populate your list of dictionaries
```
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
```
3. Define your fields if you wish
```
fields = ["fruit","quantity","isGMO","shipVia","cust","codes"]
```
1. Make a copy of the dictionary if you need to
```
listCopy = deepcopy(myList)
```
4. Call the 'show' function either statically like this

```
# Specify a list of fields
showDict().show(listCopy,fields)

# Print all fields
showDict().show(listCopy)
```
  Or, if you want to reuse it, create an object from it and then call the 'show' function:
```
o = showDict()

# Specify a list of fields
o.show(listCopy,fields)

# Print all fields
o.show(listCopy)
```
### Example ###
```
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
```
Output:
```
With only selected fields:
-------------------------------------------------------------------------------
| fruit     | quantity | isGMO | shipVia        | cust             | codes    |
-------------------------------------------------------------------------------
| apple     | 400      | True  | FEDEX          | True,False       | 2,8      |
| banana    | 1100     | False | FEDEX,UPS      | False,True,False | 981,94   |
| blueberry | 4000     | False | USPS,FEDEX,UPS | True             | 399,8484 |
-------------------------------------------------------------------------------

With all fields:
-------------------------------------------------------------------------------------------------------------
| fruit     | description  | shipped_from | isGMO | shipVia        | codes    | cust             | quantity |
-------------------------------------------------------------------------------------------------------------
| apple     | red fruit    | Utah         | True  | FEDEX          | 2,8      | True,False       | 400      |
| banana    | yellow fruit | Hawaii       | False | FEDEX,UPS      | 981,94   | False,True,False | 1100     |
| blueberry | blue fruit   | Florida      | False | USPS,FEDEX,UPS | 399,8484 | True             | 4000     |
-------------------------------------------------------------------------------------------------------------

Original list of dictionaries:
[{'fruit': 'apple', 'description': 'red fruit', 'shipped_from': 'Utah', 'isGMO': True, 'shipVia': ['FEDEX'], 'codes': [2, 8], 'cust': [True, False], 'quantity': 400}, {'fruit': 'banana', 'description': 'yellow fruit', 'shipped_from': 'Hawaii', 'isGMO': False, 'shipVia': ['FEDEX', 'UPS'], 'codes': [981, 94], 'cust': [False, True, False], 'quantity': 1100}, {'fruit': 'blueberry', 'description': 'blue fruit', 'shipped_from': 'Florida', 'isGMO': False, 'shipVia': ['USPS', 'FEDEX', 'UPS'], 'codes': [399, 8484], 'cust': [True], 'quantity': 4000}]

Copy of list of dictionaries:
[{'fruit': 'apple', 'description': 'red fruit', 'shipped_from': 'Utah', 'isGMO': 'True', 'shipVia': 'FEDEX', 'codes': '2,8', 'cust': 'True,False', 'quantity': '400'}, {'fruit': 'banana', 'description': 'yellow fruit', 'shipped_from': 'Hawaii', 'isGMO': 'False', 'shipVia': 'FEDEX,UPS', 'codes': '981,94', 'cust': 'False,True,False', 'quantity': '1100'}, {'fruit': 'blueberry', 'description': 'blue fruit', 'shipped_from': 'Florida', 'isGMO': 'False', 'shipVia': 'USPS,FEDEX,UPS', 'codes': '399,8484', 'cust': 'True', 'quantity': '4000'}]
```
