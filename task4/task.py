import math

def calculate_sum_and_product():
    sums, products = [], []

    for x in range(1, 7):
        for y in range(1, 7):
            sums.append(x + y)
            products.append(x * y)

    unique_sums = list(set(sums))
    unique_products = list(set(products))
    
    # Creating a matrix to store frequencies
    freq_matrix = [[0 for _ in unique_products] for _ in unique_sums]

    for x in range(1, 7):
        for y in range(1, 7):
            freq_matrix[unique_sums.index(x + y)][unique_products.index(x * y)] += 1

    return freq_matrix

def normalize_matrix(matrix):
    for row in matrix:
        for i in range(len(row)):
            row[i] /= 36

    return matrix

def calculate_entropy(matrix, mode='row'):
    total_entropy = 0.0
    
    if mode == 'row':
        for row in matrix:
            row_entropy = sum(row)
            if row_entropy != 0.0:
                total_entropy += -row_entropy * math.log2(row_entropy)
    
    elif mode == 'column':
        for col in range(len(matrix[0])):
            col_entropy = sum(matrix[row][col] for row in range(len(matrix)))
            if col_entropy != 0.0:
                total_entropy += -col_entropy * math.log2(col_entropy)

    return total_entropy

def calculate_joint_entropy(matrix):
    joint_entropy = 0.0
    for row in matrix:
        for val in row:
            if val != 0.0:
                joint_entropy += -val * math.log2(val)

    return joint_entropy

def calculate_conditional_entropy(matrix, normalized_matrix):
    conditional_matrix = [[0 for _ in matrix[0]] for _ in matrix]
    
    for row in range(len(matrix)):
        row_sum = sum(matrix[row])
        for col in range(len(matrix[row])):
            conditional_matrix[row][col] = matrix[row][col] / row_sum if row_sum else 0

    conditional_entropy = 0.0
    for row in range(len(conditional_matrix)):
        for col in range(len(conditional_matrix[row])):
            val = conditional_matrix[row][col]
            if val != 0.0:
                conditional_entropy += -val * math.log2(val) * sum(normalized_matrix[row])

    return conditional_entropy

def task():
    freq_matrix = calculate_sum_and_product()

    normalized_matrix = normalize_matrix(freq_matrix)
    
    entropy_X = calculate_entropy(normalized_matrix, mode='row')
    entropy_Y = calculate_entropy(normalized_matrix, mode='column')

    joint_entropy_XY = calculate_joint_entropy(normalized_matrix)

    conditional_entropy_Y_given_X = calculate_conditional_entropy(freq_matrix, normalized_matrix)

    mutual_information_X_Y = entropy_Y - conditional_entropy_Y_given_X

    return entropy_X, entropy_Y, joint_entropy_XY, conditional_entropy_Y_given_X, mutual_information_X_Y

if __name__ == '__main__':
    print(task())