def frequency():
    str = input('Enter a string :')
    di = dict()
    con = str.lower()
    for x in con:
        if x not in di :
            di[x] = 1 
        else :
            di[x]+=1
    
    d1 =sorted(di.items(),key = lambda item:item[1] ,reverse = True)
    
    for x in d1 :
        print(f"{x[0]} = 0{x[1]}")
   
frequency()
