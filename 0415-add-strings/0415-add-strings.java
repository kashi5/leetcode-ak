class Solution {
    public String addStrings(String num1, String num2) {
        StringBuilder sb = new StringBuilder();
        int carry = 0;
        int num1_l =num1.length()-1;
        int num2_l= num2.length()-1;
        int result = 0;
        while((num1_l >= 0 ) || (num2_l >=0)){
            int c = 0;
            int m =0;
            if (num1_l>= 0){
                c = num1.charAt(num1_l) - '0';
            } 
            if (num2_l>= 0) {
                 m = num2.charAt(num2_l) - '0';
            }
            int sum = carry + c + m;
            carry = sum/10;
            result = sum%10;
            sb.insert(0,result);
            num1_l --;
            num2_l --;
        }
        if (carry !=0 )sb.insert(0,carry);
        return new String(sb);
    }
}