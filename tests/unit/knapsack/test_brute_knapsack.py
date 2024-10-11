import pytest

from src.knapsack.brute_knapsack import generate_knapsack


@pytest.mark.parametrize(
    "items,weight_constraint,expected",
    [
        pytest.param(
            {"Lemons": 40, "Pennies": 20, "Milky Ways": 40, "Mounds": 50, "Apples": 25, "Crackers": 25},
            100,
            [["Milky Ways", "Pennies", "Lemons"], ["Apples", "Mounds", "Crackers"]],
        ),
        pytest.param(
            {"Snickers": 50, "Barbies": 65, "Butterfingers": 72}, 75, [["Snickers"], ["Butterfingers"], ["Barbies"]]
        ),
        pytest.param(
            {"Starbursts": 54, "Barbies": 39, "Limes": 41, "Butterfingers": 11},
            145,
            [["Limes", "Starbursts", "Barbies", "Butterfingers"]],
        ),
    ],
)
def test_brute_knapsack(items, weight_constraint, expected):
    result = [sorted(group, key=str.lower) for group in generate_knapsack(items, weight_constraint)]
    expected = [sorted(group, key=str.lower) for group in expected]

    assert len(result) == len(expected)
    assert sorted(result) == sorted(expected)
