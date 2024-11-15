class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> indicies = new HashMap<>();


        for(int i = 0; i < nums.length; i++){
            int num = nums[i];
            int diff = target - num;
            if(indicies.containsKey(diff)){
                return new int[]{i , indicies.get(diff)};
            }

            indicies.put(nums[i], i);
        }

        return new int[0];
    }
}