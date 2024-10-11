import pytest

from src.knapsack.greedy_knapsack import generate_knapsack


@pytest.mark.parametrize(
    "items,weight_constraint,expected",
    [
        pytest.param(
            {
                "Harry": 50,
                "Mr. Belding": 15,
                "Mickey": 75,
                "Percy": 20,
                "Peaches": 60,
                "Larry": 45,
                "Lenny": 10,
                "Carrie": 5,
                "Molly": 85,
                "Maxx": 65,
            },
            100,
            [
                ["Molly", "Mr. Belding"],
                ["Mickey", "Percy", "Carrie"],
                ["Maxx", "Lenny"],
                ["Peaches"],
                ["Harry", "Larry"],
            ],
        ),
        pytest.param(
            {
                "Donuts": 50,
                "Burgers": 65,
                "Peaches": 12,
                "Whip Cream": 35,
                "Radishes": 50,
                "Danishes": 85,
                "Butter": 72,
                "Limes": 24,
                "Chocolates": 10,
                "Apples": 38,
            },
            100,
            [
                ["Danishes", "Peaches"],
                ["Butter", "Limes"],
                ["Burgers", "Whip Cream"],
                ["Donuts", "Radishes"],
                ["Apples", "Chocolates"],
            ],
        ),
        pytest.param(
            {
                "Burgers": 39,
                "Whip Cream": 59,
                "Radishes": 42,
                "Licorices": 41,
                "Chocolates": 59,
                "Butter": 11,
                "Star Crunch": 54,
                "Apples": 28,
            },
            120,
            [
                ["Whip Cream", "Chocolates"],
                ["Star Crunch", "Radishes", "Butter"],
                ["Licorices", "Burgers", "Apples"],
            ],
        ),
    ],
)
def test_greedy_knapsack(items, weight_constraint, expected):
    result = generate_knapsack(items, weight_constraint)
    assert result == expected
