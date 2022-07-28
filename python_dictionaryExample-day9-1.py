programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again.",
  "Loop": "The action of doing something over and over again.",
}
print(programming_dictionary["Bug"])
#retrieving items from a dictionary
print(programming_dictionary["Bug"])

#adding new items to a dictionary
programming_dictionary[123] = "Test dictionary"
programming_dictionary["Fix"] = "Defined entry for a fixed item"
print(programming_dictionary)

#to add an empty dictionary
empty_dictionary {}

# validate add of empty dictionary
print(empty_dictionary)

#wiping or erasing all entries in a dictionary
programming_dictionary {}

#edit a dictionary
programming_dictionary["Fix"] = "New definition of a fix"

#Loop through a dictionary
for thing in programming_dictionary:
  print(thing) # prints the key information Bug, Loop, Fix ...
#best way
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])

