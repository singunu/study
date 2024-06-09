package problem2;
import java.util.Scanner;

public class Problem7 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String subject = "";
        int[][] arr = new int[4][3];
        for (int i = 0; i < arr.length; i++) {
            System.out.println(i + 1 + "번 학생의 성적을 입력하세요:");
            for (int j = 0; j < arr[i].length; j++) {
                if (j == 0) {
                    subject = "국어";
                } else if (j == 1) {
                    subject = "영어";
                } else {
                    subject = "수학";
                }
                System.out.print(subject+"점수: ");
                arr[i][j] = input.nextInt();
                input.nextLine();
            }
        }
        int sum = 0;
        for (int i = 0; i < arr.length; i++)
        {
            sum = 0;
            for (int j = 0; j < arr[i].length; j++) {
                sum += arr[i][j];
            }
            System.out.println(i + 1 + "번 학생의 총점: " + sum + ", 평균: " + (double)(sum / arr.length));
        }

    }
}
