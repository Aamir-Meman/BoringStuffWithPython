colors = ["red", "orange", "blue"]

colors.append("yellow")

colors.insert(0, "green")

colors.remove("orange")

last_color = colors.pop()

print(colors)
print(last_color)

colors.clear()

print(len(colors))

"""
['green', 'red', 'blue']
yellow
0

"""