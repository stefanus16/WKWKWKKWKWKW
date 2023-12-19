class Penduduk:
    def _init_(self, nama, usia):
        self.nama = nama
        self.usia = usia

class Node:
    def _init_(self, penduduk):
        self.penduduk = penduduk
        self.left = None
        self.right = None

class BinaryTree:
    def _init_(self):
        self.root = None

    def tambah_penduduk(self, nama, usia):
        new_penduduk = Penduduk(nama, usia)
        if self.root is None:
            self.root = Node(new_penduduk)
        else:
            self._tambah_penduduk_recursive(self.root, new_penduduk)

    def _tambah_penduduk_recursive(self, curr_node, new_penduduk):
        if new_penduduk.nama < curr_node.penduduk.nama:
            if curr_node.left is None:
                curr_node.left = Node(new_penduduk)
            else:
                self._tambah_penduduk_recursive(curr_node.left, new_penduduk)
        else:
            if curr_node.right is None:
                curr_node.right = Node(new_penduduk)
            else:
                self._tambah_penduduk_recursive(curr_node.right, new_penduduk)

    def tampilkan_nama_urut(self):
        result = []
        self._tampilkan_nama_urut_recursive(self.root, result)
        print("Daftar Penduduk:")
        for penduduk in result:
            print(f"{penduduk.nama} - {penduduk.usia} tahun")

    def _tampilkan_nama_urut_recursive(self, curr_node, result):
        if curr_node:
            self._tampilkan_nama_urut_recursive(curr_node.left, result)
            result.append(curr_node.penduduk)
            self._tampilkan_nama_urut_recursive(curr_node.right, result)

    def tampilkan_usia_urut(self):
        result = []
        self._tampilkan_usia_urut_recursive(self.root, result)
        print("Daftar Penduduk:")
        for penduduk in result:
            print(f"{penduduk.nama} - {penduduk.usia} tahun")

    def _tampilkan_usia_urut_recursive(self, curr_node, result):
        if curr_node:
            self._tampilkan_usia_urut_recursive(curr_node.left, result)
            result.append(curr_node.penduduk)
            self._tampilkan_usia_urut_recursive(curr_node.right, result)

# Contoh penggunaan
tree = BinaryTree()

while True:
    print("Pilih Menu:")
    print("1. Tambah Penduduk")
    print("2. Tampilkan Urut Nama")
    print("3. Tampilkan Urut Usia")
    print("0. Keluar")
    pilihan = int(input("Pilihan Anda: "))

    if pilihan == 0:
        break
    elif pilihan == 1:
        nama = input("Masukkan Nama: ")
        usia = int(input("Masukkan Usia: "))
        tree.tambah_penduduk(nama, usia)
        print("Data berhasil ditambahkan!")
    elif pilihan == 2:
        tree.tampilkan_nama_urut()
    elif pilihan == 3:
        tree.tampilkan_usia_urut()
    else:
        print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")