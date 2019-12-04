#
# https://www.hackerrank.com/challenges/jumping-on-the-clouds/
#
# Emma is playing a new mobile game that starts with consecutively numbered
# clouds.
# Some of the clouds are thunderheads and others are cumulus.
# She can jump on any cumulus cloud having a number that is equal to the
# number of the current cloud plus  or
# She must avoid the thunderheads.
# Determine the minimum number of jumps it will take Emma to jump from her
# starting postion to the last cloud.
# It is always possible to win the game.
#


def jump(l):
    arr = [idx for idx, item in enumerate(l) if not item]
    destination = arr[-1]
    position = arr[0]
    jumper = 0
    while not position == destination:
        value = position + 2
        if value in arr:
            jumper += 1
            position = value
        else:
            value = position + 1
            jumper += 1
            position = value
    else:
        return jumper


if __name__ == "__main__":
    n = int(input())
    c = [int(k) for k in input().split()]
    solution = jump(c)
    print(solution)
