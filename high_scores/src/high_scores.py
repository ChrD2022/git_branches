def latest(score_list):
    return score_list[-1]

def personal_best(scores):
    return max(scores)

def personal_top_three(scores):
    scores.sort()
    return [scores[-1], scores[-2], scores[-3]]

def high_to_low_scores(scores):
    scores.sort(reverse=True)
    return scores

