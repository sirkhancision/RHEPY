def highest_score(types, scores_table, sorted_types):
    """
    Select the type with the highest score
    """
    highest_score = sorted_types[-1]

    if not all(types):
        raise ValueError("Test score is zero")

    for score, type in scores_table.items():
        if score == highest_score:
            return type


def wing_tie(types, scores_table, sorted_types):
    """
    In case there are two top types with the same score, select
    the one with higher scored wings
    """
    second_highest = 0
    wing_sum = 0

    if not all(types):
        raise ValueError("Test score is zero")

    if sorted_types[-1] == sorted_types[-2]:
        for score, type in scores_table.items():
            if sorted_types[-2] == score and type != types["result"]:
                second_highest = type
                break

    wing_scores = [
        scores_table[score]
        for score, type in scores_table.items()
        if type == types["result"] or type == second_highest
    ]

    for index, score in enumerate(wing_scores):
        wing_sum += (index + 1) * score

    if wing_sum < 5 * 2 * (second_highest + sorted_types[-2]):
        return second_highest


def check_triads(types):
    """
    Check if the score correlates to the triad groups for a type,
    and select it if so
    """
    if all(types) == 0:
        raise ValueError("Test score is zero")

    groups_triads = {
        "intelligence": {
            "feeling": types["f_2"] + types["c_3"] + types["e_4"],
            "thinking": types["h_5"] + types["b_6"] + types["i_7"],
            "instinct": types["a_9"] + types["g_8"] + types["d_1"],
        },
        "hornevian": {
            "assertive": types["c_3"] + types["i_7"] + types["g_8"],
            "dutiful": types["d_1"] + types["f_2"] + types["b_6"],
            "withdrawn": types["e_4"] + types["h_5"] + types["a_9"],
        },
        "harmonic": {
            "positive": types["f_2"] + types["i_7"] + types["a_9"],
            "reactive": types["e_4"] + types["b_6"] + types["g_8"],
            "competency": types["d_1"] + types["c_3"] + types["h_5"],
        },
    }

    checks = [
        (
            groups_triads["intelligence"]["instinct"]
            > groups_triads["intelligence"]["thinking"]
            and groups_triads["intelligence"]["instinct"]
            > groups_triads["intelligence"]["feeling"]
            and groups_triads["hornevian"]["dutiful"]
            > groups_triads["hornevian"]["assertive"]
            and groups_triads["hornevian"]["dutiful"]
            > groups_triads["hornevian"]["withdrawn"]
            and groups_triads["harmonic"]["competency"]
            > groups_triads["harmonic"]["reactive"]
            and groups_triads["harmonic"]["competency"]
            > groups_triads["harmonic"]["positive"]
        ),
        (
            groups_triads["intelligence"]["feeling"]
            > groups_triads["intelligence"]["thinking"]
            and groups_triads["intelligence"]["feeling"]
            > groups_triads["intelligence"]["instinct"]
            and groups_triads["hornevian"]["dutiful"]
            > groups_triads["hornevian"]["assertive"]
            and groups_triads["hornevian"]["dutiful"]
            > groups_triads["hornevian"]["withdrawn"]
            and groups_triads["harmonic"]["positive"]
            > groups_triads["harmonic"]["reactive"]
            and groups_triads["harmonic"]["positive"]
            > groups_triads["harmonic"]["competency"]
        ),
        (
            groups_triads["intelligence"]["feeling"]
            > groups_triads["intelligence"]["thinking"]
            and groups_triads["intelligence"]["feeling"]
            > groups_triads["intelligence"]["instinct"]
            and groups_triads["hornevian"]["assertive"]
            > groups_triads["hornevian"]["dutiful"]
            and groups_triads["hornevian"]["assertive"]
            > groups_triads["hornevian"]["withdrawn"]
            and groups_triads["harmonic"]["competency"]
            > groups_triads["harmonic"]["reactive"]
            and groups_triads["harmonic"]["competency"]
            > groups_triads["harmonic"]["positive"]
        ),
        (
            groups_triads["intelligence"]["feeling"]
            > groups_triads["intelligence"]["thinking"]
            and groups_triads["intelligence"]["feeling"]
            > groups_triads["intelligence"]["instinct"]
            and groups_triads["hornevian"]["withdrawn"]
            > groups_triads["hornevian"]["dutiful"]
            and groups_triads["hornevian"]["withdrawn"]
            > groups_triads["hornevian"]["assertive"]
            and groups_triads["harmonic"]["reactive"]
            > groups_triads["harmonic"]["competency"]
            and groups_triads["harmonic"]["reactive"]
            > groups_triads["harmonic"]["positive"]
        ),
        (
            groups_triads["intelligence"]["thinking"]
            > groups_triads["intelligence"]["feeling"]
            and groups_triads["intelligence"]["thinking"]
            > groups_triads["intelligence"]["instinct"]
            and groups_triads["hornevian"]["withdrawn"]
            > groups_triads["hornevian"]["dutiful"]
            and groups_triads["hornevian"]["withdrawn"]
            > groups_triads["hornevian"]["assertive"]
            and groups_triads["harmonic"]["competency"]
            > groups_triads["harmonic"]["reactive"]
            and groups_triads["harmonic"]["competency"]
            > groups_triads["harmonic"]["positive"]
        ),
        (
            groups_triads["intelligence"]["thinking"]
            > groups_triads["intelligence"]["feeling"]
            and groups_triads["intelligence"]["thinking"]
            > groups_triads["intelligence"]["instinct"]
            and groups_triads["hornevian"]["dutiful"]
            > groups_triads["hornevian"]["withdrawn"]
            and groups_triads["hornevian"]["dutiful"]
            > groups_triads["hornevian"]["assertive"]
            and groups_triads["harmonic"]["reactive"]
            > groups_triads["harmonic"]["competency"]
            and groups_triads["harmonic"]["reactive"]
            > groups_triads["harmonic"]["positive"]
        ),
        (
            groups_triads["intelligence"]["thinking"]
            > groups_triads["intelligence"]["feeling"]
            and groups_triads["intelligence"]["thinking"]
            > groups_triads["intelligence"]["instinct"]
            and groups_triads["hornevian"]["assertive"]
            > groups_triads["hornevian"]["withdrawn"]
            and groups_triads["hornevian"]["assertive"]
            > groups_triads["hornevian"]["dutiful"]
            and groups_triads["harmonic"]["positive"]
            > groups_triads["harmonic"]["competency"]
            and groups_triads["harmonic"]["positive"]
            > groups_triads["harmonic"]["reactive"]
        ),
        (
            groups_triads["intelligence"]["instinct"]
            > groups_triads["intelligence"]["feeling"]
            and groups_triads["intelligence"]["instinct"]
            > groups_triads["intelligence"]["thinking"]
            and groups_triads["hornevian"]["assertive"]
            > groups_triads["hornevian"]["withdrawn"]
            and groups_triads["hornevian"]["assertive"]
            > groups_triads["hornevian"]["dutiful"]
            and groups_triads["harmonic"]["reactive"]
            > groups_triads["harmonic"]["competency"]
            and groups_triads["harmonic"]["reactive"]
            > groups_triads["harmonic"]["positive"]
        ),
        (
            groups_triads["intelligence"]["instinct"]
            > groups_triads["intelligence"]["feeling"]
            and groups_triads["intelligence"]["instinct"]
            > groups_triads["intelligence"]["thinking"]
            and groups_triads["hornevian"]["withdrawn"]
            > groups_triads["hornevian"]["assertive"]
            and groups_triads["hornevian"]["withdrawn"]
            > groups_triads["hornevian"]["dutiful"]
            and groups_triads["harmonic"]["positive"]
            > groups_triads["harmonic"]["reactive"]
            and groups_triads["harmonic"]["positive"]
            > groups_triads["harmonic"]["positive"]
        ),
    ]

    for index, check in enumerate(checks, start=1):
        if check:
            return index


