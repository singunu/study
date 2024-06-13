package poly.ex5;

public class Cat implements InterfaceAnimal{
    @Override
    public void sound() {
        System.out.println("먀");
    }

    @Override
    public void move() {
        System.out.println("이동");
    }
}
