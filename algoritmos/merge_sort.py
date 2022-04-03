from math import inf


def merge_sort(array):
    if len(array) == 1:
        return array, 1

    m = int(len(array)/2)
    array_left, cont_l = merge_sort(array[:m])
    array_right, cont_r = merge_sort(array[m:])

    cont = cont_l + cont_r
    a = 0
    b = 0
    array_res = []
    array_left.append(inf)
    array_right.append(inf)
    for i in range(len(array_left) + len(array_right) - 2):
        cont += 1
        if array_left[a] <= array_right[b]:
            array_res.append(array_left[a])
            a += 1
        else:
            array_res.append(array_right[b])
            b += 1
    return array_res, cont
