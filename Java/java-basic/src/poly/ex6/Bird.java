package poly.ex6;

public class Bird extends AbstractAnimal implements Fly{
    @Override
    public void sound() {
        System.out.println("끽");
    }

    @Override
    public void fly() {
        System.out.println("펄-럭");
    }
}
