# https://www.hackerrank.com/challenges/frequency-queries/problem
# You are given q queries. Each query is of the form two integers described
# below:
# 1, x: Insert x in your data structure.
# 2, y: Delete one occurrence of y from your data structure, if present.
# 3, z: Check if any integer is present whose frequency is exactly . If yes,
# print 1 else 0.
# .
# .
# .
# TLDR

# To solve this we make use of two hashmaps (dict) in python:
# 1. items: frequency
# 2. frequencies: items

# Trick is to sync both the dictionaries
# Time Complexity is O(N)
# Thanks for all the comments and discussions thread :)


from collections import defaultdict


def frequency_queries(queries):
    items_to_frequency = dict()
    frequencies_to_items = defaultdict(set)

    for operation, value in queries:
        freq = items_to_frequency.get(value, 0)
        if operation == 1:
            items_to_frequency[value] = freq + 1
            frequencies_to_items[freq].discard(value)
            frequencies_to_items[freq + 1].add(value)
        if operation == 2:
            items_to_frequency[value] = max(0, freq - 1)
            frequencies_to_items[freq].discard(value)
            frequencies_to_items[freq - 1].add(value)
        if operation == 3:
            print(1 if frequencies_to_items[value] else 0)


if __name__ == "__main__":
    n = int(input())

    items = ((1, 5), (1, 6), (3, 2), (1, 10), (1, 10), (1, 6), (2, 5), (3, 2))

    frequency_queries(items)
