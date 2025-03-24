#concating or joining two strings
str1= "hi"
str2= "dude"
result = str1+ " "+str2
print (result)

#To print length of two strings
text= " Hello World, How are You " #it counts spaces and , as well
length= len(text)
print(length)

#To print given string as lowercase or uppercase leters
upcase= text.upper()
lowcase= text.lower()
print("upper case:", upcase)
print("lower case:",lowcase)

#To replaced a word in a given string
replace=  text.replace("World", str2)
print(replace)

#To split a string of words to a individual words
word=text.split() # we can set the delimiter here
print("Words:",word)

#To strip or removes the blanks in beginning and end of string
stripping=text.strip()
print("stripped text:",stripping)

#To substring in a text
sub="are"
if sub in text:
    print(sub, "found in the text")

#substring using slicing
substring= text[0:5]
print(substring)