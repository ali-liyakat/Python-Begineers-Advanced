# Strings are declared using single or double quotes
# they are immutable

fname = 'Liyakat'
lname = 'Ali'

name = fname +" " + lname
print(name)

# Python formatted strings

fullname = f"{fname} {lname}"
print(fullname)
age = 25

print(f"{fname} {lname} age is {age} years.")

# strings are 0 indexed

print(name[0])
print(name[0:5])    #slicing
print(name[8:])    

print(len(name))    # Gives length

print("Liyakat's fav color is Balck")
print('''i love 
      to have 
      a good room''')


# Various Methods Related to Strings

recipe = "biryani with rice, cloves, cardamon, ginger and chicken"
print("rice" in recipe)   # to check the elemeents
print("Love" in recipe) 

print(recipe.find("chicken"))   # gives index

s = "patient was charges $100"
print(s)
s = s.replace("$100", "$10")
print(s)
print(s.upper())
print(s.index("$10"))

s1 = "My name is"
s2 = "Liyakat Ali"
s3 = s1 + " " + s2
print(s3)

tickers ="APL|NVD|CUDA|API"
print(tickers.split("|"))

data = "  hey! what are you doing?   "
print(data.strip())