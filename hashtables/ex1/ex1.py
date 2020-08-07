# Time complexity: O(n)
def get_indices_of_item_weights(weights, length, limit):
    weight_hash = {}

    for i in range(length):
        weight_hash.update({weights[i]: i})

    for i in range(length):
        match = limit - weights[i]
        if match in weight_hash:
            return (weight_hash[match], i)

    return None

weights_3 = [4, 6, 10, 15, 16]
print(get_indices_of_item_weights(weights_3, 5, 21))

weights_4 = [12, 6, 7, 14, 19, 3, 0, 25, 40]
print(get_indices_of_item_weights(weights_4, 9, 7))