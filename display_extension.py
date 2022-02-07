filename = input("Input the Filename: ")
ext = filename.split(".")
if(ext[-1]=='py'):
    print ("The extension of the file is :'Python'")
elif(ext[-1]=='c'):
    print("The extension of the file is : 'C language'")
elif(ext[-1]=='cpp'):
    print("The extension of the file is : 'C ++'")
