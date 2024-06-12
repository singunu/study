package poly.basic;

public class CastingMain6 {
    public static void main(String[] args) {
        Parent parent1 = new Parent();
        Parent parent2 = new Child();
        System.out.println("parent1 호출");
        call(parent1);
        System.out.println("parent2 호출");
        call(parent2);
    }
    private static void call(Parent parent) {
        parent.parentMethod();

        if (parent instanceof Child child) {
            System.out.println("Child~");
            child.childMethod();
        } else {
            System.out.println("Not Child~");
        }
    }
}
