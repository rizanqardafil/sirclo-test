class Cart:
    def __init__(self):
        self.products = {}

    def tambahProduk(self, kodeProduk, kuantitas):
        if kodeProduk in self.products:
            currentQuantity = self.products[kodeProduk]
            self.products[kodeProduk] = currentQuantity + kuantitas
        else:
            self.products[kodeProduk] = kuantitas

    def hapusProduk(self, kodeProduk):
        if kodeProduk in self.products:
            del self.products[kodeProduk]

    def tampilkanCart(self):
        for kodeProduk, kuantitas in self.products.items():
            print(f"{kodeProduk} ({kuantitas})")

keranjang = Cart()

keranjang.tambahProduk("Pisang Hijau", 2)
keranjang.tambahProduk("Semangka Kuning", 3)
keranjang.tambahProduk("Apel Merah", 1)
keranjang.tambahProduk("Apel Merah", 4)
keranjang.tambahProduk("Apel Merah", 2)

keranjang.hapusProduk("Semangka Kuning")
keranjang.hapusProduk("Semangka Merah")

keranjang.tampilkanCart()
