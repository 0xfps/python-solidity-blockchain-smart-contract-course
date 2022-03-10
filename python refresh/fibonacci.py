"""
This code requires user input and gets the fibonacci sequence for that particular number.
"""

import time

print("""
===================================
       FIBONACCI SEQUENCE
===================================
""")

inp = input("Type in the number to get the fibonacci sequence >> ")

def ret(n):
    print(f"""\n
FIBONACCI SEQUENCE FOR {n} >> \n
    """)
    print(n)    

try:
    num = int(inp)
    lists = [0, 1]
    string = ""
    
    if num == 0:
        ret(0)
    
    elif num >= 100:
        ret("Out of limits")
    
    else:
        
        for i in range(num - 2):
            f = lists[len(lists) - 2] + lists[len(lists) - 1]
            lists.append(f)
        
        for fibb in lists:
            string += str(fibb) + " "
            
        ret(string)
        

except:
    print("Please input a number.")
    
finally:
    print("""
===================================
             DONE
===================================
    """)