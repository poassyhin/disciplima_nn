import csv
from collections import defaultdict
from io import StringIO

def parse_csv_graph(csv_string):
    graph = defaultdict(list)
    reverse_graph = defaultdict(list)
    nodes = set()
    f = StringIO(csv_string)
    reader = csv.reader(f)
    for row in reader:
        src, dest = row
        graph[src].append(dest)
        reverse_graph[dest].append(src)
        nodes.update([src, dest])
    return graph, reverse_graph, nodes

def compute_relations(graph, reverse_graph, nodes):
    relations = {node: [0, 0, 0, 0, 0] for node in nodes}
    for node in nodes:

        relations[node][0] = len(graph[node])

        relations[node][1] = len(reverse_graph[node])

        for child in graph[node]:
            relations[node][2] += len(graph[child])
            for grandchild in graph[child]:
                if grandchild != node:
                    relations[node][4] += 1
        for parent in reverse_graph[node]:
            relations[node][3] += len(reverse_graph[parent])

    return relations

def task(csv_string):
    graph, reverse_graph, nodes = parse_csv_graph(csv_string)
    relations = compute_relations(graph, reverse_graph, nodes)
    
    output = StringIO()
    writer = csv.writer(output)
    for node in sorted(nodes):
        writer.writerow(relations[node])

    return output.getvalue().strip()


csv_str = "1,2\n2,3\n2,4\n3,5\n3,6"
result = task(csv_str)
print(result)