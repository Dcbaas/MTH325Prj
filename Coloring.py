def is_proper(graph, color):
    for key, value in graph.items():
        for i in value:
            c1 = color[key]
            c2 = color[i]
            if c1 == c2:
                return False
    return True


bool1 = is_proper({"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]}, {"A": 1, "B": 1, "C": 3})
print(bool1)


def ternary_combinations(length):
    ternary_set_list = []
    total_elements = pow(3, length)

    for i in range(0, total_elements):
        ternary_value = []
        decimal_val = i
        for bit in range(length-1,-1,-1):
            bit_place = pow(3, bit)
            bit_val = decimal_val // bit_place;
            decimal_val -= bit_place * bit_val
            ternary_value.append(bit_val + 1)
        ternary_set_list.append(ternary_value)
    return ternary_set_list

def three_color(graph):
    three_color_output = []
    vertex = list(graph.keys())
    ternary_combos = ternary_combinations(len(vertex))
    for i in ternary_combos:
        temp_set ={}
        for j in range(0,len(i)):
            key_val = vertex[j]
            val = {key_val: i[j]}
            temp_set.update(val)
        three_color_output.append(temp_set)
    return three_color_output



    # return threeColor

color =three_color({"A":["B"], "B":["A"]})
print(color)
