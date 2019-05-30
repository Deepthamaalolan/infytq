def check_double(number):
    
    #Remove pass and write your logic here
    double_number=number+number
    numberlist=list(str(number))
    double_numberlist=list(str(double_number))
    len1=len(str(number))
    len2=len(str(double_number))
    flag=False
    for i in numberlist:
        if i in double_numberlist:
            flag=True
    if((sorted(str(number)))==(sorted(str(double_number)))):
        flag1=True
    else:
        flag1=False
    if((len1==len2)and(flag==True)and(flag1==True)):
        flag3=True
    else:
        flag3=False
    return flag3
        

#Provide different values for number and test your program
print(check_double(100))
