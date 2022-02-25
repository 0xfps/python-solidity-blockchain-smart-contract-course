# Working with files

x = '''
"r" means open in read mode.
"w" means write mode, for rewriting the contents of a file.
"a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).

r doesnt create new files but w and a does

you can add + at the end of the modes to give them extra abilities
'''

with open("filename.txt") as file:
    #print(file.read())
    m = file.write(x)
    print(m)
    file.close()
    
    #the file is closed automatically at the end of the with statement, even if an error occurs within the file.
