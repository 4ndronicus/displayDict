# displayDict
Prints the specified fields out of the list of dictionaries that is passed in.

## Assumptions ##
1. The list of dictionaries is in the format:
```
[
  {
    "<field_one>":"some string",
    "<field_two>":"some string",
    "<field_three>":"some string",
  },
  {
    "<field_one>":"some string",
    "<field_two>":"some string",
    "<field_three>":"some string",
  },
  {
    "<field_one>":"some string",
    "<field_two>":"some string",
    "<field_three>":"some string",
  },
]
```
Notice that all of the field names in each record are the same.

## Use Case ##
This class can be used to display a list of dictionaries.  Why is it called "displayDict" then?  Because I don't feel like fixing it. :)
This class can output the values as found in the results of a "scan" operation on a dynamodb table.

## Known Issues ##
1. Does not handle values that are dictionaries. No plans to fix this.

## Required Modules ##
None. :)

## Usage ##
1. Import the module.
1. Populate your list of dictionaries
1. Call the 'show' function

```
#!/usr/bin/python3

from displayDict import *

myList = [
        {
            "fruit":"apple",
            "description":"red fruit",
            "shipped_from":"Utah"
        },
        {
            "fruit":"banana",
            "description":"yellow fruit",
            "shipped_from":"Hawaii"
        },
        {
            "fruit":"blueberry",
            "description":"blue fruit",
            "shipped_from":"Florida"
        }
    ]

fields = ["fruit","description"]

showDict().show(myList,fields)
```
Or, if you want to reuse it, create an object from it and then call the 'show' function:
```
#!/usr/bin/python3

from displayDict import *

myList = [
        {
            "fruit":"apple",
            "description":"red fruit",
            "shipped_from":"Utah"
        },
        {
            "fruit":"banana",
            "description":"yellow fruit",
            "shipped_from":"Hawaii"
        },
        {
            "fruit":"blueberry",
            "description":"blue fruit",
            "shipped_from":"Florida"
        }
    ]

fields = ["fruit","description"]

o = showDict()

# ... do stuff ...

o.show(myList,fields)
```
Output:
```
----------------------------
| fruit     | description  |
----------------------------
| apple     | red fruit    |
| banana    | yellow fruit |
| blueberry | blue fruit   |
----------------------------
```
