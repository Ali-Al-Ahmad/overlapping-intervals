"overlapping Intervals"

def _merge_intervals(intervals_array):
    intervals_array.sort()

    merged_array = [intervals_array[0]]

    for current in intervals_array[1:]:
        last_merged = merged_array[-1]

        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged_array.append(current)

    return merged_array
