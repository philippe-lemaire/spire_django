import random


def roll(dice, difficulty=0):
    """Rolls a dice number of d10s, keeps the best one, and returns the dice pool for display and the text result."""
    offset = 0
    dice -= difficulty

    if dice < 1:
        dice = 1
        offset = 2
        print(
            f"Difficulty over dice pool, rolling 1 die but the result will be degraded by 2 steps"
        )

    pool = [random.randint(1, 10) for die in range(dice)]
    best = max(pool)

    result_ranges = [
        "Critical failure. Fail, and take double stress.",
        "Failure. Fail, and take stess.",
        "Success at a cost. Succeed, but take stress.",
        "Success. Succeed, and take no stress.",
        "Critical Success. Succeed dramatically, and increase outgoing stress dice by 1 step.",
    ]

    if best == 1:
        idx = 0
    elif best in range(1, 6):
        idx = 1
    elif best in range(6, 8):
        idx = 2
    elif best in range(8, 10):
        idx = 3
    elif best == 10:
        idx = 4

    print(f"{idx=}")
    idx -= offset

    res = result_ranges[max(idx, 0)]

    return pool, res


if __name__ == "__main__":
    print(roll(dice=5, difficulty=3))
