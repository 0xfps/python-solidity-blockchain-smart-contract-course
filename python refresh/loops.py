i = 0
while i < 9:
    print(i)
    
    i+=1
    
print("\n")
str = "testing for loops"
count = 0

for x in str:
   if(x == 't'):
    count += 1

print(count)

numbers1 = list(range(0, 61, 5))
numbers2 = list(range(60, -1, -5))
print(numbers1)
print(numbers2)