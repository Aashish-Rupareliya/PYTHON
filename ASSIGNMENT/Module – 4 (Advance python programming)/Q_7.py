def file_to_variable(filename):
    with open(filename, 'r') as file:
        return file.read()

content = file_to_variable('Q_1.txt')
print(content)
