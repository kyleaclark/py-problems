import pytest

from src.graph.acyclic_graph import is_acyclic
from src.graph.utils import generate_adjacency_matrix


@pytest.mark.parametrize(
    "num_nodes,edges,expected",
    [
        # Case 0: Empty graph, no nodes or edges
        pytest.param(
            0,
            [],
            True,
        ),
        # Case 1: Single node with no edges, trivially acyclic
        pytest.param(
            1,
            [],
            True,
        ),
        # Case 2: Single node with a self-loop, cyclic
        pytest.param(
            1,
            [(1, 1)],
            False,
        ),
        # Case 3: 4-node cyclic graph with a cycle 1 -> 2 -> 3 -> 1
        pytest.param(
            4,
            [(1, 2), (4, 1), (2, 3), (3, 1)],
            False,
        ),
        # Case 4: 4-node cyclic graph
        pytest.param(
            4,
            [(1, 3), (4, 1), (2, 3), (3, 2)],
            False,
        ),
        # Case 5: 4-node cyclic graph: 1 -> 2 -> 3 -> 4 -> 1
        pytest.param(
            4,
            [(1, 2), (4, 1), (2, 3), (3, 4)],
            False,
        ),
        # Case 6: 4-node acyclic graph
        pytest.param(
            4,
            [(1, 2), (1, 3), (2, 3), (4, 2)],
            True,
        ),
        # Case 5: 5-node cyclic graph with a cycle 1 → 2 → 3 → 1
        pytest.param(
            5,
            [(1, 2), (2, 3), (1, 3), (3, 4), (1, 4), (2, 5), (3, 5)],
            True,
        ),
        # Case 6: 5-node cyclic graph with a cycle 1 → 2 → 3 → 1
        pytest.param(
            5,
            [(1, 2), (2, 3), (3, 1), (3, 4), (1, 4), (2, 5), (3, 5)],
            False,
        ),
        # Case 7: 6-node acyclic graph with linear directed edges
        pytest.param(
            6,
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)],
            True,
        ),
        # Case 8: 6-node cyclic graph with a cycle 4 → 5 → 6 → 4
        pytest.param(
            6,
            [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 4)],
            False,
        ),
    ],
)
def test_acyclic_graph(num_nodes, edges, expected):
    adj_matrix = generate_adjacency_matrix(num_nodes, edges)
    assert is_acyclic(adj_matrix) == expected
