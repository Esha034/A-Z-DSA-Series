1. HashMap approach — O(n) time, O(n) space

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        freqmap = {}

        for num in nums:
            if num in freqmap:
                freqmap[num] += 1
            else:
                freqmap[num] = 1

            if freqmap[num] > n // 2:
                return num


Interview explanation:

I will use a HashMap to maintain the frequency of each element.

I traverse the array and check whether the current element exists in the dictionary.
- If it exists, I increment its frequency.
- Otherwise, I insert it with an initial frequency of one.
- After updating the frequency, I check whether it has exceeded n divided by 2.
- If it has, I return that element because it is the majority element.
Since the problem guarantees that a majority element always exists, I will definitely find and return it.

Complexity:
- Time: O(n) average — one traversal, with O(1) average dictionary operations.
- Space: O(n) — in the worst case, the dictionary can store all distinct elements.




2. Boyer–Moore Voting Algorithm — O(n) time, O(1) space


The intuition: Imagine every occurrence of the majority element gets one vote, and every occurrence of another element cancels one vote.

Because the majority element appears more than half the time, it cannot be completely cancelled out.

#code
  
  class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num

            if num == candidate:
                count += 1
            else:
                count -= 1

        return candidate


Understand the variables
- candidate: The element currently considered as the majority element.
- count: The current voting balance.

Complexity
- Time: O(n) — only one traversal.
- Space: O(1) — only two variables are maintained.
