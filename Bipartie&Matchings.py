def contains(list, element):
    if list.count(element) > 0:
        return True
    return False


# Takes a list returns the power set.
def power(list):
    output_list = []
    pow_set_size = pow(2, len(list))
    print("here 1")
    for i in range(0, pow_set_size):
        temp = []
        for j in range(0, len(list)):
            if i & (1 << j):
                temp.append(list[j])
        output_list.append(temp)
    # output_list.sort(len(x) < len(y))
    return output_list


# This works and I don't know why????????????????!? :parrot:
def partite_sets(graph):
    partite_set__x = []
    partite_set__y = []
    for key, value in graph.items():
        # Case 0: the key is in nether. Add the key to X and the value to Y
        if not contains(partite_set__x, key) and not contains(partite_set__y, key):
            partite_set__x.append(key)
            for i in value:
                partite_set__y.append(i)

        # Case 1: the key is in X check if the values are in Y if one isn't add it in.
        elif contains(partite_set__x, key):
            for i in value:
                if not contains(partite_set__y, i):
                    partite_set__y.append(i)
        # Case 2: The key is in  check if the values are in X if one isn't add it in.
        elif contains(partite_set__y, key):
            for i in value:
                if not contains(partite_set__x, i):
                    partite_set__x.append(i)
    output_set = [partite_set__x, partite_set__y]
    return output_set


def is_bipartite(graph):
    partite_set = partite_sets(graph)
    for key in graph:
        if contains(partite_set[0], key) and contains(partite_set[1], key):
            return False
    return True


def is_perfect(graph):
    partite_set = partite_sets(graph)
    print(partite_set)
    # Do both partite sets have an equal number of vertices
    if len(partite_set[0]) != len(partite_set[1]):
        return False

    return True


graph1 = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}
graph2 = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C"]}

# boolean = is_bipartite(graph1)
# print(boolean)

perfect1 = is_perfect(graph2)
perfect2 = is_perfect(graph1)

print(perfect1)
print(perfect2)
