import csv
import math
from io import StringIO
from math import log2

def parse_csv_matrix(csv_string):
    matrix = []
    f = StringIO(csv_string)
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        matrix.append([int(x) for x in row])
    return matrix

def calculate_entropy(matrix):
    total_values = sum(sum(row) for row in matrix)
    if total_values == 0:
        return 0.0

    res = 0.0
    for row in matrix:
        for value in row:
            if value > 0:
                res -= int(value) / (len(matrix) - 1) *  log2(int(value) / (len(matrix) - 1))
    return round(res, 1)

def task(csv_string):
    matrix = parse_csv_matrix(csv_string)
    return calculate_entropy(matrix)

# Example usage
csv_str = '''1,0,2,0,0
2,1,2,0,0
2,1,0,1,0
0,1,0,1,0
0,1,0,1,0
0,1,0,1,0'''
result = task(csv_str)
print(result)