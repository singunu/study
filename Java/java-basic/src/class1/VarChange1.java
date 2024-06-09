package class1;

public class VarChange1 {
    public static void main(String[] args) {
        Data dataA = new Data();
        dataA.value = 10;
        Data dataB = dataA;
        System.out.println("dataA 참조값=" + dataA);
        System.out.println("dataB 참조값=" + dataB);
        System.out.println("dataA.value = " + dataA.value);
        System.out.println("dataB.value = " + dataB.value);
        //dataA 변경
        dataA.value = 20;
        System.out.println("변경 dataA.value = 20");
        System.out.println("dataA.value = " + dataA.value);
        System.out.println("dataB.value = " + dataB.value);
        //dataB 변경
        dataB.value = 30;
        System.out.println("변경 dataB.value = 30");
        System.out.println("dataA.value = " + dataA.value);
        System.out.println("dataB.value = " + dataB.value);
    }
}
//dataA 참조값=ref.Data@x001
//dataB 참조값=ref.Data@x001
//dataA.value = 10
//dataB.value = 10
//변경 dataA.value = 20
//dataA.value = 20
//dataB.value = 20
//변경 dataB.value = 30
//dataA.value = 30
//dataB.value = 30
