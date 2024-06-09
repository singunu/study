package refactoring;

public class Ex1 {
    public static void main(String[] args) {

        System.out.println("평균값: "+ average(1,2,3));
        System.out.println("평균값: "+ average(15,25,35));


    }
    public static double average(double a, double b, double c) {
        double sum = a + b + c;
        double avg = sum / 3;
        return avg;
    }
}
