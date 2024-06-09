package problem2;
import java.util.Scanner;
public class Problem2 {
    public static void main(String[] args) {
        System.out.println("5개의 정수를 입력하세요:");
        Scanner input = new Scanner(System.in);
        int i = 0;
        int[] arr = new int[5];
        while (i < arr.length) {
            int intValue = input.nextInt();
            arr[i] = intValue;
            i++;
        }
        for (int j = 0; j < arr.length; j++) {
            if (j + 1 == arr.length) {
                System.out.print(arr[j]);
            }
            else {
                System.out.print(arr[j]+", ");
            }
        }

    }
}
