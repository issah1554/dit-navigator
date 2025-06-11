import csv
from collections import defaultdict


def convert_edges_to_graph(csv_file):
    graph = defaultdict(dict)

    with open(csv_file, mode="r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            from_node = row["from"]
            to_node = row["to"]
            distance = int(row["distance"])

            # Add both directions (assuming bidirectional paths)
            graph[from_node][to_node] = distance
            graph[to_node][from_node] = distance

    # Convert defaultdict to regular dict for cleaner output
    return dict(graph)


def format_as_js(graph):
    js_lines = []
    js_lines.append("const graph = {")

    for node, connections in graph.items():
        connections_str = ", ".join(f'"{k}": {v}' for k, v in connections.items())
        js_lines.append(f'  "{node}": {{{connections_str}}},')

    js_lines.append("};")
    return "\n".join(js_lines)


# Example usage:
graph = convert_edges_to_graph("edges.csv")
js_code = format_as_js(graph)
# print(js_code)

# To save to a file:
with open("graph.js", "w") as f:
    f.write(js_code)
