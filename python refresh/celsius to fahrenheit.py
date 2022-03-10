celsius = int(input())

def conv(c):
    #your code goes here
    val = ((9 * c)/5) + 32
    return val

fahrenheit = conv(celsius)
print(fahrenheit)