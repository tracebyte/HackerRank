#
# https://www.hackerrank.com/challenges/2d-array/
# Given a  2D Array, :
# We define an hourglass in  to be a subset of values with indices falling in
# this pattern
# in arr's graphical representation:
# a b c
#   d
# e f g
# TLDR;
# ...


N = 6


class HourGlass:
    def __init__(self, arr):
        self.arr = arr
        self.max_hourglass = -100

    def get_max_hourglass(self):
        for i in range(1, 5):
            for j in range(1, 5):
                t = self.arr[i][j]
                t += self.arr[i - 1][j] + self.arr[i - 1][j - 1] + self.arr[i - 1][j + 1]
                t += self.arr[i + 1][j] + self.arr[i + 1][j - 1] + self.arr[i + 1][j + 1]
                if t >= self.max_hourglass:
                    self.max_hourglass = t
        return self.max_hourglass


if __name__ == "__main__":
    hourglasses = [[int(i) for i in input().strip().split()] for i in range(N)]
    hours = HourGlass(hourglasses)
    print(hours.get_max_hourglass())
