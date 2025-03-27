#set funtion inbuild

a={1,2,3,4}
b={3,6,2,7}

# adding the element in the set
a.add(8)
print(a)

#removing the elements in the set
b.remove(6)
print(b)

#set operations two sets 
uni=a.union(b) #To union two a and b
inter= a.intersection(b)#To intersection two sets
diff=a.difference(b) #To diff between two sets
print(f'union of two sets {uni}'," ",f'intersection of two sets {inter}'," ",f'differnce between two set {diff}')
