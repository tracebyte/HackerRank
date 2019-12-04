"""
Link: https://www.hackerrank.com/challenges/sparse-arrays/problem
There is a collection of input strings and a collection of query strings.
For each query string, determine how many times it occurs in the list of input
strings.

TLDR...

Passed all test cases
"""

from collections import defaultdict


def matching_strings(strings, queries):
    result = []
    strings_dict = defaultdict(int)
    for item in strings:
        strings_dict[item] += 1

    for item in queries:
        if item in strings_dict:
            result.append(strings_dict[item])
        else:
            result.append(0)
    return result


if __name__ == '__main__':

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matching_strings(strings, queries)

    for r in res:
        print(r)
