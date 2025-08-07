class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Create a hashmap to store number and its index
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i]; // Find the complement
            if (map.containsKey(complement)) {
                // If complement exists, return indices
                return new int[] { map.get(complement), i };
            }
            // Store current number and its index
            map.put(nums[i], i);
        }
        // No solution found (shouldn't happen per problem constraints)
        return new int[0];
    }
}
