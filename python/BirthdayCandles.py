# https://www.hackerrank.com/challenges/birthday-cake-candles
# You are in charge of the cake for your niece's birthday and have decided the
# cake will have one candle for
# each year of her total age. When she blows out the candles, she’ll only be
# able to blow out the tallest ones.
# Your task is to find out how many candles she can successfully blow out.
#
# TLDR;
#


def blow_candle(candles):
    maxy = -1
    count = 0

    for candle in candles:
        if candle > maxy == -1:
            maxy = candle
            count += 1
        elif candle == maxy:
            count += 1
        elif candle < maxy:
            pass
        else:
            maxy = candle
            count = 1

    return count


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().rstrip().split()))

    ans = blow_candle(arr)
    print(ans)
