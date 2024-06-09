package refactoring;

public class Ex2 {
    public static void main(String[] args) {
        String message = "Hello, world!";
        printMsg(message, 3);
    }
    public static void printMsg (String msg, int a) {
        for (int i = 0; i < a; i++) {
            System.out.println(msg);
        }
    }
}
