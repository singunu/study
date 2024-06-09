package problem2;

public class Problem1 {
    public static void main(String[] args) {
        int[] students = {90, 80, 70, 60, 50};
        int total = 0;
        for (int student : students) {
            total += student;
        }
        System.out.println("점수 총합: " + total);
        System.out.println("정수 평균: " + (double) total/ students.length);
    }
}
