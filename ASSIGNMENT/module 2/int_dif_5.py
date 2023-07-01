def check_int_value(a,b):
    if a==b or a+b==5 or abs(a-b)==5:
        return True
    else:
        return False
    
num1=int(input("enter num 1 : "))
num2=int(input("enter num 2 : "))

result=check_int_value(num1,num2)
print(result)
                   