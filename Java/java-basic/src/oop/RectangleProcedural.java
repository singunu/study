package oop;

public class RectangleProcedural {
    int width;
    int height;

    void calculateArea () {
        System.out.println("넓이: " + width * height);
    }
    void calculatePerimeter () {
        System.out.println("둘레 길이: " +(width + height) * 2);
    }
    void isSquare () {
        boolean sqr = false;
        if (width == height) {
            sqr = true;
        }
        System.out.println("정사각형 여부: " + sqr);
    }
}
