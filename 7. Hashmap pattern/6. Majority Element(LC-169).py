1. HashMap approach — O(n) time, O(n) space
Your code is incomplete, but you can complete it like this:
class Solution:    def majorityElement(self, nums: list[int]) -> int:        n = len(nums)        freqmap = {}        for num in nums:            if num in freqmap:                freqmap[num] += 1            else:                freqmap[num] = 1            if freqmap[num] > n // 2:                return num



Interview explanation
"I will use a HashMap to maintain the frequency of each element.

I traverse the array and check whether the current element exists in the dictionary.
- If it exists, I increment its frequency.
- Otherwise, I insert it with an initial frequency of one.
- After updating the frequency, I check whether it has exceeded n divided by 2.
- If it has, I return that element because it is the majority element.
Since the problem guarantees that a majority element always exists, I will definitely find and return it."
Dry run
Input:
nums = [2, 2, 1, 1, 1, 2, 2]



Here, n = 7, so:
\[
\lfloor n/2 \rfloor = 3
\]

The majority element must occur more than 3 times.
Iteration	Current number	Dictionary	Frequency > 3?
1	2	{2: 1}	No
2	2	{2: 2}	No
3	1	{2: 2, 1: 1}	No
4	1	{2: 2, 1: 2}	No
5	1	{2: 2, 1: 3}	No
6	2	{2: 3, 1: 3}	No
7	2	{2: 4, 1: 3}	Yes

Output: 2
Complexity
- Time: O(n) average — one traversal, with O(1) average dictionary operations.
- Space: O(n) — in the worst case, the dictionary can store all distinct elements.

2. Boyer–Moore Voting Algorithm — O(n) time, O(1) space
Best space-efficient approach
This is a very important interview algorithm.

The intuition: Imagine every occurrence of the majority element gets one vote, and every occurrence of another element cancels one vote.

Because the majority element appears more than half the time, it cannot be completely cancelled out.
Code
class Solution:    def majorityElement(self, nums: list[int]) -> int:        candidate = None        count = 0        for num in nums:            if count == 0:                candidate = num            if num == candidate:                count += 1            else:                count -= 1        return candidate



Understand the variables
- candidate: The element currently considered as the majority element.
- count: The current voting balance.
Dry run
Input:
