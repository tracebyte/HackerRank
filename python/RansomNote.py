# https://www.hackerrank.com/challenges/ctci-ransom-note/
#
# Harold is a kidnapper who wrote a ransom note, but now he is worried it will
# be traced back to him through his
# handwriting. He found a magazine and wants to know if he can cut out whole
# words from it and use them to create an
# untraceable replica of his ransom note. The words in his note are
# case-sensitive and he must use
# only whole words available in the magazine. He cannot use substrings or
# concatenation to create the words he needs.

# TLDR;

# PROBLEM 1
# 6 4
# give me one grand today night
# give one grand today

# Yes

# PROBLEM 2
# 6 5
# two times three is not four
# two times two is four

# No

# Solution:
#
# There are many ways of solving like using dictionaries with words - the keys
# and values using counter but python's
# built in method Counter does the job

from collections import Counter


def check_magazine(magazine, note):
    # yes this is kinda funny syntax - we remove
    # contents of ransom notes common in magazine
    # you ll end up with empty dict object if the note was created using all
    # the
    # magazine words
    if Counter(note) - Counter(magazine) == {}:
        return "YES"
    return "NO"


if __name__ == "__main__":
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine_words = input().rstrip().split()

    note_words = input().rstrip().split()

    res = check_magazine(magazine_words, note_words)

    print(res)
