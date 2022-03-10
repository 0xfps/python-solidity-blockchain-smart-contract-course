def format_number(num):
    newnum = str(num)
    
    if(len(newnum) < 4):
        return newnum
    else:
        x = len(newnum) % 3
        l = len(newnum) - 1
        
        if(x == 0):
            start = 0 + 2
        else:
            start = x - 1
        
        precomma = newnum[:start + 1] + ","
        
        formnum = ""
        
        newlist = newnum[start + 1 : ]
        newlist_len = len(newlist) - 1
        i = 0
        j = 1
        
        while i <= newlist_len:
            if(i == newlist_len):
                formnum += newlist[i]
            else:
                if( j == 3):
                    formnum += newlist[i]+","
                    j = 1
                else:
                    formnum += newlist[i]
                    j += 1
            i += 1
        
        divided_number = precomma + formnum
    
    return divided_number

format_number(1234568789245824798)