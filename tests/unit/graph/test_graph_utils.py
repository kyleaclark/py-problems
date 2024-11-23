import pytest

from src.graph.utils import generate_adjacency_matrix


@pytest.mark.parametrize(
    "num_nodes,edges,expected",
    [
        # Case 0: Empty graph, no nodes or edges
        pytest.param(
            0, [], [],
        ),
        # Case 1: Single node with no edges
        pytest.param(
            1, [], [[]],
        ),
        # Case 2: Single node with a self-loop
        pytest.param(
            1, [(1, 1)], [[0]],
        ),
        # Case 3: 4-node graph with directed edges
        pytest.param(
            4, [(1, 2), (4, 1), (2, 3), (3, 1)], [[1], [2], [0], [0]],
        ),
        # Case 4: 5-node graph with multiple edges
        pytest.param(
            5,
            [(1, 2), (2, 3), (1, 3), (3, 4), (1, 4), (2, 5), (3, 5)],
            [[1, 2, 3], [2, 4], [3, 4], [], []],
        ),
        # Case 5: 3-node graph with no edges
        pytest.param(
            3, [], [[], [], []],
        ),
        # Case 6: 3-node graph with multiple directed edges
        pytest.param(
            3, [(1, 2), (1, 3), (2, 3)], [[1, 2], [2], []],
        ),
    ],
)
def test_generate_adjacency_matrix(num_nodes, edges, expected):
    assert generate_adjacency_matrix(num_nodes, edges) == expected
