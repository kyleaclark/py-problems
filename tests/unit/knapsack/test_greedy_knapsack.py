from src.knapsack.greedy_knapsack import generate_knapsack


def test_one():
    items_dict = {
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
    }
    weight_constraint = 100

    knapsack = generate_knapsack(items_dict, weight_constraint)

    expected_knapsack = [
        ["Molly", "Mr. Belding"],
        ["Mickey", "Percy", "Carrie"],
        ["Maxx", "Lenny"],
        ["Peaches"],
        ["Harry", "Larry"],
    ]

    assert knapsack == expected_knapsack


def test_two():
    items_dict = {
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
    }
    weight_constraint = 100

    knapsack = generate_knapsack(items_dict, weight_constraint)

    expected_knapsack = [
        ["Danishes", "Peaches"],
        ["Butter", "Limes"],
        ["Burgers", "Whip Cream"],
        ["Donuts", "Radishes"],
        ["Apples", "Chocolates"],
    ]

    assert knapsack == expected_knapsack


def test_three():
    items_dict = {
        "Burgers": 39,
        "Whip Cream": 59,
        "Radishes": 42,
        "Licorices": 41,
        "Chocolates": 59,
        "Butter": 11,
        "Star Crunch": 54,
        "Apples": 28,
    }
    weight_constraint = 120

    knapsack = generate_knapsack(items_dict, weight_constraint)

    expected_knapsack = [
        ["Whip Cream", "Chocolates"],
        ["Star Crunch", "Radishes", "Butter"],
        ["Licorices", "Burgers", "Apples"],
    ]

    assert knapsack == expected_knapsack
