class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n=len(fruits)
        basket={}
        low,high=0,0
        res=0

        for high in range(n):
            if fruits[high] in basket:
                basket[fruits[high]]+=1
            else:
                basket[fruits[high]]=1

            if len(basket)<=2:
                res=max(res,high-low+1)

            while len(basket)>2:
                basket[fruits[low]]-=1
                if basket[fruits[low]]==0:
                    del basket[fruits[low]]
                low+=1
        return res



        
