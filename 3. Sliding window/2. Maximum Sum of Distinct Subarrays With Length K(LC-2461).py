class Solution:
    def maximumSubarraySum(self, nums, k):
        freq = {}
        curr_sum = 0
        max_sum = 0

        # Build the first window
        for i in range(k):
            curr_sum += nums[i]

            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

        if len(freq) == k:
            max_sum = curr_sum

        # Slide the window
        for i in range(k, len(nums)):

            # Add incoming element
            curr_sum += nums[i]

            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

            # Remove outgoing element
            outgoing = nums[i - k]
            curr_sum -= outgoing
            freq[outgoing] -= 1

            if freq[outgoing] == 0:
                del freq[outgoing]

            # All k elements are distinct
            if len(freq) == k:
                if curr_sum > max_sum:
                    max_sum = curr_sum

        return max_sum

Complexity:

Time	O(n)
Space	O(k)
