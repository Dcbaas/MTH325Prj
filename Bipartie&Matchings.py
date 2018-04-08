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
    return output_list
