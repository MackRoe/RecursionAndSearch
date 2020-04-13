#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # TODO: implement linear search recursively here
    if index == len(array):
        return None
    if array[index] == item:
        return index
    else:
        result = linear_search_recursive(array, item, index + 1)
        return result

    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    starting_array = array
    array.sort()
    midpoint = len(array) // 2
    # gets midpoint
    count = len(array)
    while count > 1:
        if array[midpoint] == item:
            return index
        elif array[midpoint] < item:
            array = array[0: midpoint]
            midpoint = len(array) // 2
            print('new midpoint:', midpoint)
            count = len(array)
            print('count:', count)
        elif array[midpoint] > item:
            end_of_array = len(array)
            array = array[midpoint: end_of_array]
            midpoint = len(array) // 2
            print('new midpoint:', midpoint)
            count = len(array)
            print('count:', count)
    print('midpoint:', midpoint)
    print('item at midpoint', array[midpoint])
    if array[midpoint] == item:
        return index

    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests


def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    pass
    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests
