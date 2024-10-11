def generate_knapsack(items_dict, constraint_value):
    items = sorted(items_dict.items(), key=lambda x: x[1], reverse=True)

    return _compute_greedy_knapsack(items, constraint_value, [])


def _compute_greedy_knapsack(items, constraint_value, knapsack_collection):
    bag_of_items = []
    knaspack_weight = 0

    idx = 0
    while idx < len(items):
        if knaspack_weight > constraint_value:
            break

        item = items[idx]
        name, weight = item
        verification_weight = knaspack_weight + weight

        if verification_weight <= constraint_value:
            bag_of_items.append(name)
            items.pop(idx)
            knaspack_weight = verification_weight
        else:
            idx += 1

    knapsack_collection.append(bag_of_items)

    if len(items) > 0:
        return _compute_greedy_knapsack(items, constraint_value, knapsack_collection)

    return knapsack_collection
