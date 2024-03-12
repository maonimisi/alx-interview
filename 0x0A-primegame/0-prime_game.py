#!/usr/bin/python3
"""Prime Game - Maria and Ben are playing a game"""


def isWinner(rounds, numbers):
    """Determines the winner of the game."""
    if rounds <= 0 or numbers is None or rounds != len(numbers):
        return None

    ben_score = 0
    maria_score = 0

    primes = [1] * (max(numbers) + 1)
    primes[0], primes[1] = 0, 0

    for i in range(2, len(primes)):
        remove_multiples(primes, i)

    for num in numbers:
        if sum(primes[:num + 1]) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    return "Ben" if ben_score > maria_score else "Maria" \
           if maria_score > ben_score else None


def remove_multiples(lst, x):
    """Removes multiples of primes."""
    for i in range(2 * x, len(lst), x):
        try:
            lst[i] = 0
        except IndexError:
            break
