# https://www.hackerrank.com/challenges/minimum-swaps-2
# You are given an unordered array consisting of consecutive integers
# [1, 2, 3, ..., n]
# without any duplicates. You are allowed to swap any two elements.
# You need to find the minimum number of swaps required to sort the array in
# ascending order.
#
# For example, given the array  we perform the following steps:
# i   arr                     swap (indices)
# 0   [7, 1, 3, 2, 4, 5, 6]   swap (0,3)
# 1   [2, 1, 3, 7, 4, 5, 6]   swap (0,1)
# 2   [1, 2, 3, 7, 4, 5, 6]   swap (3,4)
# 3   [1, 2, 3, 4, 7, 5, 6]   swap (4,5)
# 4   [1, 2, 3, 4, 5, 7, 6]   swap (5,6)
# 5   [1, 2, 3, 4, 5, 6, 7]

# TLDR;
#
# Solution: minimum_swaps()
# Passed all test cases ;)
#
# The implementation minimum_swaps() is faster as we swap value to its
# rightful position and
# also in the internal `while` loop if we come across values not in its
# rightful position we swap them too,
# we keep doing this till our initial value is in
# its rightful position this works because we already know the sorted array
# ("Consecutive" integers is the keyword) - this makes sure we don't enter
# internal loop always
# The caveat here was with one of the problem statement where value was not
# consecutive hence the initial if
# condition check

# The slower func minimum_swaps_slower() swaps one value each loop which leads
# to larger array access hence slower


def minimum_swaps_slower(arr, n):
    swaps = 0

    for i in range(n):
        if arr[i] > n:
            return swaps
        j = i
        while i + 1 != arr[j]:
            j += 1
        if j != i:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
            swaps += 1
    return swaps


def minimum_swaps(arr, n):
    swaps = 0
    for i in range(n):
        if arr[i] > n:
            return swaps
        while arr[i] != i + 1:
            t = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = t
            swaps += 1
    return swaps


if __name__ == "__main__":
    total_inputs = int(input())

    input_arr = list(map(int, input().rstrip().split()))

    res = minimum_swaps(input_arr, total_inputs)

    print(res)
