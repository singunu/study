package poly.ex5;

public class Cow implements InterfaceAnimal{
    @Override
    public void sound() {
        System.out.println("므~");
    }

    @Override
    public void move() {
        System.out.println("이동");
    }
}
