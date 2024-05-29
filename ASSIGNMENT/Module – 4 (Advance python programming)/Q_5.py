def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines[-n:]


print(read_last_n_lines('Q_1.txt', 3))
