package cond;

public class Problem2 {
    public static void main(String[] args) {
        int distance = 15;
        String delivery;
        if (distance <= 1) {
            delivery = "도보";
        }
        else if (distance <= 10) {
            delivery = "자전거";
        }
        else if (distance <= 100) {
            delivery = "자동차";
        }
        else {
            delivery = "비행기";
        }
        System.out.println(delivery+"를 이용하세요.");
    }
}
