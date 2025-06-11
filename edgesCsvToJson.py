import csv
from collections import defaultdict
import json


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


def save_as_json(graph, output_file):
    with open(output_file, "w") as f:
        json.dump(graph, f, indent=2)


if __name__ == "__main__":
    # Convert CSV to graph structure
    graph = convert_edges_to_graph("edges.csv")

    # Save as JSON file
    save_as_json(graph, "graph.json")

    print("Successfully generated graph.json")
