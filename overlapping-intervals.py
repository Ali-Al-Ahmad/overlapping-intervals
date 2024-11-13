"this function merger overlapping intervals"
array_of_intervals = [[6, 8], [1, 9], [2, 4], [4, 7]]

def _merge_intervals(intervals):
    for i in range(len(intervals)-1):
        for j in range(len(intervals)-1):
            if intervals[j][0] > intervals[j+1][0]:
                temp = intervals[j+1]
                intervals[j+1] = intervals[j]
                intervals[j] = temp

    i = 0
    while i < len(intervals):
        j = i+1
        while j < len(intervals):

            # check if their is overlapping set the new array and remove the unwanted inex
            if intervals[j][0] <= intervals[i][1] and intervals[i][1] <= intervals[j][1]:
                if intervals[i][0] < intervals[j][0]:
                    intervals[i][1] = intervals[j][1]
                    intervals.remove(intervals[j])
                    i = -1
                    break

                intervals[i] = intervals[j]
                intervals.remove(intervals[j])
                i = -1

            elif intervals[j][1] <= intervals[i][1] and intervals[i][0] <= intervals[j][1]:
                if intervals[j][0] < intervals[i][0]:
                    intervals[i][0] = intervals[j][0]
                    intervals.remove(intervals[j])
                    i = -1
                    break

                intervals.remove(intervals[j])
                i = -1
            j += 1
        i += 1

    return intervals

intervals123 = _merge_intervals(array_of_intervals)
print(intervals123)
