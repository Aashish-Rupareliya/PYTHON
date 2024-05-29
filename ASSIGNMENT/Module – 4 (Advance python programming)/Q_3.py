
new_text = "\nThis is some additional text to be appended using append mode."


with open('Q_1.txt', 'a') as file:
   
    file.write(new_text)


with open('Q_1.txt', 'r') as file:
   
    content = file.read()


print(content)
