# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? Enter a two-digit number e.g. 23")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "💰" # where money bag is the location in the grid based on selection

# another way to represent the data correctly is:
#
# selected_row = map[vertical -1]
# selected_row[horizontal -1] = " X"
#
# end of another way to represent the data

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")