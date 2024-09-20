class MaximumSubarray{
    public static int maxSubArray(int[] nums) {
        int currSum = nums[0], maxSum = nums[0];
        for(int i =1;i<nums.length;i++){
            // currSum = max(nums[i], currSum + nums[i]);
            currSum = Math.max(nums[i], currSum + nums[i]);
            maxSum = Math.max(maxSum, currSum);
        }
        return maxSum;
    }
}