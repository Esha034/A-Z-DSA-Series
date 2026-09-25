class Solution:
    def isIntersect(self, intervals):
        
        intervals.sort()
        res=[intervals[0]]
        for i in range(1,n):
            current=intervals[i]
            last=res[-1]
            if current[0]<=last[1]:
                return True
            else:
                res.append(current)
        return False
