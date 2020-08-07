def intersection(arrays):
    """
    YOUR CODE HERE
    """
    num_hash = {}
    result = []
    for i in range(len(arrays)):
        for j in range(len(arrays[i])):
            if num_hash.get(arrays[i][j]):
                num_hash.update({arrays[i][j]: num_hash.get(arrays[i][j]) + 1})
                if num_hash.get(arrays[i][j]) == len(arrays):
                    result.append(arrays[i][j])
            else:
                num_hash.update({arrays[i][j]: 1})
            

    # print(num_hash)
    return sorted(result)


if __name__ == "__main__":
    # arrays = []

    # arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    # arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    # arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    # print(intersection(arrays))

    arrays = [
    [1, 2, 3, 4, 5],
    [12, 7, 2, 9, 1],
    [99, 2, 7, 1,]
    ]

    print(intersection(arrays))
