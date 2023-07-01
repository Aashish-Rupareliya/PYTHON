frequency=input("enter string : ")

for char in frequency:
    if char in frequency:
        frequency[char]+=1
    else:
        frequency[char]=1

print("enter frequency : ",frequency)