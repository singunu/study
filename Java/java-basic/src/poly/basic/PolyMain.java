package poly.basic;

public class PolyMain {
    public static void main(String[] args) {
        System.out.println("P->P");
        Parent parent = new Parent();
        parent.parentMethod();

        System.out.println("C->C");
        Child child = new Child();
        child.parentMethod();
        child.childMethod();

        System.out.println("P->C");
        Parent poly = new Child(); // 자식을 부모에 대입
        poly.parentMethod();
    }
}
