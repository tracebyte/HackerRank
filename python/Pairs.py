# https://www.hackerrank.com/challenges/pairs/problem
# You will be given an array of integers and a target value. Determine the
# number of pairs of array elements that have a
# difference equal to a target value... TLDR

# k: an integer, the target difference
# arr: an array of integers

# Note: This problem is similar to 2Sum problem

# Analysis:
# Time Complexity for pairs(): O(N)

# Time Complexity for brute_force(): O(N^2)


def brute_force(values, differences):
    """
    Brute force method with time complexity of O(N^2) - for every item we
    create pairs and check for
    difference. For every outer loop we do inner loop hence Quadratic times

    Space Complexity: O(N) - as we are iterating over same array
    :param values: array of items
    :param differences: k difference
    :return: count of pairs
    """
    counter = 0
    for i in values:
        for j in values:
            if i - j == differences:
                counter += 1

    return counter


def pairs(values, difference):
    """
    Smarter method is to make use of hashmaps - in our case we are using set()
    - you can also use
    dictionary; hashmaps contains unique items with no duplicates with look up
    times of constant O(1)

    Inserting items to hashmap DS like set takes O(N) space complexity.
    We insert all the items in set and iterate over the set -
    we dont need to iterate over the initial array for this problem

    Time Complexity: O(N)

    :param values: array of items
    :param difference: k difference
    :return: count of pairs
    """
    counter = 0
    unique_items = set(values)

    for i in unique_items:

        #
        # If I pick a value from array (unique_items) - I can add the
        # difference(k) to predict the
        # the required next value i.e a + k = b; then b - a = k which is what
        # is required by the problem
        #

        if i + difference in unique_items:
            counter += 1
    return counter


if __name__ == "__main__":
    n, k = (int(i) for i in input().split())

    arr = list(map(int, input().rstrip().split()))

    result = pairs(arr, k)

    # n, k = 5, 2
    # arr = [1, 5, 3, 4, 2]
    # result = pairs(arr, k)
    print(result)
