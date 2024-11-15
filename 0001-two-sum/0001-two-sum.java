class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> indicies = new HashMap<>();

        for (int i = 0; i < nums.length; i ++){
            indicies.put(nums[i], i);
        }

        for(int i = 0; i < nums.length; i++){
            int diff = target - nums[i];
            if(indicies.containsKey(diff) && indicies.get(diff) != i){
                return new int[]{i , indicies.get(diff)};
            }
        }

        return new int[0];
    }
}