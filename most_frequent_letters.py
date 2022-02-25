def frequency():
    str = input('Enter a string :')
    di = dict()
    con = str.lower()
    for x in con:
        if x not in di :
            di[x] = 1 
        else :
            di[x]+=1
    for x in di:
        print(x,'=',di[x])

frequency()
