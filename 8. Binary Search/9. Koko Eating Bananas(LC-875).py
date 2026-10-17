#Binary search on answer
Binary Search chooses a speed
          ↓
Calculate how many hours that speed needs
          ↓
Compare hours with h
          ↓
Decide whether speed should increase or decrease
          ↓
Try another speed


#optimsl code


class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Calculate hours needed at this speed
        def cal_hrs(speed):
            hrs=0
            for pile in piles:
                hrs+= pile//speed
                if pile%speed!=0:
                    hrs+=1
            return hrs

        low,high=1,max(piles)

        while low<=high:
            speed=(low+high)//2
            hours=cal_hrs(speed)
             # Fast enough → try a smaller speed
            if hours<=h:
                high=speed-1
            # Too slow → increase speed
            else:
                low=speed+1
        return low




class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)

        while low <= high:
            speed = (low + high) // 2

            hours = 0

            # Calculate hours needed at this speed
            for pile in piles:
                hours += (pile + speed - 1) // speed

             # Fast enough → try a smaller speed
            if hours <= h:
                ans = mid
                right = mid - 1
           # Too slow → increase speed
            else:
                left = mid + 1

        return ans








class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        n=len(piles)

        def hours_needed(speed):
            hr=0
            for pile in piles:
                hr+=pile//speed
                if pile%speed!=0:
                    hr+=1
            return hr
        

        low,high=1,max(piles)
        res=-1
        while low<=high:

            speed=(low+high)//2

            hr=hours_needed(speed)

            if hr>h:
                low=speed+1
            else:
                res=speed
                high=speed-1
        return res



        
         
