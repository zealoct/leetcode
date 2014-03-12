class Solution {
public:
    int singleNumber(int A[], int n) {
        int result = 0;
        for(int i=0;i<sizeof(int)*8;i++) {
            int c = 0;
            for(int j=0; j<n; j++) {
                c += (A[j] >> i) & 0x1;
            }
            
            result |= (c%3) << i;
        }
        return result;
    }
};