def result_type(types):
    """
    Calculates the Enneagram Type, using various methods
    """
    scores_table = {
        types["d_1"]: 1,
        types["f_2"]: 2,
        types["c_3"]: 3,
        types["e_4"]: 4,
        types["h_5"]: 5,
        types["b_6"]: 6,
        types["i_7"]: 7,
        types["g_8"]: 8,
        types["a_9"]: 9,
    }

    sorted_types = sorted(types.values())

    try:
        types["result"] = highest_score(types, scores_table, sorted_types)
        types["result"] = (wing_tie(types, scores_table, sorted_types) or
                           types["result"])
        types["result"] = check_triads(types) or types["result"]
    except ValueError:
        raise ValueError("Test score is zero")

    return types["result"]


def result_wing(types):
    """
    Calculates the Enneagram Type's wing

    It just checks which type, corresponding to the wing of the matched basic
    type, has a higher score, and assigns the respective wing to it
    """
    match types["result"]:
        case 1:
            if types["a_9"] == types["f_2"]:
                wing = 0
            elif types["a_9"] > types["f_2"]:
                wing = 9
            else:
                wing = 2
        case 2:
            if types["d_1"] == types["c_3"]:
                wing = 0
            elif types["d_1"] > types["c_3"]:
                wing = 1
            else:
                wing = 3
        case 3:
            if types["f_2"] == types["e_4"]:
                wing = 0
            elif types["f_2"] > types["e_4"]:
                wing = 2
            else:
                wing = 4
        case 4:
            if types["c_3"] == types["h_5"]:
                wing = 0
            elif types["c_3"] > types["h_5"]:
                wing = 3
            else:
                wing = 5
        case 5:
            if types["e_4"] == types["b_6"]:
                wing = 0
            elif types["e_4"] > types["b_6"]:
                wing = 4
            else:
                wing = 6
        case 6:
            if types["h_5"] == types["i_7"]:
                wing = 0
            elif types["h_5"] > types["i_7"]:
                wing = 5
            else:
                wing = 7
        case 7:
            if types["b_6"] == types["g_8"]:
                wing = 0
            elif types["b_6"] > types["g_8"]:
                wing = 6
            else:
                wing = 8
        case 8:
            if types["i_7"] == types["a_9"]:
                wing = 0
            elif types["i_7"] > types["a_9"]:
                wing = 7
            else:
                wing = 9
        case 9:
            if types["g_8"] == types["d_1"]:
                wing = 0
            elif types["g_8"] > types["d_1"]:
                wing = 8
            else:
                wing = 1
        case _:
            wing = 0

    return wing
