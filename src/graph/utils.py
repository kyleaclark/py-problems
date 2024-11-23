def generate_adjacency_matrix(num_nodes: int, edges: list[tuple[int, int]]) -> list[list[int]]:
    # Initialize an empty adjacency list for each node
    result = [[] for _ in range(num_nodes)]

    # Populate adjacency matrix with directed edges
    for start_node, end_node in edges:
        # Adjust for zero-based indexing
        result[start_node - 1].append(end_node - 1)

    return result
