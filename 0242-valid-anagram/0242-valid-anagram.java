class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        // HashMap<Character, Integer> sCount = new HashMap<>();
        // HashMap<Character, Integer> tCount = new HashMap<>();

        // for (int i = 0; i < s.length(); i ++){
        //     sCount.put(s.charAt(i), sCount.getOrDefault(s.charAt(i), 0) + 1);
        //     tCount.put(t.charAt(i), tCount.getOrDefault(t.charAt(i), 0) + 1);
        
        // }
        // return sCount.equals(tCount);
        int[] count = new int[26];
        for(int i = 0; i < s.length(); i ++){
            count[s.charAt(i) - 'a'] ++; 
            count[t.charAt(i) - 'a'] --; 
        }

        for (int val: count){
            if(val != 0){
                return false;
            }
        }
        return true;

    }
}