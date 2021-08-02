from geometri.bangun_ruang import BangunRuang


class PersegiPanjang(BangunRuang):
    def __init__(self, p, l):
        # fungsi yang dipanggil pertamakali
        self.p = p
        self.l = l

    def info(self):
        return (f'modul menghitung rumus-rumus tentang persegipanjang dengan panjang={self.p}, lebar={self.l}')

    def hitung_luas(self):
        return self.p * self.l
