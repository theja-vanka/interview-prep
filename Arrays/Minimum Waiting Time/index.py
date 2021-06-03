def minimumWaitingTime(queries):
    queries.sort()

    totalWaitingTime = 0
    for idx, duration in enumerate(queries):
        queriesLeft = len(queries) - (idx + 1)
        totalWaitingTime += duration * queriesLeft
    return totalWaitingTime


def minimumWaitingTimeAlt(queries):
    queries.sort()
    summation = 0
    lst = []
    for number in range(len(queries) - 1):
        summation += queries[number]
        lst.append(summation)
    return sum(lst)
