package problem;
import java.util.Scanner;
public class Problem9 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sum = 0;
        while (true) {
            System.out.println("1 : 상품 입력, 2 : 결제, 3 : 프로그램 종료");
            int choose = scanner.nextInt();
            if (choose == 1) {
                scanner.nextLine();
                System.out.print("상품명을 입력하세요: ");
                String product = scanner.nextLine();
                System.out.print("상품의 가격을 입력하세요: ");
                int price = scanner.nextInt();
                System.out.print("구매 수량을 입력하세요: ");
                int quantity = scanner.nextInt();
                System.out.println("상품명:" + product + " 가격:" + price + " 수량:" + quantity + " 합계:" + price * quantity);
                sum += (price * quantity);
            } else if (choose == 2) {
                System.out.println("총 비용: " + sum);
            } else if (choose == 3) {
                System.out.println("프로그램을 종료합니다.");
                break;
            } else {
                System.out.println("올바른 옵션을 선택해주세요.");
            }
        }

    }
}
