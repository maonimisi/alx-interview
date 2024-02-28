#!/usr/bin/python3
"""Function different values, determine the fewest number of coins
needed to meet a given amount total"""


def makeChange(coins, total):
    """Function returns fewest number of coint needed to meet totals"""
    if total < 1:
        return 0
    coins = sorted(coins, reverse=True)
    current_total = 0
    minimum_coins = 0
    for coin in coins:
        balance = (total - current_total) // coin
        current_total += balance * coin
        minimum_coins += balance
        if current_total == total:
            return minimum_coins
    return -1
