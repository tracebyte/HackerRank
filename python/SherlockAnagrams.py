# https://www.hackerrank.com/challenges/sherlock-and-anagrams
# Two strings are anagrams of each other if the letters of one string can be
# rearranged to form the other string.
# Given a string, find the number of pairs of substrings of the string that
# are anagrams of each other.
#
# TLDR;
#
# Solution:
# This was tricky one: - I had no idea what anagrams were and wikipedia didn't
# help much !!
# In short - anagrams - if I give you a string arrange it to create another
# string
#
# In this problem the other strings are the ones we need to create and compare
# them against other substrings
# and check if they are anagrams
# e.g. 'MOM' - as every letter is an sub-string we can say
# 'M' is a substring of MOM
# So lets say 1st string I create is 'M', I can create another string 'M'
# All possible substring will be: ['M', 'MO', 'MM', 'O', 'OM']
#
# Breaking the problem into 2 parts:
# 1. Create all possible substrings of the given string
# 2. Compare all substrings with each other if anagrams exists increment count

# NOTE: This problem is Quadratic + Quadratic time - but it did pass all the
# tests
# Can we do better?? please fork or PR ;)


def sherlock_anagrams(s):
    combinations = []
    count = 0

    #
    # Generate all possible substrings for a given string
    #
    for i in range(len(s)):
        for j in range(i, len(s)):
            subs = "".join(sorted(s[i : j + 1]))
            if subs != s:
                combinations.append(subs)

    #
    # Iterate over the list of substrings and check for anagrams
    #
    for i in range(len(combinations) - 1):
        value = combinations[i]
        for j in range(i + 1, len(combinations)):
            if value == combinations[j]:
                count += 1

    return count


if __name__ == "__main__":
    q = int(input())

    for q_itr in range(q):
        string = input()
        result = sherlock_anagrams(string)
        print(result, flush=True)
