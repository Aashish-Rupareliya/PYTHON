def sum_of_three_int(a,b,c):
    if a==b or b==c or c==a:
        return 0
    else:
        return a+b+c
    
num1=int(input("enter num 1: "))
num2=int(input("enter num 2: "))
num3=int(input("enter num 3: "))

result= sum_of_three_int(num1,num2,num3)
print(f"the sum is : {result}")
