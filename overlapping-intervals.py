array_of_intervals  = [[1,3], [2,4], [6,8]]
#                     [[1, 4], [6,8]]

def merge_intervals(intervals):
    i=0
    while i<len(intervals)-1:
        j=i+1
        while j<len(intervals):
            print(intervals)
            
            # check if ther is overlapping set the new array and remove the unwanted inex
            if intervals[i][1] >= intervals[j][0] and intervals[i][1] <= intervals[j][1]:
                if intervals[i][0]< intervals[j][0]:
                    intervals[j][0] = intervals[i][0]
                    intervals.remove(intervals[i])
                    j+=1
                else:
                    intervals.remove(intervals[i])
                    j+=1
            j+=1
        i+=1
        
    return intervals

intervals123 = merge_intervals(array_of_intervals)
print(intervals123)