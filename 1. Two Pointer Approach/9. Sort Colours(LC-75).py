1. Brute Force 
#Idea
a. Create three separate arrays:
  red for 0s
  white for 1s
  blue for 2s
b. Traverse the array once and put each element into its respective array.
c.Merge all three arrays back.
  
#code
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        red=[]
        white=[]
        blue=[]
        for i in range(n):
            if nums[i]==0:
                red.append(nums[i])
            elif nums[i]==1:
                white.append(nums[i])
            else:
                blue.append(nums[i])
#Used slice assignment (nums[:] = ...)to overwrite the contents of the original nums array in-place.
        nums[:]=red+white+blue

#Complexity
Time: O(n)
Space: O(n) 
             

2. Better Approach (Counting approach)
# Idea
Since the array contains only three values (0, 1, 2):

a. Count how many 0s, 1s, and 2s are present.
b.Fill the array based on count:
 First all 0s
 Then all 1s
 Then all 2s
             
#code
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count0 = count1 = count2 = 0
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1
        i = 0
        while count0:
            nums[i] = 0
            i += 1
            count0 -= 1
        while count1:
            nums[i] = 1
            i += 1
            count1 -= 1
        while count2:
            nums[i] = 2
            i += 1
            count2 -= 1
          
#Complexity
Time: O(n)
Space: O(1)




3. Optimal Approach (Dutch National Flag Algorithm)
# Idea
Use 3 pointers:
  low → Next position for 0
  mid → Current element
  high → Next position for 2
             
#code
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n=len(nums)
        l,m,h=0,0,n-1
        while m<=h:
            if nums[m]==0:
                nums[l],nums[m]=nums[m],nums[l]
                l+=1
                m+=1
            elif nums[m]==1:
                m+=1
            else:
                nums[m],nums[h]=nums[h],nums[m]
                h-=1
#Complexity
Time: O(n) 
Space: O(1)
