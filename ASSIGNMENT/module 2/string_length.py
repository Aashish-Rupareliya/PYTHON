def string_length(string):
    length=0
    for i in string:
        length+=1
    return length

input_string=input("enter string :  ")
length=string_length(input_string)
print(f"stringh length is {length}")