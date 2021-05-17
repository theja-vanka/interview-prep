# O(NlogN) space | O(N) time
def mergeOverlappingIntervals(intervals):
    sortedIntervals = sorted(intervals, key=lambda x: x[0])

    mergedIntervals = []
    currentInterval = sortedIntervals[0]
    mergedIntervals.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, currentIntervalEnd = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        if currentIntervalEnd >= nextIntervalStart:
            currentInterval[1] = max(currentIntervalEnd, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            mergedIntervals.append(currentInterval)

    return mergedIntervals


# O(NlogN) time | O(N) space
def mergeOverlappingIntervalsAlt(intervals):
    intervals.sort()
    current = 0
    pointer = 1
    print(intervals)
    while pointer < len(intervals):
        if intervals[current][1] >= intervals[pointer][0] and intervals[current][1] >= intervals[pointer][1]:
            del(intervals[pointer])
        elif intervals[current][1] >= intervals[pointer][0]:
            intervals[current][1] = intervals[pointer][1]
            del(intervals[pointer])
        else:
            current += 1
            pointer += 1
    print(pointer)
    print(intervals)
    return intervals[:current+1]
