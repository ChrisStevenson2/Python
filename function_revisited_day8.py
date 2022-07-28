# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
def greet():
  print("line 1\nline 2\nline 3")
  print("First Group of text lines")
greet()

def greet1():
  print("Hello")
  print("How are you today?")
  print("How is the weather today? Nice I hope...")
  print("***************************")
  

greet1()

def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How are you today {name}?")

greet_with_name("Lorenda")

def greet_me(name, location):
  print(f"Hello {name}")
  print(f"How are you today {name}?")
  print(f"You are at: {location}")

greet_me("Chris","Monroe")

def greet_with(name, location):
  print(f"Hello {name}")
  print(f"I see you are in {location}")

greet_with(name="Fred",location="Rockville")
greet_with(location="Seattle",name="Pike")