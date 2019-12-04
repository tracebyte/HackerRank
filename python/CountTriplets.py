# https://www.hackerrank.com/challenges/count-triplets-1
#
# You are given an array and you need to find number of triplets of indices
# such that the elements at those indices
# are in geometric progression for a given common ratio  and ... TLDR
#
# Solution:
# This was a bit challenging but after little research and understanding here
# it is
# I initially solved the problem using 3 array access - brute force but that
# will be O(N^3) times where we check each
# combination for GP which is not acceptable
#
# The key here is GP - Geometric Progression
# Quick intro: GP is a type of sequence where each item after the first is
# found by multiplying by a common ratio and
# first value
# Using hash maps - dictionary data structure in case of python its much
# impler to implement
# Let's say GP triplets are a, b, c and common ratio r
# other values are: b = a * r, c = b * r
#
# - In a given array if we pick a value say v
#
# We can calculate potential 2nd value by v * r and store it in dict2 with
# initial count as 1 - that's my default
#
# as I pick new value in array ll check if its already in dict2 if yes then
# I can calculate dict3 key (v * r) - potential 3rd triplet and I can create
# dict3 combination values with dict2 values
# - taking care of duplicated values also - hence incrementing count of dict3
# as many as dict2 value count
#
# Lastly I check if the value v that I have picked is already in dict3 then we
# ll increment the count by as many as
# dict3 count - as full 3 triplets is found
# The idea is to pre calculate potential triplets which are yet to come across
# with that in mind you can solve the
# problem in 0(N) time - which is as huge performance bump from O(N^3)
# credits - I wouldn't have understood the problem if it wasn't for existing
# discussions thread and code snippets
# Thanks all :)


from collections import Counter


def count_triplets(arr, r):
    # Create counter dict to hold the count

    dict2 = Counter()
    dict3 = Counter()

    count = 0

    for item in arr:
        # check - if item is part of the all 3 potential triplets we had
        # calculated then
        # increment the count by total potential triplets that means potential
        # triplets that we had calculated
        # are also part of given array
        # Also there could be potential triplets that we might have calculated
        # but not in array
        if item in dict3:
            count += dict3[item]

        # check - if item is part of 2nd sequence item in triplet
        # then pre calculate 3rd triplet key and increment 3rd sequence item
        # count to that of 2nd sequence item count
        # as we can create as many 3rd item as many as 2nd exists - taking
        # care of duplicates also
        if item in dict2:
            dict3[item * r] += dict2[item]

        # for every value we pick from array calculate the next potential 2nd
        # value
        # and increment the count by 1 - which in consecutive loops we use to
        # calculate next potential 3rd items
        dict2[item * r] += 1

    return count


if __name__ == "__main__":
    nr = input().rstrip().split()

    length = int(nr[0])

    ratio = int(nr[1])

    values = list(map(int, input().rstrip().split()))

    ans = count_triplets(values, ratio)

    print(ans)
