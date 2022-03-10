"""
Longest Word


Given a text as input, find and output the longest word.

Sample Input
this is an awesome text

Sample Output
awesome
"""

txt = input()

#your code goes here
x = txt.split(' ')
p = max(x, key=len)
print(p)