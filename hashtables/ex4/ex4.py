def has_negatives(a):
    """
    YOUR CODE HERE
    """
    negative_hash = {}
    result = []
    for i in range(len(a)):
        # Number is negative
        if negative_hash.get(abs(a[i])) is not None:
            if a[i] < 0 and negative_hash.get(abs(a[i])) is True:
                result.append(abs(a[i]))
            elif a[i] > 0 and negative_hash.get(abs(a[i])) is False:
                result.append(abs(a[i]))
        else:
            if a[i] < 0:
                negative_hash.update({abs(a[i]): False})
            else:
                negative_hash.update({abs(a[i]): True})

    return result


if __name__ == "__main__":
    # Output should be: [1, 2, 4]
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
