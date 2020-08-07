# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    query_hash = {}
    result = []
    for i in range(len(queries)):
        query_hash.update({queries[i]: True})

    for i in range(len(files)):
        split_path = files[i].split("/")
        for j in range(len(split_path)):
            if split_path[j] in query_hash:
                result.append(files[i])

    return result

# ['/bin/foo', '/usr/bin/baz']
if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
