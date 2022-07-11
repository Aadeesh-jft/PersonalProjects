import string


def matchingStrings(strings, queries):
    # Write your code here
    returnArray = []
    for i in queries:
        returnArray.append(strings.count(i))
    return returnArray
    