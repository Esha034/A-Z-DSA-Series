Optimal (XOR)
#Idea 
Every number except one appears exactly twice.
XOR has the property that a number XOR itself becomes 0,
so all duplicate numbers cancel each other.
The only remaining value is the single number.

#code
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=0
        for num in nums:
            res^=num
        return res

#Complexity
Time: O(n)
Space: O(1)



Better (Hashing)
#Idea 
I store the frequency of every element using a hash map. 
Then I find the element whose frequency is 1.

#Algorithm
Create a dictionary.
Count the frequency of each number.
Traverse the dictionary.
Return the key whose frequency is 1.

#code
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in freq:
            if freq[num] == 1:
                return num

#Complexity
Time: O(n)
One traversal for counting.
One traversal to find the answer.

Space: O(n)
Hash map stores frequencies.


Brute Force (Linear Search)

#Idea 
For every element, I count how many times it appears in the array. 
The element with frequency 1 is the answer.

#Algorithm
Traverse every element.
Count its frequency by traversing the array again.
If frequency is 1, return that element.

#code
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            count=0
            for j in range(n):
                if nums[i]==nums[j]:
                    count+=1
            if count==1:
                return nums[i]

#Complexity
Time: O(n²)
Space: O(1)





  

