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
Notice that all of the field names in each record are the same.

## Use Case ##
This class can be used to display a list of dictionaries.  Why is it called "displayDict" then?  Because I don't feel like fixing it. :)
This class can output the values as found in the results of a "scan" operation on a dynamodb table.

## Known Issues ##
1. The data is a list of dictionaries.  In each dictionary is a set of key/value pairs.  If the value is a list, the values in the list must be of type string, integer, or boolean.  Additional levels of lists and dictionaries are not supported.

## Required Modules ##
None. :)

## Usage ##
1. Import the module.
```
from displayDict import *
```
1. Populate your list of dictionaries
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
1. Define your fields if you wish
```
fields = ["fruit","quantity","isGMO","shipVia","cust","codes"]
```
1. Call the 'show' function either statically like this

```
showDict().show(myList,fields)
```
Or, if you want to reuse it, create an object from it and then call the 'show' function:
```
o = showDict()
o.show(myList,fields)
```

````
#!/usr/bin/python3

from modules.displayDict import *

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

o.show(myList,fields)
```
Output:
```
-------------------------------------------------------------------------------
| fruit     | quantity | isGMO | shipVia        | cust             | codes    |
-------------------------------------------------------------------------------
| apple     | 400      | True  | FEDEX          | True,False       | 2,8      |
| banana    | 1100     | False | FEDEX,UPS      | False,True,False | 981,94   |
| blueberry | 4000     | False | USPS,FEDEX,UPS | True             | 399,8484 |
-------------------------------------------------------------------------------
```
