1.Bruteforce Approach

#Idea
a. Rotate the array one step to the right.
b. Repeat this k times.
    
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        for i in range(k):
            t=nums[-1]
            for j in range(n-1,-1,-1):
                nums[j]=nums[j-1]
            nums[0]=t
#Complexity
Time: O(n × k) 
Space: O(1)




2.Better Approach
#Idea
Instead of rotating one step at a time,
directly place every element in its new position.
    
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        ans=[0]*n
        for i in range(n):
           ans[(i+k)%n]=nums[i]

        nums[:]=ans

#Complexity
Time: O(n)
Space: O(n)



3.Optimal Approach(Two pointer)

#Idea
uses the reversal algorithm: 
       a.reverse the entire array,
       b.then reverse the first k elements and 
       c.the remaining n-k elements.

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)

    def reverse(self,nums,left,right):
        while left<right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1



class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k%=n
        def reverse(left,right):
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)

#Complexity
Time: O(n)
Space: O(1) 

