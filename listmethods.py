

alist = [10,20]
alist.append(30)
alist.append(40)
print("After appending:", alist)
#alist.clear()
#print(alist)
alist.extend([50,60,70,80,10,10])
print("After extending:", alist)

print("Count of 10 :", alist.count(10))

getindex = alist.index(20)
print("INdex of 20 :", getindex)

# reverse happends in-place
alist.reverse()
print(alist)

alist.sort()
print(alist)

popitem = alist.pop(5)
print("removed elmeent :", popitem)
print("after removing :" , alist)






