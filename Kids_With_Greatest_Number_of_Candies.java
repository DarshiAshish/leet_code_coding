class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int m=-1;
        for(int i=0;i<candies.length;i++){
            m = Math.max(m, candies[i]);
        }
        ArrayList<Boolean> res=new ArrayList<Boolean>();
        for(int i=0;i<candies.length;i++){
            int t = candies[i] + extraCandies;
            if(t>=m){
                res.add(true);
            }
            else{
                res.add(false);
            }
        }
            return res;

    }
}class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int m=-1;
        for(int i=0;i<candies.length;i++){
            m = Math.max(m, candies[i]);
        }
        ArrayList<Boolean> res=new ArrayList<Boolean>();
        for(int i=0;i<candies.length;i++){
            int t = candies[i] + extraCandies;
            if(t>=m){
                res.add(true);
            }
            else{
                res.add(false);
            }
        }
            return res;

    }
}