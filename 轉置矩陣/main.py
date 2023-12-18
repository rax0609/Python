matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

transpose_matrix = [list(row) for row in zip(*matrix)]

print(transpose_matrix)