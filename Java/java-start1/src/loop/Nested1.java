package loop;

public class Nested1 {
    public static void main(String[] args) {
        for (int i = 0; i < 2; i++) {
            System.out.println("외부 "+i);
            for (int j = 0; j < 3; j++) {
                System.out.println("내부 "+i+" "+j);
            }
            System.out.println();
        }
    }
}
//외부 0
//내부 0 0
//내부 0 1
//내부 0 2
//
//외부 1
//내부 1 0
//내부 1 1
//내부 1 2