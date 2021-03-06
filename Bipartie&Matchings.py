# Helper function that checks if a list contains a given element
# Return: True if element is there false otherwise.
def contains(list, element):
    if list.count(element) > 0:
        return True
    return False


# Takes a list returns the power set.
def power(list):
    output_list = []
    pow_set_size = pow(2, len(list))
    for i in range(0, pow_set_size):
        temp = []
        for j in range(0, len(list)):
            if i & (1 << j):
                temp.append(list[j])
        output_list.append(temp)
    # output_list.sort(len(x) < len(y))
    return output_list


# Takes a bipartite graph and separates the vertices into sets X and Y
# If given a graph that isn't Bipartite a value will be in both partite sets.
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


# Takes a graph as an input and checks if it is bipartite or not.
# True if the graph is bipartite false otherwise.
def is_bipartite(graph):
    partite_set = partite_sets(graph)
    for key in graph:
        if contains(partite_set[0], key) and contains(partite_set[1], key):
            return False
    return True

# Helper method that looks at the neighbor of a partite set
# Returns true if the neighborhood is greater than the subset of the partite set.
# False otherwise.
def greater_neighbor(partite_set, graph):
    partite_power_set = power(partite_set)

    for i in partite_power_set:
        neighborhood = []
        for j in i:
            for k in graph.get(j):
                for l in k:
                    if not contains(neighborhood, l):
                        neighborhood.append(k)
        if len(neighborhood) >= len(i):
            return True
    return False

# Checks if a graph has a perfect matching.
# True if the graph has a perfect matching. False otherwise.
def is_perfect(graph):
    partite_set = partite_sets(graph)
    # Do both partite sets have an equal number of vertices
    if len(partite_set[0]) == len(partite_set[1]):
        if greater_neighbor(partite_set[0], graph) and greater_neighbor(partite_set[1], graph):
            return True

    return False


# Examples Provided by the professor.

list1 = ["A", "B"]
list2 = ["A", "B", "C"]

graph1 = {"A" : ["B", "C"], "B": ["A"], "C": ["A"]}
graph2 = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C"]}
graph3 = {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}

print(power(list1))
print(power(list2))

print(partite_sets(graph1))
print(partite_sets(graph2))

print(is_bipartite(graph1))
print(is_bipartite(graph3))

print(is_perfect(graph2))
print(is_perfect(graph1))