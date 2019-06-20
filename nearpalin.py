 def nearest_palindrome(number):
    #start writitng your code here
    flag=1
    while(flag==1):
        number+=1 
        number1=str(number)
        number2=numbe1[::-1]
        if(number1==number2):
            flag=0
    return number
number=12300
print(nearest_palindrome(number))
