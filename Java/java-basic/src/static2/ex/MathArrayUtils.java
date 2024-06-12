package static2.ex;

public class MathArrayUtils {
    public static int sum(int[] values) {
        int sum = 0;
        for (int i = 0; i < values.length; i++) {
            sum += values[i];
        }
        return sum;
    }
    public static double average(int[] values) {
        double sumValue = sum(values);
        return sumValue / values.length;
    }
    public static int min(int[] values) {
        int min = values[0];
        for (int i = 0; i < values.length; i++) {
            if (min > values[i]) {
                min = values[i];
            }
        }
        return min;
    }
    public static int max(int[] values) {
        int max = values[0];
        for (int i = 0; i < values.length; i++) {
            if (max < values[i]) {
                max = values[i];
            }
        }
        return max;
    }
}
