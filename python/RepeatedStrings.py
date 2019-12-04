#
# https://www.hackerrank.com/challenges/repeated-string
# Lilah has a string, , of lowercase English letters that she repeated
# infinitely many times.
# Given an integer, , find and print the number of letter a's in the first
# letters of Lilah's infinite string.
# For example, if the string  and , the substring we consider is , the first
# characters of her infinite string.
# There are  occurrences of a in the substring.
#


def problem(string: str, elements: int) -> int:
    count = 0
    for i in string:
        if i == "a":
            count += 1
    q = elements // len(string)
    result = q * count
    r = elements % len(string)

    if r > 0:
        t = string[:r]
        for i in t:
            if i == "a":
                result += 1

    return result


if __name__ == "__main__":
    s = input()
    n = int(input())
    solution = problem(s, n)
    print(solution)
