lists = ['a', 'b', 'c', [1, 2, 3]]
empty_list = []
print(lists[0])
print(lists[3][0])

string = "Strings can also act as lists"
print(string[6])

lists[3][0] = 7
print(lists)

print(4 in lists)
print(5 not in lists)