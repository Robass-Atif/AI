def findAlphabetically(arr):
    ret=arr.split()
    ret.sort()
    return ret[-1]
print(findAlphabetically("what is the last sentence in word"))

