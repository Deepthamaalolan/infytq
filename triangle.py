def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"
  
    if(num3<num1+num2 and num1<num2+num3 and num2<num1+num3):
        x=success
    else:
        x=failure
    return x
       
ram
num1=3
num2=3
num3=5
x=form_triangle(num1, num2, num3)
print(x)
