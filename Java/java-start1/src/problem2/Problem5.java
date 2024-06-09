package problem2;
import java.util.Scanner;

public class Problem5 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int sum = 0;
        System.out.println("입력받을 숫자의 개수를 입력하세요: ");
        int num = input.nextInt();
        System.out.println(num + "개의 정수를 입력하세요: ");
        int[] arr = new int[num];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = input.nextInt();
        }
        for (int j = arr.length - 1; j > -1; j--) {
            sum += arr[j];
        }
        System.out.println("입력한 정수의 합계: "+ sum);
        System.out.println("입력한 정수의 평균: "+ (double) sum / arr.length);
    }
}
