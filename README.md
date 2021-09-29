# displayDict
Prints the specified fields out of the list of dictionaries that is passed in.

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
1. The data is a list of dictionaries.  In each dictionary is a set of key/value pairs.  This module does not handle values that are dictionaries.  String, boolean, and integer values are supported.

## Required Modules ##
None. :)

## Usage ##
1. Import the module.
1. Populate your list of dictionaries
1. Call the 'show' function

```
#!/usr/bin/python3

from modules.displayDict import *

myList = [
        {
            "fruit":"apple",
            "description":"red fruit",
            "shipped_from":"Utah",
            "isGMO":True,
            "shipVia":["USPS","FEDEX"],
            "quantity":400
        },
        {
            "fruit":"banana",
            "description":"yellow fruit",
            "shipped_from":"Hawaii",
            "isGMO":False,
            "shipVia":["FEDEX","UPS"],
            "quantity":1100
        },
        {
            "fruit":"blueberry",
            "description":"blue fruit",
            "shipped_from":"Florida",
            "isGMO":False,
            "shipVia":["USPS","FEDEX","UPS"],
            "quantity":4000
        }
    ]

fields = ["fruit","quantity","isGMO","shipVia"]

showDict().show(myList,fields)
```
Or, if you want to reuse it, create an object from it and then call the 'show' function:
```
#!/usr/bin/python3

from modules.displayDict import *

myList = [
        {
            "fruit":"apple",
            "description":"red fruit",
            "shipped_from":"Utah",
            "isGMO":True,
            "shipVia":["USPS","FEDEX"],
            "quantity":400
        },
        {
            "fruit":"banana",
            "description":"yellow fruit",
            "shipped_from":"Hawaii",
            "isGMO":False,
            "shipVia":["FEDEX","UPS"],
            "quantity":1100
        },
        {
            "fruit":"blueberry",
            "description":"blue fruit",
            "shipped_from":"Florida",
            "isGMO":False,
            "shipVia":["USPS","FEDEX","UPS"],
            "quantity":4000
        }
    ]

fields = ["fruit","quantity","isGMO","shipVia"]

fields = ["fruit","quantity","isGMO"]

o = showDict()

# ... do stuff ...

o.show(myList,fields)
```
Output:
```
-------------------------------------------------
| fruit     | quantity | isGMO | shipVia        |
-------------------------------------------------
| apple     | 400      | True  | USPS,FEDEX     |
| banana    | 1100     | False | FEDEX,UPS      |
| blueberry | 4000     | False | USPS,FEDEX,UPS |
-------------------------------------------------
```
