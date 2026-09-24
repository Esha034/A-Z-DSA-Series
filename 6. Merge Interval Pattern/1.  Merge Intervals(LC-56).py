#optimal code

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        result = [intervals[0]]

        for i in range(1, len(intervals)):
            current = intervals[i]
            last = result[-1]

            # Overlapping
            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])

            # Non-overlapping
            else:
                result.append(current)

        return result











class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()

        n=len(intervals)

        start1=intervals[0][0]
        end1=intervals[0][1]

        res=[]

        for i in range(1,n):
            start2=intervals[i][0]
            end2=intervals[i][1]

            if end1>=start2:
            
                end1=max(end1,end2)
            
            else:
                res.append([start1, end1])
                start1=start2
                end1=end2
                
        res.append([start1,end1])

        return res


    
