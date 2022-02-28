def frequency():
    str = input('Enter a string :')
    di = dict()
    con = str.lower()
    for x in con:
        if x not in di :
            di[x] = 1 
        else :
            di[x]+=1
    d1 =sorted(di.values(), reverse = True)
    i=0
    for x in di :
        print(x ,'=',d1[i])
        i+=1
    
frequency()
