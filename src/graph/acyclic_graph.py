def is_acyclic(adj_matrix: list[list[int]]) -> bool:
    # Check for an empty graph
    if not adj_matrix:
        return True

    # Check for a single node with no edges
    if len(adj_matrix) == 1:
        if len(adj_matrix[0]) == 0:  # No edges
            return True
        elif adj_matrix[0][0] == 0:  # Self-loop detected
            return False

    # Continue with the acyclicity check
    for node_index in range(len(adj_matrix)):
        outgoing_edges = adj_matrix[node_index]
        if isinstance(outgoing_edges, list) and len(outgoing_edges):
            for target_node in outgoing_edges:
                visited_nodes = []
                nodes_to_explore = []
                current_node = target_node
                while True:
                    if current_node not in visited_nodes:
                        visited_nodes.append(current_node)
                        nodes_to_explore.extend(list(adj_matrix[current_node]))

                    if len(nodes_to_explore):
                        prev_node = current_node
                        current_node = nodes_to_explore.pop(0)
                        if current_node == prev_node or current_node == target_node:
                            return False
                    else:
                        break

    return True
