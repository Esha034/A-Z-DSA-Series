Approach 1 — Brute Force: Three Loops

"Find every combination of 3 elements."


#code

class Solution:
    def threeSum(self, nums):
        n = len(nums)
        ans = []


        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):


                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]
                        triplet.sort()


                        if triplet not in ans:
                            ans.append(triplet)


        return ans

Complexity:

Time: O(n3)
Space: O(number of unique triplets)

Idea:

"The brute-force approach is to use three nested loops to consider every combination of three indices.
If their sum is zero, I add the triplet to the result after ensuring that duplicate triplets are not included. 
Since I examine three indices, the time complexity is O(n³)."






Approach 2 — Better: Hash Set


#Code
class Solution:
    def threeSum(self, nums):
        n = len(nums)
        ans = set()


        for i in range(n):


            seen = set()


            for j in range(i + 1, n):


                required = -(nums[i] + nums[j])


                if required in seen:
                    triplet = [nums[i], nums[j], required]
                    triplet.sort()
                    ans.add(tuple(triplet))


                seen.add(nums[j])


        return [list(triplet) for triplet in ans]

Complexity:

Time: O(n2)
Space: O(n)

Idea:

"For every fixed element, I reduce the remaining problem to Two Sum. 
I use a hash set to check whether the required third value has already been seen.
This reduces the time complexity from O(n³) to O(n²), but requires O(n) extra space.
I also use a set for the final triplets to remove duplicates."






Approach 3 — Optimal: Sorting + Two Pointers 

#code

class Solution:
    def threeSum(self, nums):
        nums.sort()

        n = len(nums)
        ans = []

        for i in range(n - 2):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return ans

#complexity

Time: O(n²)
space: O(1) 

