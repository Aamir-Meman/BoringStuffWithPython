colors = ["red", "blue", "green", "yellow"]

print(colors[1])

print(colors[1:])

print(colors[:1])

print(colors[1:3])

for index, color in enumerate(colors, start=1):
    print(index, color)

"""
blue
['blue', 'green', 'yellow']
['red']
['blue', 'green']
1 red
2 blue
3 green
4 yellow

"""