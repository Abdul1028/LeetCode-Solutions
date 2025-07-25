class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left = 0 
        max_score = 0
        current_sum = 0 
        seen = set()
        for right in range(len(nums)):

            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1
            seen.add(nums[right])
            current_sum += nums[right]
            max_score = max(current_sum, max_score)
        
        return max_score

