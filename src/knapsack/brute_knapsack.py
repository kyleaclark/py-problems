__author__ = "kclark"


def generate_knapsack(items_dict, constraint_value):
    items_list = sorted(items_dict.items(), key=lambda x: x[1], reverse=True)
    items_partitions = _generate_partitions_helper(items_list)

    optimal_knapsack = None
    for items_set in items_partitions:
        current_knapsack = _compute_brute_knapsack(items_set, constraint_value)

        if current_knapsack is not None and (optimal_knapsack is None or len(current_knapsack) < len(optimal_knapsack)):
            optimal_knapsack = current_knapsack

    return optimal_knapsack


def _compute_brute_knapsack(items_list, constraint_value):
    current_collection = []

    for items_set in items_list:
        total_weight = 0
        current_set_list = []

        for cow in items_set:
            name, weight = cow
            verify_weight = total_weight + weight

            if verify_weight <= constraint_value:
                current_set_list.append(name)
                total_weight = verify_weight
            else:
                return None

        current_collection.append(current_set_list)

    return current_collection


def _generate_partitions_helper(set_):
    for partition in _compute_partitions_helper(set_):
        yield [list(elt) for elt in partition]


def _compute_partitions_helper(items_set):
    if not items_set:
        yield []
        return

    for index in range(2 ** len(items_set) // 2):
        parts = [set(), set()]

        for item in items_set:
            parts[index & 1].add(item)
            index >>= 1

        for bit in _compute_partitions_helper(parts[1]):
            yield [parts[0], *bit]
