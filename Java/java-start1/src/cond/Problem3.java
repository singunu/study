package cond;

public class Problem3 {
    public static void main(String[] args) {
        int dollor = 2;
        String result;
        if (dollor > 0) {
            dollor *= 1300;
            System.out.println("환전 금액은 "+ dollor+"원입니다.");
        } else if (dollor == 0) {
            System.out.println("환전할 금액이 없습니다.");
        }
        else {
            System.out.println("잘못된 금액입니다.");
        }
    }
}
