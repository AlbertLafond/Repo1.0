print("I wasn't picking it, I was scratching it!")

add = 2 + 2
print(add)

sub = 4 - 1
print(sub)

mul = 5 * 5
print(mul)

div = 30 / 7
print(div)

lob = 30 // 7
print(lob)

mod = 30 % 7
print(mod)

print("30 divided by 7 equals: ")
print(lob)
print("with a remainder of: ")
print(mod)
      
pi = 3.1415926535897932
print(pi)

def return_lyrics():
    lyrics = "I'm a lumberjack, and im okay."
    lyrics = lyrics + "I sleep all night and I work all day."
    return lyrics
lumberjackSong = return_lyrics()

i = 0
while i < 5:
    print ("hello")
    i += 1

j = 0
i = 0
while i < 5:
    while j < 5:
        print (j, end = '\t')
        j += 1
    print ('\n$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $')
    j = 0
    i += 1
            
    
def print_lyrics():
    print("I dont care")
    print("Blah blah blah")
    return "not at all what you expected"

printThis = print_lyrics()
print("xxxxxxxxxxxxxxxxxxxxx")
print(printThis)

#print(print_lyrics())

x = 41
if x == 42: # equals
    print ("equals")
if x != 42: # not equal
    print ("not equals")
if x > 42: # greater than
    print ("greater than")
if x >= 42: # greater than or equal to
    print ("greater than or equal to")
if x < 42: # less than
    print ("less than")
if x <= 42: # less than or equal to
    print ("less than or equal to")


drinks = ['Apple juice', 'Grape juice', 'Iced tea',]

firstdrink = drinks[0]
# lists are zero indexed
# the first element is 0

firstdrink = drinks[-1]
# negative indicces are counted from the end
# the first element is negative len

# the keyword "for"
# loops through a list

for drink in drinks:
    print (drink)

twodrinks = drinks[1:3]

#dictionary
people = {'firstname': 'Cato', 'lastname': 'Bowman', 'email':'CatoBowman@Gmail.com'}      
# As directed by pep 8 do not exceed 80 characaters per line

firstname = people['firstname'] # returns the value associated with the key firstname

#https://docs.python.org/3/library/stdtypes.html#str.split
#https://docs.python.org/3/library/stdtypes.html#str.lower
#https://docs.python.org/3/library/stdtypes.html#str.find

#use when index of subString is needed

    string = "catch my catantonic cat."
    subString = cat
    stringIndex = string.find(subString)
    print(stringIndex)
# "in" will return a boolean
    if(subString):
        print("yes")
    else:
        print("no")
#convert a string to lower will allow you to make comparisions that ignore case
        crazyString = "I will be easy to cAtch my cAtAtoinc cat."
        stringIndex = crazyString.find(subString)
        print(stringIndex)
        stingIndex = crazySting.lower().find(subSting)
        print(stringIndex)
#the second print statement prits the origal crazyString
        print(crazyString.lower())
        print(crazyString)
    if crazyString > string:
        print("crazy")
    else:
        print("lower is greater tahn uspercase")
    if "z" < "a":
        print("upercase letters come first")
    stringIndex = string.find(subString, 19)
    print(stringIndex)
    someValues = "Laconia Gilford Belmont"
    listofvalues = someValues.split()
    print(listOfValues[1])
    keyValuePairs = "bill; Laconia, Jane; Gilfords Tom;Belmont"
    listOfPairs = keyValuePairs.split(", ")
    count = 0
    while count < len(listOfPairs)
        fname, town = listOfPairs[count].split(": ")
        print(first name is: " + fname = "\n town is: " + town)
        count += 1
