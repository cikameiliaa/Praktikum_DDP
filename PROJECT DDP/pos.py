import tkinter as tk
from tkinter import messagebox

class AplikasiPOS:
    def __init__(self, master):
        self.master = master
        self.master.title("Aplikasi POS Struk Pembelian")


        # Variabel penyimpanan data barang
        self.data_barang = []

        # Label dan Entry untuk input nama barang
        self.label_barang = tk.Label(master, text="Nama Barang:")
        self.label_barang.pack(pady=5)
        self.entry_barang = tk.Entry(master)
        self.entry_barang.pack(pady=5)

        # Label dan Entry untuk input harga barang
        self.label_harga = tk.Label(master, text="Harga Barang:")
        self.label_harga.pack(pady=5)
        self.entry_harga = tk.Entry(master)
        self.entry_harga.pack(pady=5)

        # Tombol untuk menambahkan barang
        self.tombol_tambah = tk.Button(master, text="Tambah Barang", command=self.tambah_barang)
        self.tombol_tambah.pack(pady=10)

        # Listbox untuk menampilkan barang yang telah ditambahkan
        self.listbox_barang = tk.Listbox(master)
        self.listbox_barang.pack(pady=10)

        # Tombol untuk menghitung total harga
        self.tombol_hitung = tk.Button(master, text="Hitung Total Harga", command=self.hitung_total_harga)
        self.tombol_hitung.pack(pady=10)

        # Label untuk menampilkan total harga
        self.label_total_harga = tk.Label(master, text="")
        self.label_total_harga.pack(pady=5)

        # Tombol untuk mencetak struk
        self.tombol_cetak = tk.Button(master, text="Cetak Struk", command=self.cetak_struk)
        self.tombol_cetak.pack(pady=10)

    def tambah_barang(self):
        nama_barang = self.entry_barang.get().strip()
        harga_str = self.entry_harga.get().strip()

        if nama_barang and harga_str:
            try:
                harga = float(harga_str)
                self.data_barang.append({"nama": nama_barang, "harga": harga})
                self.listbox_barang.insert(tk.END, f"{nama_barang} - {harga}")
                self.entry_barang.delete(0, tk.END)
                self.entry_harga.delete(0, tk.END)
            except ValueError:
                messagebox.showwarning("Peringatan", "Harga harus berupa angka!")
        else:
            messagebox.showwarning("Peringatan", "Masukkan nama dan harga barang!")

    def hitung_total_harga(self):
        total_harga = sum(barang["harga"] for barang in self.data_barang)
        self.label_total_harga.config(text=f"Total Harga: {total_harga}")

    def cetak_struk(self):
        if not self.data_barang:
            messagebox.showwarning("Peringatan", "Tambahkan barang terlebih dahulu!")
            return

        struk = "===== Struk Pembelian =====\n"
        for barang in self.data_barang:
            struk += f"{barang['nama']}: {barang['harga']}\n"

        struk += "\nTotal Harga: " + str(sum(barang["harga"] for barang in self.data_barang))

        messagebox.showinfo("Struk Pembelian", struk)

if __name__ == "__main__":
    root = tk.Tk()
    aplikasi = AplikasiPOS(root)
    root.mainloop()