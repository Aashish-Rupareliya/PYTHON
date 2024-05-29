def read_first_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = [file.readline() for _ in range(n)]
    return lines


print(read_first_n_lines('Q_1.txt', 3))
