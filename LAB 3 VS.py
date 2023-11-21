def matrix_averages(matrix):
    n = len(matrix)
    averages = []

    for j in range(n):
        # Hər sütunda müsbət elementlərin tapılması
        positives = [matrix[i][j] for i in range(n) if matrix[i][j] > 0]

        # Sütundakı müsbət elementlərin ortalamasının hesablanması
        if len(positives) > 0:
            average = sum(positives) / len(positives)
            averages.append(average)
        else:
            averages.append(0)

    # Əsas diaqonalın yenilənməsi
    for i in range(n):
        matrix[i][i] = averages[i]

    return matrix

# İstifadə nümunəsi
matrix = [
    [1, -2, 3],
    [4, 5, -6],
    [-7, 8, 9]
]

result_matrix = matrix_averages(matrix)

# Nəticənin çap edilməsi
for row in result_matrix:
    print(row)
