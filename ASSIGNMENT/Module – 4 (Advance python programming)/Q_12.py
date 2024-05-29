def copy_file(src, dest):
    with open(src, 'r') as source_file:
        content = source_file.read()
    with open(dest, 'w') as dest_file:
        dest_file.write(content)

copy_file('Q_1.txt', 'example_copy.txt')
