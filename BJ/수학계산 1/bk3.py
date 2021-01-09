a = int(input())
mo = 1
br = 1
i = 1
while i < a:
    for j in range ((mo+br)-1): 
        if a <= i:
            break 
        else:
            if  mo==1 and br ==1:
                i+=1
                mo +=1
            elif (mo+br) % 2 == 1:
                if mo != 1:
                    mo -= 1
                    br += 1
                    i+=1
                else:
                    br +=1
                    i+=1
            else:
                if br != 1:
                    mo += 1
                    br -=1
                    i+=1
                else :
                    mo+=1
                    i+=1
print (f'{br}/{mo}')