from src.knapsack.brute_knapsack import generate_knapsack


def test_one():
    items_dict = {"Lemons": 40, "Pennies": 20, "Milky Ways": 40, "Mounds": 50, "Apples": 25, "Crackers": 25}
    weight_constraint = 100

    knapsack = [sorted(group, key=str.lower) for group in generate_knapsack(items_dict, weight_constraint)]

    expected_knapsack = [["Milky Ways", "Pennies", "Lemons"], ["Apples", "Mounds", "Crackers"]]
    expected_knapsack = [sorted(group, key=str.lower) for group in expected_knapsack]

    assert len(knapsack) == len(expected_knapsack) and sorted(knapsack) == sorted(expected_knapsack)


def test_two():
    items_dict = {"Snickers": 50, "Barbies": 65, "Butterfingers": 72}
    weight_constraint = 75

    knapsack = generate_knapsack(items_dict, weight_constraint)

    expected_knapsack = [["Snickers"], ["Butterfingers"], ["Barbies"]]
    expected_knapsack = [sorted(group, key=str.lower) for group in expected_knapsack]

    assert len(knapsack) == len(expected_knapsack) and sorted(knapsack) == sorted(expected_knapsack)


def test_three():
    items_dict = {"Starbursts": 54, "Barbies": 39, "Limes": 41, "Butterfingers": 11}
    weight_constraint = 145

    knapsack = [sorted(group, key=str.lower) for group in generate_knapsack(items_dict, weight_constraint)]

    expected_knapsack = [["Limes", "Starbursts", "Barbies", "Butterfingers"]]
    expected_knapsack = [sorted(group, key=str.lower) for group in expected_knapsack]

    assert len(knapsack) == len(expected_knapsack) and sorted(knapsack) == sorted(expected_knapsack)
