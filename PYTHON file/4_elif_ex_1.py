a=int(input("Enter A :"))
b=int(input("Enter B :"))
c=int(input("Enter C :"))

if a>b:
    if a>c:
        print(a,"is max num")
    else:
        print(c,"is max num")

elif b>c:
    print(b,"is max num")

else:
    print(c,"is max num")

