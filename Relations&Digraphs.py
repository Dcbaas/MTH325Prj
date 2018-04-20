def is_reflex(ground, relation):  # Takes digraph as input
    for element in ground:  # Checks each element ("A", "B", "C"...) individually
        value = False  # Assume there is no reflexsive relation for this element
        # print (element)                  #DEBUG PRINT STATEMENT
        for rel in relation:  # Checks each relationship against current element
            if rel.count(element) >= 2:  # If the current element is in the relation twice i.e. ("A", "A")
                # print (rel)                  #DEBUG PRINT STATEMENT
                value = True  # If we find a valid
        if not value:  # If value is still false (we did not find a reflexsive relation for this element)
            return False  # Automatically returns false
    return True  # If we have not found False after checking each element, the digraph must be true


def is_sym(ground, relation):  # Takes digraph as input
    for A in ground:  # For each element in digraph
        for B in ground:  # For each set of elements in digraph
            value1 = False  # Assume no relation between these elements
            value2 = False  # Assume no reverse relation between these elements
            for rel in relation:  # Check each relation against these two elements
                if rel[0] == A and rel[1] == B:  # If A relates to B
                    value1 = True  # Relation 1 is true
                if rel[1] == A and rel[0] == B:  # If B relates to A
                    value2 = True  # Relation 2 is true
            if value1 and not value2:  # If only one value relates to the other
                return False  # The digraph is not symmetric
            if value2 and not value1:  # See above
                return False  # See above
    return True  # If we have not disproven it after checking each set of elements, the digraph must be symmetric


def is_antisym(ground, relation):  # Takes digraph as input
    for A in ground:  # For each element
        for B in ground:  # For each pair of elements
            value1 = False  # Assume no relation
            value2 = False  # Assume no reverse relation
            for rel in relation:  # For each relation
                if rel[0] == A and rel[1] == B:  # If A relates to B
                    value1 = True  # We have a relation
                if rel[1] == A and rel[0] == B:  # If B relates to A
                    value2 = True  # We have a reverse relation
            if value1 and value2:  # If A and B relate to each other
                if A != B:  # If A and B are not the same
                    return False  # False, not antisymmetric
    return True  # If we have not disproved it after checking each set of elements, the digraph must be antisymmetric


def is_trans(ground, relation):  # Takes digraph as input
    for A in ground:  # For each element
        tempList = []  # Creates empty list that will be filled with required relations
        for rel in relation:  # For each relation
            if rel[0] == A:  # If A relates to another element
                B = rel[1]  # That element becomes B
                for rel2 in relation:  # Check each relation again
                    if rel2[0] == B:  # If B relates to another element
                        tempList.append(rel2[1])  # Then append it to the list of required relations for A
        for C in tempList:  # For each element of our required list
            value = False  # Assume that the required relation does not exist
            for rel3 in relation:  # For each relation
                if rel3[0] == A and rel3[1] == C:  # If A relates to C
                    value = True  # The relation does exist
            if not value:  # If the relation does not exist
                return False  # The digraph is not Transitive
    return True  # If we have not yet disproved it, the digraph must be transitive


def trans_clos(digraph):
    ground_set = list(digraph.keys())  # Get the ground set
    trans_graph = digraph  # Copy the existing graph to be the final output
    total_relation_set = []
    # Generate all of the relations
    for key, value in trans_graph.items():  # For each Vertex of the graph
        for i in value:
            total_relation_set.append([key, i])

    for base_vertex in ground_set:  # For a given vertex in the ground_set
        for distance_vertex in ground_set:  # How does it relate to the other vertecies in the ground set
            key_val = digraph.get(base_vertex)
            if key_val.count(
                    distance_vertex) > 0:  # If the distant_vertex directly releates to the base vertex continue.
                continue
            else:
                temp_relation = []
                for relations in total_relation_set:  # Get all the relatoins that contain the base_vertex or _distance vertex
                    if relations[0] == base_vertex or relations[1] == distance_vertex:
                        temp_relation.append(relations)
                if is_trans(ground_set, temp_relation):  # This is where it goes wrong.
                    trans_graph.get(base_vertex).append(distance_vertex)
        return trans_graph


# is_reflex1 = is_reflex(["A", "B", "C", "D", "E"],
#                        [["A", "A"], ["A", "D"], ["B", "C"], ["B", "D"], ["C", "E"], ["D", "A"], ["E", "E"]])
# print(is_reflex1)
#
# is_trans1 = is_trans(["A", "B", "C", "D", "E"],
#                      [["A", "A"], ["A", "D"], ["B", "C"], ["B", "D"], ["C", "E"], ["D", "A"], ["E", "E"]])
# is_trans2 = is_trans(["A", "B", "C", "D"],
#                      [["A", "A"], ["A", "B"], ["A", "C"], ["A", "D"], ["B","D"], ["C", "D"], ["C", "C"]])
#
# print(is_trans1)
# print(is_trans2)
#
# graph1 = trans_clos({"A": ["B"], "B": ["C"], "C": ["B"], "D": ["A", "C"]})
# print(graph1)
#
temp_relation = [['A', 'B'], ['B', 'C']]
temp_ground_set = ['A', 'B', 'C']

is_trans3 = is_trans(temp_ground_set, temp_relation)
print(is_trans3)
