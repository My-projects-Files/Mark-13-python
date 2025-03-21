#Regular expression for pattern search
import re #importing regular expressions
 
#To search a string
text= "Hi, How are you!"
pattern1= r"How"

search=re.search(pattern1,text)
if search:
    print("pattern found:",search.group())
else:
    print("pattern not found")


#To match a string(only starting of string is considered)
pattern2= r"Hi" #this will show as success

match=re.match(pattern2,text)
if match:
    print("pattern matched:",match.group())
else:
    print("pattern not matched")

#To replace a sring
replace=r"dude"

new_text= re.sub(pattern2,replace,text)
print("modified text:",new_text)

#to replace the string with x
ph_num="123-432-1456"
new_ph_num=re.sub(r"\d","X", ph_num)
print(new_ph_num)

#to find all the matches

text2="who are you,where are you"
pattern3=r"you"
find=re.findall(pattern3,text2)
print("Matching patterns:",find)

#To split the sring

pattern4=r"[ ,]"
split=re.split(pattern4,text2)
print("split result:",split)