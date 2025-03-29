class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] temp = new int[nums1.length];
        for(int i=0;i<nums1.length;i++){
            temp[i] = nums1[i];
        }
        
        int j=0;
        int i=0;
        int k=0;
        while(true){
            if(i==m | j==n){
                break;
            }

            if(temp[i]<nums2[j] & (temp[i]!=0 | i<m)){
                nums1[k]=temp[i];
                i++;
            }
            else{
                nums1[k]=nums2[j];
                j++;
            }
            // System.out.println(nums1[k]+ " "+ i+" "+ j);            

            k++;

        }
        while(i<m){
            nums1[k]=temp[i];
                i++;
                k++;
        }
        while(j<n){
            nums1[k]=nums2[j];
                j++;
                k++;
        }
        
        System.out.println(nums1);
    }
}