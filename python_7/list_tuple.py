#List
bucket=["bucket_1","bucket_2","bucket_3"]

#tuple
admin=("sai","kamal")

#Indexing
element=bucket[0]
user=admin[1]
print (element,user)

#length
length_1=len(bucket)
length_2=len(admin)
print(length_1,length_2)

#append
bucket.append("bucket_8")

#Remove
bucket.remove("bucket_2")

print(bucket)

#slice a list
sli=bucket[1:3]
print(sli)

#concat
new_bucket=bucket + ["bucket_6","bucket_9"]
print(new_bucket)

#sort
new_bucket.sort()
print(new_bucket)

#checking
present= "bucket_2" in bucket
print(present)

#tuple Packing and unpacking

def value():
    return(4,8)

x,y =value()
print(x,y)
