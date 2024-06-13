package poly.ex4;

public class Cat extends AbstractAnimal {
    @Override
    public void sound() {
        System.out.println("먀");
    }

    @Override
    public void move() {
        System.out.println("이동");
    }
}
