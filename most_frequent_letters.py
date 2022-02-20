def frequency():
    str = input('Enter a string :')
    di = dict()
    for x in str:
        if x not in di :
            di[x] = 1 
        else :
            di[x]+=1
    print(di)

frequency()