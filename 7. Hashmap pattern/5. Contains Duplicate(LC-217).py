1. Using a Set — Optimal approach

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n=len(nums)
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


Interview explanation:

I will use a Set to keep track of the elements I have already visited.

I iterate through the array one element at a time. Before inserting the current element into the Set, I check whether it already exists.
- If the element is already present, it means we have encountered a duplicate, so I immediately return True.
- Otherwise, I insert the element into the Set and continue.
- If the entire array is traversed without finding any duplicate, I return False.
I am using a Set because it stores only unique elements and provides average O(1) lookup and insertion."

  
Complexity analysis:
- Time Complexity: O(n) average — We traverse the array once. Set lookup and insertion take O(1) average time.
- Space Complexity: O(n) — In the worst case, all elements are distinct, so the Set stores all n elements.











2. Using a Dictionary (Frequency Map)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        freqmap = {}

        for i in range(n):
            if nums[i] in freqmap:
                freqmap[nums[i]] += 1
            else:
                freqmap[nums[i]] = 1

            if freqmap[nums[i]] > 1:
                return True

        return False


Interview explanation:

I will use a Dictionary to maintain the frequency of each element.

I traverse the array and check whether the current element already exists in the dictionary.
- If it exists, I increment its frequency by one.
- Otherwise, I insert it into the dictionary with an initial frequency of one.
- After updating the frequency, if it becomes greater than one, I know that the element has appeared more than once, so I return True.
- If no element has a frequency greater than one, I return False."


Complexity analysis:
- Time Complexity: O(n) average — Each dictionary lookup, insertion and update takes O(1) average time, and we traverse the array once.
- Space Complexity: O(n) — In the worst case, the dictionary stores n distinct elements.








My Learning:


Using a List — Why does it give TLE?

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        n = len(nums)
        seen = []

        for num in nums:
            if num in seen:
                return True
            seen.append(num)

        return False

When seen is a list, Python searches for the element sequentially, one element at a time.

Unlike a Set or Dictionary, a List does not provide average O(1) membership checking.

Complexity analysis:

- Time Complexity: O(n²) — Each list membership check can take O(n), and we perform it for every array element.
- Space Complexity: O(n) — In the worst case, all elements are distinct and are stored in seen.
