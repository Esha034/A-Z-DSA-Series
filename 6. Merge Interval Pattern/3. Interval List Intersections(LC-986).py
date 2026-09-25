class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        m=len(firstList)
        n=len(secondList)
        res=[]
        i,j=0,0
        while i <m and j<n
        :

            interval1=firstList[i]
            interval2=secondList[j]

            start=max(interval1[0],interval2[0])
            end=min(interval1[1],interval2[1])
            if start<=end:
                res.append([start,end])

            if interval1[1]<interval2[1]:
                i+=1
            else:
                j+=1


        return res

            
