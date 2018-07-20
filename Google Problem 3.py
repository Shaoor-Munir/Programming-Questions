array =  [1,2,3,2,1,4]

hashMap = dict()

for a in array:
    if a in hashMap:
        del hashMap[a]
        print("Deleted {}".format(a))
    else:
        hashMap[a] = 1

keys = hashMap.keys()

for k in keys:
    print(k)