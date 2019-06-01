def find_max(num1, num2):
    max_num=-1
    list1=[]
    sum1=0
    # Write your logic here
    for i in range(num1,num2):
        if(i>9 and i <=99 and i%5==0):
            while(i!=0):
                num=i%10
                sum1=sum1+num
                i=i/10
            if(sum1%3==0):
                list1.append(i)
                max_num=max(list1)
                
           
        else :
            return -1
    
    return max_num    
   

#Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)
