tup = ("Acts", 23, "Romans", 40, 0, 9, 7, 6)
lists = ["Acts", "Romans"]
print("Acts" in tup)
print(tup[2])
print(tup[::4])

print(", ".join(lists))
print("Hello me".replace("me", "world!"))

if all([len(i) > 2 for i in lists]):
    print("They are all greater than 2.")
    
if any([len(i) < 5 for i in lists]):
    print("One is less than 5.")


