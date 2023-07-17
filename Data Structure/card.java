import java.util.HashMap;
import java.util.Map;

public class Cart {
    private Map<String, Integer> products;

    public Cart() {
        products = new HashMap<>();
    }

    public void tambahProduk(String kodeProduk, int kuantitas) {
        if (products.containsKey(kodeProduk)) {
            int currentQuantity = products.get(kodeProduk);
            products.put(kodeProduk, currentQuantity + kuantitas);
        } else {
            products.put(kodeProduk, kuantitas);
        }
    }

    public void hapusProduk(String kodeProduk) {
        products.remove(kodeProduk);
    }

    public void tampilkanCart() {
        for (Map.Entry<String, Integer> entry : products.entrySet()) {
            System.out.println(entry.getKey() + " (" + entry.getValue() + ")");
        }
    }

    public static void main(String[] args) {
        Cart keranjang = new Cart();

        keranjang.tambahProduk("Pisang Hijau", 2);

        keranjang.tambahProduk("Semangka Kuning", 3);

        keranjang.tambahProduk("Apel Merah", 1);
        keranjang.tambahProduk("Apel Merah", 4);
        keranjang.tambahProduk("Apel Merah", 2);

        keranjang.hapusProduk("Semangka Kuning");

        keranjang.hapusProduk("Semangka Merah");

        keranjang.tampilkanCart();
    }
}
