package cond;

public class Problem1 {
    public static void main(String[] args) {
        int score = 60;
        String str1 = "학점은 ";
        String str2 = "입니다.";
        char result = 'F';
        if (score >= 90) {
            result = 'A';
        } else if (score >=80) {
            result = 'B';
        }
        else if (score >=70) {
            result = 'C';
        }
        else if (score >=60) {
            result = 'D';
        }
        else {
            result = 'F';
        }
        System.out.println(str1+result+str2);
    }
}
