#
# https://www.hackerrank.com/challenges/counting-valleys
# Gary is an avid hiker. He tracks his hikes meticulously, paying close
# attention to small details like topography.
# During his last hike he took exactly  steps.
# For every step he took, he noted if it was an uphill, , or a downhill,  step.
# Gary's hikes start and end at sea level and each step up or down represents
# a  unit change in altitude.
# We define the following terms:
#
# Solution:
#
# Basically we do plus and minus and keep checking if we reached the sea level
# or not
# at position when we reach sea level and the step is up/U; that means we have
# covered one full valley
#


import os


def counting_valleys(n, s):
    level = 0
    valleys = 0
    for step in s:
        if step == "U":
            level += 1
        if step == "D":
            level -= 1
        if level == 0 and step == "U":
            # we keep checking for every step; have we reached the sea level
            # and if yes then what step made that happen; if its `U` then its
            # like we have
            # covered one full valley
            valleys += 1
    return valleys


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input())

    s = input()

    result = counting_valleys(n, s)

    fptr.write(str(result) + "\n")

    fptr.close()
