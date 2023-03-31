import numpy as np

def get_annual_cost():
    cost_per_downtime = 1000

    # let's simulate 10000 starting minutes of the 2 jobs
    n = 10000
    task1 = np.random.randint(0, 300, size=n)
    task2 = np.random.randint(0, 300, size=n)

    # let's find the overlaps and calculate the probability of the overlaps
    overlaps = sum(abs(task1-task2) <= 60)
    prob_overlap = overlaps / n

    # return the annual cost estimate based on the probability
    return prob_overlap * 365 * cost_per_downtime
