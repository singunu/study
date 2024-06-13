package poly.ex3;

public class AbstractMain {
    public static void main(String[] args) {

        AbstractAnimal[] animals = {new Dog(), new Cat(), new Cow()};

        for (AbstractAnimal animal : animals) {
            animalSound(animal);

        }
    }

    private static void animalSound(AbstractAnimal animal) {
        animal.sound();
        animal.move();
    }
}
