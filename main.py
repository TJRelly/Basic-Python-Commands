#Comments go here
name = "Beau" #Inline comments
print(name)
print(isinstance(name, str))

age = 39
print(age)
print(type(age)==str)
print(isinstance(age, int))

#casting (int, str, float)
number = 20
print(type(number)) #int
number2 = str(20)
print(type(number2)) #str
number2 = float(20)
print(type(number2)) #float

#// rounds down
print(5/2) # = 2.5
print(5//2) # = 2

#ternary operator
def is_adult(age):
    return True if age > 18 else False

print(is_adult(18))

#multiline string
print("""Wassup
Bro

You good?""")

# .upper() 
# .lower() 
# .isalpha 
# .isalnum 
# .isdecimal 
# .islower() 
# .isupper()
# .title()
# .startswith()
# .endswith()
# .replace()
# .split()
# .strip()
# .join()
# .find()

name = "Terrell"
print(name.isalpha())

#in
#escaping with backslash "\"

print("You are \"The Man\"")

#indexing [] - starts @ 0
print(name[1]) # e

#slice :
text = "Terrell is cool"
print(text[4:])
print(text[:4])
print(text[4:7])