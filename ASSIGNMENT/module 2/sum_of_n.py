def sum_of_n(n):
    if n<=0:
        return "invalid input"
    
    sum_result=0
    for i in range(1,n+1):
        sum_result+=i

    return sum_result

n=int(input("enter positive int = "))
result=sum_of_n(n)
print(f"sum of first positive int is {result}")