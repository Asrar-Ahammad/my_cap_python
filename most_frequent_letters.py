def most_frequent():
    str = input('Please enter a string :')
    di = dict()
    for x in str:
        if x not in di :
            di[x] = 1 
        else :
            di[x]+=1
    for x in di:
        print(x,'=',di[x])

most_frequent()
