package oop;

public class RectangleProceduralMain {
    public static void main(String[] args) {
        RectangleProcedural rectangle = new RectangleProcedural();
        rectangle.width = 6;
        rectangle.height = 6;
        rectangle.calculateArea();
        rectangle.calculatePerimeter();
        rectangle.isSquare();
    }
}
