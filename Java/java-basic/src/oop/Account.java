package oop;

public class Account {
    int balance;

    void deposit (int amount) {
        balance += amount;
        System.out.println(amount + "원 입급되었습니다.");
        System.out.println("현재 잔액 : " + balance);
        System.out.println();
    }
    void withdraw (int amount) {
        if (amount > balance) {
            System.out.println(amount + "원을 출금합니다.");
            System.out.println("출금 불가 : " + (amount - balance) + "원 부족");
            System.out.println("현재 잔액 : " + balance);
            System.out.println();
        }
        else {
            balance -= amount;
            System.out.println(amount + "원 출금되었습니다.");
            System.out.println("현재 잔액 : " + balance);
            System.out.println();
        }
    }
}
