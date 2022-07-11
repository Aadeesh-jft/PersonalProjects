l1 = [1, 2, 4]
l2 = [1, 3, 4]
#output = [1, 1, 2, 3, 4, 4]
head1 = l1[0]
head2 = l2[0]
returnList = []
lenl1 = len(l1)
lenl2 = len(l2)

if((lenl1 == 0)):
    print(l2)
elif (lenl2 == 0):
    print(l1)
elif ((lenl1 == 0) and (lenl2 == 0)):
    emptyList = []
    print(emptyList)
else:
    l = lenl1
    if (lenl1 >= lenl2):
        l = lenl2
    for i in range(l):
        if (l1[i] <= l2[i]):
            returnList.append(l1[i])
            returnList.append(l2[i])
        else:
            returnList.append(l2[i])
            returnList.append(l1[i])
    if ((lenl1 < lenl2)):
        returnList.append(l2[len[l1]:])
    elif (lenl1 > lenl2):
        returnList.append(l1[len[l2]:])
print(returnList)