def get_matrix(n, m, value):
    matrix = []
    for str_ in range(n):
        matrix.append(list())
        for stl_ in list(range(m)):
            matrix.append(value)
    return matrix


matrix = get_matrix(2, 4, 15)
print(matrix)
matrix = get_matrix(3, 5, 4)
print(matrix)
matrix = get_matrix(5, 1, 77)
print(matrix)
