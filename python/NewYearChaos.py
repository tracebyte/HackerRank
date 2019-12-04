# https://www.hackerrank.com/challenges/new-year-chaos
# It's New Year's Day and everyone's in line for the Wonderland roller coaster
# ride!
# There are a number of people queued up, and each person wears a sticker
# indicating their initial position
# in the queue. Initial positions increment by 1 from 1 at the front of the
# line to  at the back.
#
# Any person in the queue can bribe the person directly in front of them to
# swap positions.
# If two people swap positions, they still wear the same sticker denoting
# their original places in line.
# One person can bribe at most two others. For example, if n = 8 and  Person 5
# bribes Person 4,
# the queue will look like this: 1, 2, 3, 5, 4, 6, 7, 8
#
# Fascinated by this chaotic queue, you decide you must know the minimum
# number of bribes
# that took place to get the queue...
#
# TLDR;

# Solution
# We basically reverse the given que to its original and count the steps of
# each swap reversal we also check if the
# if there are swaps with more than 2 steps then its chaotic
# Careful observation you ll notice while loop is nothing but a insertion
# sort ;) - inserting items in there rightful
# place hence the name 'insertion'
#


def minimum_bribes(q, n):
    swap = 0

    for i, v in enumerate(q):
        step = (v - 1) - i
        if step > 2:
            return "Too chaotic"

    for i in range(1, n):
        key = q[i]

        j = i - 1

        while j >= 0 and key < q[j]:
            q[j + 1] = q[j]
            j -= 1
            swap += 1
        q[j + 1] = key

    return swap


if __name__ == "__main__":
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        ans = minimum_bribes(q, n)
        print(ans)
