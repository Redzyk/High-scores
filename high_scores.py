def latest(scores):
    return scores[-1]


def personal_best(scores):
    highest_num = sorted(scores)[-1]
    return highest_num


def personal_top_three(scores):
    three_highest = sorted(scores,reverse=True)
    return str(three_highest[0],three_highest[1],three_highest[2])