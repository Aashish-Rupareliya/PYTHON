def file_to_list(filename):
    with open(filename, 'r') as file:
        return file.readlines()

print(file_to_list('Q_1.txt'))
