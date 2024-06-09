package problem2;
import java.util.Scanner;

public class Problem6 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int sum = 0;
//        int min = 999999999;
//        int max = -999999999;
        System.out.println("입력받을 숫자의 개수를 입력하세요: ");
        int num = input.nextInt();
        System.out.println(num + "개의 정수를 입력하세요: ");
        int[] arr = new int[num];
        int min, max;
        for (int i = 0; i < arr.length; i++) {
            arr[i] = input.nextInt();
        }
        min = max = arr[arr.length-1];
        for (int j = arr.length - 1; j > -1; j--) {
            if (arr[j] > max) {
                max = arr[j];
            }
            if (arr[j] < min) {
                min = arr[j];
            }
        }
        System.out.println("가장 작은 정수: " + min);
        System.out.println("가장 큰 정수: " + max);
    }
}
