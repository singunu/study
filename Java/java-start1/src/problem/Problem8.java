package problem;
import java.util.Scanner;
public class Problem8 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sum = 0;
        int cnt = 0;
        System.out.println("숫자를 입력하세요. 입력을 중단하려면 -1을 입력하세요.");
        while (true) {
            int num = scanner.nextInt();

            if (num == -1) {
                double avg = sum / cnt;
                System.out.println("입력한 숫자들의 합계 : " + sum);
                System.out.println("입력한 숫자들의 평균 : " + avg);
                break;
            }
            sum += num;
            cnt++;
        }

    }
}
