package poly.ex.pay0;

public class NaverPay implements Pay {
    public boolean pay(int amount) {
        System.out.println("네이버페이 시스템과 연결");
        System.out.println(amount + "원 결제 시도");
        return true;
    }
}
