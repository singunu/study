package poly.ex2;

public class AnimalPolyMain {
    public static void main(String[] args) {
        Dog dog = new Dog();
        Cat cat = new Cat();
        Cow cow = new Cow();

        Animal[] animals = {dog, cat, cow};

        for (Animal animal : animals) {
            System.out.println("동물 소리");
            animal.sound();
        }
    }
}
