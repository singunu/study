package oop;

public class BookMain {
    public static void main(String[] args) {
        Book book1 = new Book("Hello Java", "Kim");
        Book book2 = new Book("JPA 프로그래밍", "Park", 89);
        book1.displayInfo();
        book2.displayInfo();
    }
}
