import json
import numpy as np


def load_json_data(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

def flatten_clustered_list(clustered_list):
    flattened_list = []
    index_list = []
    index = 0
    for group in clustered_list:
        if isinstance(group, int):
            group = [group]
        for item in group:
            index_list.append(index)
            flattened_list.append(item)
        index += 1
    return flattened_list, index_list

def generate_comparison_matrix(clustered_list):
    flattened, indexes = flatten_clustered_list(clustered_list)
    size = len(flattened)
    comparison_matrix = np.zeros((size, size), dtype=int)

    for i, item in enumerate(flattened):
        for j, other_item in enumerate(flattened):
            if indexes[i] <= indexes[j]:
                comparison_matrix[item - 1][other_item - 1] = 1
    return comparison_matrix

def find_disagreements(matrix1, matrix2):
    disagreement_pairs = []
    combined_matrix = np.logical_or(matrix1 * matrix2, matrix1.T * matrix2.T).astype(int)

    for i in range(len(combined_matrix)):
        for j in range(i + 1, len(combined_matrix)):
            if combined_matrix[i][j] == 0:
                pair = [i + 1, j + 1]
                disagreement_pairs.append(pair)

    return consolidate_disagreements(disagreement_pairs)

def consolidate_disagreements(pairs):
    consolidated = []
    for pair in pairs:
        found = False
        for group in consolidated:
            if set(pair).intersection(set(group)):
                group.extend(pair)
                group = list(set(group))
                found = True
                break
        if not found:
            consolidated.append(pair)
    return [sorted(list(set(group))) for group in consolidated]

def reconcile_rankings(ranking1, ranking2, disagreements):
    final_ranking = []
    for group1 in ranking1:
        if isinstance(group1, int): 
            group1 = [group1]
        for group2 in ranking2:
            if isinstance(group2, int):
                group2 = [group2]

            common_elements = set(group1).intersection(set(group2))
            for element in group1:
                in_disagreement, disagreement_group = check_in_disagreement(element, disagreements)
                if in_disagreement and disagreement_group not in final_ranking:
                    final_ranking.append(disagreement_group)
                    break
            if common_elements and not in_disagreement:
                final_ranking.append(list(common_elements) if len(common_elements) > 1 else common_elements.pop())
    return final_ranking

def check_in_disagreement(value, disagreements):
    for group in disagreements:
        if value in group:
            return True, group
    return False, []

def execute_task():
    expert_A = [1,[2,3],4,[5,6,7],8,9,10]
    expert_B = [[1,2],[3,4,5,],6,7,9,[8,10]]

    matrix_A = generate_comparison_matrix(expert_A)
    matrix_B = generate_comparison_matrix(expert_B)

    disagreement_AB = find_disagreements(matrix_A, matrix_B)


    reconciled_AB = reconcile_rankings(expert_A, expert_B, disagreement_AB)
    print(reconciled_AB)

if __name__ == '__main__':
    execute_task()
