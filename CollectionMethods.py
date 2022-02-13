from collections import *

employee = namedtuple("employee", ["name", "department", "title"] )

emp1 = employee("NN1", "ENG", "Software Engineer")
print(emp1)
print(emp1[1])
print(emp1.name)
print(emp1._asdict())

colors =(("apple", "red"),("orange", "orange"),("pear", "green"))
fruits_with_colors = defaultdict(list)

for fruit, color in colors:
    fruits_with_colors[fruit].append(color)

print(fruits_with_colors)

colours_dict = OrderedDict([("Red", 198), ("Green", 170), ("Blue", 160)])
for key, value in colours_dict.items():
    print(key, value)

favs_color = Counter(name for name, colour in colors)
print(favs_color)

d = deque()
d.append('red')
d.append('blue')
d.append('green')

print(len(d))
print(d[0])
print(d[-1])
print(d.popleft())
d.extend(["pink"])
d.extendleft(["white"])
print(d)