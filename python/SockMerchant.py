#
# https://www.hackerrank.com/challenges/sock-merchant
#
# John works at a clothing store. He has a large pile of socks that he must
# pair by color for sale.
# Given an array of integers representing the color of each sock,
# determine how many pairs of socks with matching colors there are.
# For example, there are  socks with colors .
# There is one pair of color  and one of color .
# There are three odd socks left, one of each color.
# The number of pairs is .
#
#

if __name__ == "__main__":
    items = int(input())
    socks = set()
    counter = 0
    values = [int(k) for k in input().split()]
    for value in values:
        if value in socks:
            counter += 1
            socks.remove(value)
        else:
            socks.add(value)
    print(counter)
