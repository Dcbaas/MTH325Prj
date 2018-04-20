# Finds if a graph with a given coloring is proper.
def is_proper(graph, color):
    for key, value in graph.items():
        for i in value:
            c1 = color[key]
            c2 = color[i]
            if c1 == c2:
                return False
    return True

# Helper method generate a power set of a ternary string of length n.
def ternary_combinations(length):
    ternary_set_list = []
    total_elements = pow(3, length)

    for i in range(0, total_elements):
        ternary_value = []
        decimal_val = i
        for bit in range(length - 1, -1, -1):
            bit_place = pow(3, bit)
            bit_val = decimal_val // bit_place;
            decimal_val -= bit_place * bit_val
            ternary_value.append(bit_val + 1)
        ternary_set_list.append(ternary_value)
    return ternary_set_list

# Generates all the possible colorings for a graph using three colors regardless of if it is proper
def three_color(graph):
    three_color_output = []
    vertex = list(graph.keys())
    ternary_combos = ternary_combinations(len(vertex))
    for i in ternary_combos:
        temp_set = {}
        for j in range(0, len(i)):
            key_val = vertex[j]
            val = {key_val: i[j]}
            temp_set.update(val)
        three_color_output.append(temp_set)
    return three_color_output

# Checks if a graph can be colored using three colors.
def is_three_color(graph):
    three_color_combos = three_color(graph)

    for i in three_color_combos:
        if is_proper(graph, i):
            return True
    return False

# Checks if a graph has a proper edge coloring
def is_proper_edge(graph):
    for key, value in graph.items():
        coloring = []
        for i in value:
            coloring.append(i[1])
        for i in coloring:
            if coloring.count(i) > 1:
                return False
    return True

# Generates a vertex coloring for a given graph using the greedy algorithm.
def greedy(graph, ordering):
    coloring = {}
    for i in ordering:
        color = 1
        adjacent = []
        # Get the list of adjacent colors
        for j in graph.get(i):
            other_color = coloring.get(j, "none")
            if other_color == "none":
                continue
            else:
                adjacent.append(other_color)
        done = False
        while not done:
            if adjacent.count(color) == 0:
                done = True
            else:
                color += 1

        coloring.update({i: color})
    return coloring


is_proper1 = is_proper({"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}, {"A": 1, "B": 1, "C": 3})
print(is_proper1)

color = three_color({"A": ["B"], "B": ["A"]})
print(color)

is_color1 = is_three_color({" A ": [" B ", " C "], " B ": [" A ", " C "], " C ": [" A ", " B "]})
is_color2 = is_three_color({" A ": [" B ", " C ", " D "], " B ": [" A ", " C ", " D "], " C ": [" A ", " B ", " D "],
                            " D ": [" A ", " B ", " C "]})

print(is_color1)
print(is_color2)
print("\n")

proper_edge1 = is_proper_edge(
    {" A ": [[" B ", 1], [" C ", 2]], " B ": [[" A ", 1], [" C ", 3]], " C ": [[" A ", 2], [" B ", 3]]})

proper_edge2 = is_proper_edge(
    {" A ": [[" B ", 1], [" C ", 2]], " B ": [[" A ", 1], [" C ", 2]], " C ": [[" A ", 2], [" B ", 2]]})

print(proper_edge1)
print(proper_edge2)
print("\n")

graph1 = greedy({" A ": [" B ", " C "], " B ": [" A "], " C ": [" A "]}, [" A ", " B ", " C "])
graph2 = greedy({" A ": [" B "], " B ": [" A ", " C "], " C ": [" B ", " D "], " D ": [" C "]},
                [" A ", " D ", " B ", " C "])
print(graph1)
print(graph2)
