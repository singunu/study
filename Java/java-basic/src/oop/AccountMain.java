package oop;

public class AccountMain {
    public static void main(String[] args) {
        Account person1 = new Account();
        person1.deposit(10000);
        person1.withdraw(9000);
        person1.withdraw(2000);
    }
}
