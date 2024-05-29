def write_list_to_file(filename, lst):
    with open(filename, 'w') as file:
        for item in lst:
            file.write(f"{item}\n")

write_list_to_file('Q_1.txt', ['first line', 'second line', 'third line'])
