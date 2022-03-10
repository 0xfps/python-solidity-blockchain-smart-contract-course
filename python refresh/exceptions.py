inp = input()

try:
    x = int(inp)
    print(x)

except:
    print("An integer is needed.")
    raise

finally:
    print("This line will run.")
    
    

assert(10 > 9), "This went well"
assert False
#Error on line 17