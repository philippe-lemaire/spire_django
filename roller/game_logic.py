import random


def roll(dice, difficulty=0):
    """Rolls a dice number of d10s, keeps the best one, and returns the dice pool for display and the text result."""
    offset = 0
    reduction = False
    dice -= difficulty

    if dice < 1:
        dice = 1
        offset = 2
        reduction = True

    pool = [random.randint(1, 10) for die in range(dice)]
    best = max(pool)

    extra_stress = pool.count(10)

    result_ranges = [
        "Échec critique. L’action échoue, et vous subissez le double du stress infligé normalement.",
        "Échec. L’action échoue, et vous subissez le stress.",
        "Succès avec coût. L’action réussit, mais vous subissez le stress.",
        "Succès. L’action réussit, et vous ne subissez aucun stress.",
        f"Succès critique ! L’action réussit admirablement. Si vous infligez du stress, ajoutez un bonus de {extra_stress}.",
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

    return pool, res, best, reduction
