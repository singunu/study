package poly.ex1;

public class AnimalSoundMain {
    public static void main(String[] args) {
        Dog dog = new Dog();
        Cat cat = new Cat();
        Cow cow = new Cow();

        System.out.println("동물소리 테스트 시작");
        dog.sound();
        cat.sound();
        cow.sound();

        System.out.println("동물소리 테스트 종료");
    }
}
