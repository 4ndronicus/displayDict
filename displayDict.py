#*******************************************************************************
# Class Name: showDict
# By: Scott Morris <smmorris@verisk.com>
# Date: 2021-09-28
#
# Description: This class receives a list of dictionaries and prints the
#   specified fields from out of those dictionaries
#
# Required imports: None
#
# Usage Example:
#
# import displayDict as displayDict
# 
# myList = [
#         {
#             "fruit":"apple",
#             "description":"red fruit",
#             "shipped_from":"Utah"
#         },
#         {
#             "fruit":"banana",
#             "description":"yellow fruit",
#             "shipped_from":"Hawaii"
#         },
#         {
#             "fruit":"blueberry",
#             "description":"blue fruit",
#             "shipped_from":"Florida"
#         }
#     ]
# 
# fields = ["fruit","description"]
# 
# displayDict.showDict().show(myList,fields)
#
#*******************************************************************************
class showDict:

#*******************************************************************************
# Function Name: formatField
# Description: Creates a field in a row for displaying on the screen.
# Post-conditions: The field is created and returned.
# Expected parameters:
#   o me - the class
#   o inField - string - The string we want to format for display
#   o fieldSize - integer - How many characters long it needs to be
# Returns: The formatted version of the field ready for output.
# Usage Example:
# fieldVal = me.formatField("apple",27)
#*******************************************************************************
    def formatField(me,inField,fieldSize):
        return "| " + inField.ljust(fieldSize) + ' '

#*******************************************************************************
# Function Name: printField
# Description: Outputs a field
# Post-conditions: The field has been displayed to the screen.
# Expected parameters:
#   o me - the class
#   o inField - string - The value to be displayed
#   o fieldSize - integer - how many characters long it should be
# Usage Example:
# me.printField("apple",27)
#*******************************************************************************
    def printField(me,inField,fieldSize):
        print(me.formatField(inField,fieldSize),end='')

#*******************************************************************************
# Function Name: printHeader
# Description: Displays the field names of the data that will be printed out
# Prerequisites: Size requirements need to have been computed 
# Post-conditions: The header has been displayed
# Expected parameters:
#   o dataDict - list of dictionaries - the list of fields we want to print
#   o inDict - dictionary - fields and corresponding lengths - in the format:
# {"<fieldname>":<fieldlength>,"<fieldname>":<fieldlength>}
# Usage Example:
# me.printHeader(fieldList,dataDict)
#*******************************************************************************
    def printHeader(me,dataDict,inDict):
        outStr = ''
        for field in dataDict:
            outStr += me.formatField(field, inDict[field])
        lineLen = len(outStr) + 1 # for additional | char
        print('-' * lineLen)
        print(outStr + '|')
        print('-' * lineLen)

#*******************************************************************************
# Function Name: printFooter
# Description: Prints a line of dashes of the proper length
# Post-conditions: The line has been printed
# Expected parameters:
#   o inDict - dictionary - fields and corresponding lengths - in the format:
# {"<fieldname>":<fieldlength>,"<fieldname>":<fieldlength>}
# Usage Example:
# me.printFooter(sizeCt)
#*******************************************************************************
    def printFooter(me,inDict):
        totLen = 0
        for i in inDict:
            totLen += inDict[i] + 3 # for additional chars in fields
        totLen += 1 # for last | char on line
        print('-' * totLen)

#*******************************************************************************
# Function Name: printRec
# Description: Prints out the requested fields from the specified dictionary
# Prerequisites: Size requirements need to have been computed
# Post-conditions: The row of data has been displayed to the screen
# Expected parameters:
#   o me - this object
#   o inRec - dictionary - contains the record you wish to print
#   o sizeCt - dictionary - fields and corresponding lengths - in the format:
# {"<fieldname>":<fieldlength>,"<fieldname>":<fieldlength>}
#   o fields - list - contains the fields we want to print
# Usage Example:
# me.printRec(dictRec,sizeCt,fieldList)
#*******************************************************************************
    def printRec(me,inRec,sizeCt,fields):
        for field in fields:
            me.printField(inRec[field],sizeCt[field])
        print('|')

#*******************************************************************************
# Function Name: show
# Description: Recieves a list of dictionaries and a list of fields.  It prints
#   out a simple table showing the specified fields from the dictionary list.
# Required imports: None
# Prerequisites: Should already have populated a list of dictionaries, such as
#   with using scan() on a dynamodb table, for example.
# Post-conditions: The contents of the list of dictionaries has been displayed
# Expected parameters:
#   o me - this object
#   o inDict - list of dictionaries - The data you wish to display
#   o fieldList - list - The list of fields you wish to display - in the format:
# ["<fieldname>","<fieldname>","<fieldname>"]
#       - you can put as many fields as you want, but they must exist in all
#           of the records
# Returns: None
# Usage Example: (See class usage example at the top)
#*******************************************************************************
    def show(me,inDict,fieldList):

        sizeCt = {}

	# Initialize the line length tracker
        for i in range(len(fieldList)):
            sizeCt[fieldList[i]]=0

        # Go through each of the dictionaries - convert values to strings
        for i in range(len(inDict)):
            for field in fieldList:
                if type(inDict[i][field]) in [bool,int]:
                    inDict[i][field] = str(inDict[i][field])


	# Calculate the longest value of each requested field
        for rec in inDict:
            for field in fieldList:
                if len(rec[field]) > sizeCt[field]:
                    sizeCt[field] = len(rec[field])

        # Just in case the field names are longer than the content
        for field in fieldList:
            if len(field) > sizeCt[field]:
                sizeCt[field] = len(field)

        # Output the header
        me.printHeader(fieldList,sizeCt)

        # Output the records
        for i in range(len(inDict)):
            me.printRec(inDict[i],sizeCt,fieldList)

        # Output the footer
        me.printFooter(sizeCt)
