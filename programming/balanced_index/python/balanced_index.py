def get_balanced_index(num_list):
    ind = -1
    for i, v in enumerate(num_list):
        if sum(num_list[:(i+1)]) == sum(num_list[(i+1):]):
            ind = i

    return ind
