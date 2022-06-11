print("Trick or Treat!")
row1 = ["🎃", "🎃", "🎃"]
row2 = ["🎃", "🎃", "🎃"]
row3 = ["🎃", "🎃", "🎃"]
maps = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = str(input("Where do you want to put the skull?: "))
horizontal = int(position[0])
vertical = int(position[1])
selected_row = maps[vertical - 1]
selected_row[horizontal - 1] = "💀"
print(f"{row1}\n{row2}\n{row3}")
