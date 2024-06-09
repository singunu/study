package problem2;
import java.util.Scanner;
public class Problem3 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int[] arr = new int[5];
        System.out.println("5개의 정수를 입력하세요: ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = input.nextInt();
        }
        for (int j = arr.length - 1; j > -1; j--) {
            if (j == 0) {
                System.out.print(arr[j]);
            }
            else {
                System.out.print(arr[j]+", ");
            }
        }
    }
}
