# Fizzbuzz
n = int(input())

for x in range(1, n, 2):
    if((x % 3 == 0) and (x % 5 == 0)):
	print("SoloLearn")
    else:
	if((x % 3 == 0)):
	    print("Solo")

	else:
	    if((x % 5 == 0)):
		print("Learn")

	    else:
		print(x)