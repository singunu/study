package class1;

public class ProductOrderMain {
    public static void main(String[] args) {
        ProductOrder product1 = new ProductOrder();
        ProductOrder product2 = new ProductOrder();
        ProductOrder product3 = new ProductOrder();
        createOrtder(product1, "두부", 2000, 2);
        createOrtder(product2, "김치", 5000, 1);
        createOrtder(product3, "콜라", 1500, 2);
        ProductOrder[] products = new ProductOrder[]{product1,product2,product3};
        printOrder(products);
        getTotalAmount(products);
    }
    static void createOrtder(ProductOrder product, String name, int price, int quantity) {
        product.productName = name;
        product.price = price;
        product.quantity = quantity;
    }
    static void getTotalAmount(ProductOrder[] products) {
        int total = 0;
        for (ProductOrder product : products) {
            total += product.price * product.quantity;
        }
        System.out.println("총 결제 금액: " + total);
    }
    static void printOrder(ProductOrder[] products) {
        for (ProductOrder product : products) {
            System.out.println("상품명: " + product.productName + ", 가격: " + product.price + ", 수량: " + product.quantity);
        }
    }
}
