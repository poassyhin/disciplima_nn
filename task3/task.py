import csv
import math

def calculate_probabilities(matrix):
    probabilities = []
    num_elements = len(matrix)
    for row in matrix:
        row_probabilities = [elem / (num_elements - 1) for elem in row]
        probabilities.append(row_probabilities)
    return probabilities

def entropy_of_row(row):
    return sum([-p * math.log2(p) for p in row if p > 0])

def total_entropy(matrix):
    probability_matrix = calculate_probabilities(matrix)
    return sum(entropy_of_row(row) for row in probability_matrix)

def main():
    relation_matrix = [
        [2,0,2,0,0],
        [0,1,0,0,1],
        [2,1,0,0,1],
        [0,1,0,1,1],
        [0,1,0,1,1],

    ]
    entropy = total_entropy(relation_matrix)
    print(f"Total Entropy: {entropy}")

if __name__ == "__main__":
    main()