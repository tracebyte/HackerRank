# https://www.hackerrank.com/challenges/crush/problem
# Starting with a 1-indexed array of zeros and a list of operations, for each
# operation add a value to each of the array
# element between two given indices, inclusive. Once all operations have been
# performed,
# return the maximum value in your array.
#
# For example, the length of your array of zeros n = 10
# Your list of queries is as follows:
# a b k
# 1 5 3
# 4 8 7
# 6 9 1

# actual-> 0 1 2  3  4 5 6 7 8  9
#
# index->  1 2 3  4  5 6 7 8 9  10
#         [0,0,0, 0, 0,0,0,0,0, 0]
#         [3,3,3, 3, 3,0,0,0,0, 0]
#         [3,3,3,10,10,7,7,7,0, 0]
#         [3,3,3,10,10,8,8,8,1, 0]
#
# The largest value is  10 after all operations are performed.
# TLDR;
#
# Solution: This one is tricky - the brute force method brute_force() - is
# pretty simple but is slow almost quadratic
# time as we enter the internal loop range to increment the values in the
# given range leading worst case time ~ MN
# If M - operations; N - array access;
#
# Faster:
# To make this faster we make use of input loop (M) and start calculating the
# sum on the 1st array access and
# negate the one past the last element in given range - the trick is to use
# the last+1 negate element to balance the
# consecutive sums - which we run as separate loop (N+1) - the negate value in
# loop resets the array between the ranges
#


def brute_force(items, queries):
    arr = [0] * (items + 1)
    maxed = -1
    N = 0
    M = 0
    for q in queries:
        M += 1
        s = q[0] - 1
        e = q[1]
        incr = q[2]

        for j in range(s, e):
            N += 1
            arr[j] += incr
            if arr[j] > maxed:
                maxed = arr[j]

    return maxed


if __name__ == "__main__":

    # Faster Implementation

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    zeroes = [0] * (n + 1)

    for _ in range(m):
        start, end, adder = [int(n) for n in input().split(" ")]
        zeroes[start - 1] += adder
        if end <= n + 1:
            zeroes[end] -= adder

    maxy = x = 0
    for i in zeroes:
        x = x + i
        if maxy < x:
            maxy = x
    print(maxy)
