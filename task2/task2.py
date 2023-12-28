import csv
import sys

def load_graph_from_file(file_path):
    node_connections = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            node = row[0]
            connected_nodes = row[1:]
            node_connections.setdefault(node, []).extend(connected_nodes)

    return node_connections

def create_adjacency_matrix(graph):
    nodes = sorted(set(graph.keys()).union(*graph.values()))
    matrix_size = len(nodes)
    adjacency_matrix = [[0] * matrix_size for _ in range(matrix_size)]

    for node, neighbors in graph.items():
        node_index = nodes.index(node)
        for neighbor in neighbors:
            neighbor_index = nodes.index(neighbor)
            adjacency_matrix[node_index][neighbor_index] = 1
            adjacency_matrix[neighbor_index][node_index] = -1

    return adjacency_matrix, nodes

def analyze_graph(matrix, nodes):
    analysis_matrix = [[0 for _ in range(5)] for _ in nodes]

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value == 1:
                analysis_matrix[i][0] += 1
                analysis_matrix[i][2] += sum(1 for v in matrix[j] if v == 1)
            elif value == -1:
                analysis_matrix[i][1] += 1
                analysis_matrix[i][3] += sum(1 for v in matrix[j] if v == -1)
                analysis_matrix[i][4] += sum(1 for k, v in enumerate(matrix[j]) if v == 1 and k != i)

    return analysis_matrix

def save_to_csv(data, output_filename):
    with open(output_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def main(file_path):
    graph = load_graph_from_file(file_path)
    matrix, nodes = create_adjacency_matrix(graph)
    result_matrix = analyze_graph(matrix, nodes)
    save_to_csv(result_matrix, 'result_matrix.csv')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <filepath>")
        sys.exit(1)

    input_file_path = sys.argv[1]
    main(input_file_path)
