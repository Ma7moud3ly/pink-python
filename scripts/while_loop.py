while(True):
    x = int(input("Percentage : "))
    if (x==-1):break
    if( x >= 85 ):
        print("Excellent")
        if(x>=95):print('A+')
        elif(x>=90):print('A')
        else:print('A-')
    elif( x >= 75 ):
        print("Very Good")
        if(x>=80):print('B+')
        else:print('B')
    elif( x >= 50 ):
        print("Good")
        if(x>=70):print('B-')
        elif(x>=60):print('C')
        else:print('D')
    else:
        print("Failed")
    print("==================")    
   
