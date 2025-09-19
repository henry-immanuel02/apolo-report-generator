from functions import *
from untuk0100 import *
from variables import *
from untuk0200 import *
import pandas as pd

class Apolo():
    def __init__(self, data0100, data0200, periode_lapor = 20250731):
        self.data0100 = data0100
        self.data0200 = data0200
        self.period = periode_lapor

    def cek_0100(self):
        cols = ['Baris Include dalam File Teks?', 'Nomor Baris yang masuk ke file teks',
       'Single atau Multi Rows', 'Flag Detail', 'Kode Komponen / Baris',
       'Keterangan Akun', 'Nomor Polis', 'Nama Pemegang Polis', 'Jenis Polis',
       'Tanggal Mulai Polis', 'Tanggal Berakhir Polis', 'NIK/NPWP',
       'Tanggal Lahir Pemegang Polis', 'Jenis Kelamin', 'Lokasi', 'Lini Usaha',
       'Cara Bayar', 'Jumlah Premi', 'Uang Pertanggungan', 'Cadangan Premi',
       'CAPYBMP', 'Jumlah Tertanggung']
        for i in cols:
            try:
                self.data0100[i]
            except:
                raise ValueError(f'Kolom {i} tidak ditemukan!')

    def proses_0100(self):
        self.data0100['Jenis Polis'] = self.data0100.apply(lambda x: cek_jenis_polis(x['Jenis Polis']), axis = 1)
        self.data0100['Nomor Polis'] = self.data0100.apply(lambda x: cek_nomor_polis(x['Nomor Polis'], x['Jenis Polis']), axis = 1)
        self.data0100['Nama Pemegang Polis'] = self.data0100.apply(lambda x: cek_nama(x['Nama Pemegang Polis'], x['Jenis Polis']), axis = 1)
        self.data0100['Tanggal Mulai Polis'] = self.data0100.apply(lambda x: cek_mulai_polis(x['Tanggal Mulai Polis'], self.period), axis = 1)
        self.data0100['Tanggal Berakhir Polis'] = self.data0100.apply(lambda x: cek_akhir_polis(x['Tanggal Berakhir Polis'], self.period), axis = 1)
        self.data0100['NIK/NPWP'] = self.data0100.apply(lambda x: cek_nik_npwp(x['NIK/NPWP']), axis = 1)
        self.data0100['Tanggal Lahir Pemegang Polis'] = self.data0100.apply(lambda x: cek_tanggal_lahir(x['Tanggal Lahir Pemegang Polis'], x['Jenis Polis']), axis = 1)
        self.data0100['Jenis Kelamin'] = self.data0100.apply(lambda x: cek_jenis_kelamin(x['Jenis Kelamin'], x['Jenis Polis']), axis = 1)
        self.data0100['Lokasi'] = self.data0100.apply(lambda x: cek_lokasi(x['Lokasi'], x['Jenis Polis']), axis = 1)
        self.data0100['Lini Usaha'] = self.data0100.apply(lambda x: cek_lini(x['Lini Usaha'], x['Jenis Polis']), axis = 1)
        self.data0100['Cara Bayar'] = self.data0100.apply(lambda x: cek_cara_bayar(x['Cara Bayar'], x['Jenis Polis']), axis = 1)
        self.data0100['Jumlah Premi'] = self.data0100.apply(lambda x: cek_jumlah_premi(x['Jumlah Premi'], x['Jenis Polis']), axis = 1)
        self.data0100['Uang Pertanggungan'] = self.data0100.apply(lambda x: cek_uang_pertanggungan(x['Uang Pertanggungan'], x['Jenis Polis']), axis = 1)
        self.data0100['Cadangan Premi'] = self.data0100.apply(lambda x: cek_cadangan(x['Cadangan Premi'], x['Jenis Polis']), axis = 1)
        self.data0100['CAPYBMP'] = self.data0100.apply(lambda x: cek_capybmp(x['CAPYBMP'], x['Jenis Polis']), axis = 1)
        self.data0100['Jumlah Tertanggung'] = self.data0100.apply(lambda x: cek_jumlah_tertanggung(x['Jumlah Tertanggung'], x['Jenis Polis']), axis = 1)

    def generate_0100(self):
        self.cek_0100()
        self.proses_0100()
        self.data0100['Awal'] = 'D01'
        self.data0100['Jumlah Premi1'] = self.data0100['Jumlah Premi'].apply(int)
        self.data0100['Uang Pertanggungan1'] = self.data0100['Uang Pertanggungan'].apply(int)
        self.data0100['Cadangan Premi1'] = self.data0100['Cadangan Premi'].apply(int)
        self.data0100['CAPYBMP1'] = self.data0100['CAPYBMP'].apply(int)
        self.data0100['Jumlah Tertanggung1'] = self.data0100['Jumlah Tertanggung'].apply(int)

        self.res0100 = self.data0100[['Awal', 'Kode Komponen / Baris', 'Nomor Polis' , 'Nama Pemegang Polis', 'Jenis Polis', 
                                    'Tanggal Mulai Polis', 'Tanggal Berakhir Polis', 'NIK/NPWP',
                                    'Tanggal Lahir Pemegang Polis', 'Jenis Kelamin', 'Lokasi', 'Lini Usaha',
                                    'Cara Bayar', 'Jumlah Premi', 'Uang Pertanggungan', 'Cadangan Premi',
                                    'CAPYBMP', 'Jumlah Tertanggung']]
        self.res0100['Kode Komponen / Baris'] = '0010010000'

        result = self.data0100[['Nomor Polis', 'Nama Pemegang Polis']].drop_duplicates()
        self.names = dict(zip(result['Nomor Polis'], result['Nama Pemegang Polis']))
        result = self.data0100[['Nomor Polis', 'NIK/NPWP']].drop_duplicates()
        self.nik = dict(zip(result['Nomor Polis'], result['NIK/NPWP']))

        header_line = f"H01|031202|2000003822|{str(self.period)[0:4]}-{str(self.period)[4:6]}-{str(self.period)[6:]}|PLSASRUK|0100|0|"
        footer_line = f"D01|0010020000||||||||||||{self.data0100['Jumlah Premi1'].sum()}|{self.data0100['Uang Pertanggungan1'].sum()}|{self.data0100['Cadangan Premi1'].sum()}|{self.data0100['CAPYBMP1'].sum()}|{self.data0100['Jumlah Tertanggung1'].sum()}"

        # konversi dataframe jadi string pakai to_csv (tanpa header & index)
        body = self.res0100.to_csv(sep="|", index=False, header=False, lineterminator="\r\n")

        # gabung semua bagian jadi satu string
        content = header_line + "\r\n" + body + footer_line + "\r\n"
        return content


    def cek0200(self):
        cols = ['Baris Include dalam File Teks?', 'Nomor Baris yang masuk ke file teks',
       'Single atau Multi Rows', 'Flag Detail', 'Kode Komponen / Baris',
       'Keterangan Akun', 'Status Pertanggungan', 'Nomor Polis',
       'Nama Pemegang Polis', 'NIK/NPWP', 'Lini Usaha', 'Jenis Klaim',
       'Nilai Klaim']
        for i in cols:
            try:
                self.data0200[i]
            except:
                raise ValueError(f'Kolom {i} tidak ditemukan!')

    def proses0200(self):
        self.data0200['Status Pertanggungan'] = self.data0200['Status Pertanggungan'].apply(cek_status2)
        self.data0200['Nama Pemegang Polis'] = self.data0200.apply(lambda x: ambil_nama(x['Nomor Polis'], self.names), axis = 1)
        self.data0200['NIK/NPWP'] = self.data0200.apply(lambda x: ambil_nik(x['Nomor Polis'], self.nik), axis = 1)
        self.data0200['Lini Usaha'] = self.data0200['Lini Usaha'].apply(atur_lini_usaha)
        self.data0200['Jenis Klaim'] = self.data0200.apply(lambda x: atur_jenis_klaim(x['Jenis Klaim'], x['Status Pertanggungan']), axis = 1)
        self.data0200['Nilai Klaim'] = pd.to_numeric(
            self.data0200['Nilai Klaim'], errors='coerce'
        ).fillna(0).astype(int)

        self.data0200['Nilai Klaim'] = self.data0200.apply(
            lambda row: '' if atur_nilai_klaim(row['Nilai Klaim'], row['Status Pertanggungan']) == 0
                        else str(atur_nilai_klaim(row['Nilai Klaim'], row['Status Pertanggungan'])),
            axis=1
        )

        self.total_klaim = int(pd.to_numeric(self.data0200['Nilai Klaim'], errors='coerce').fillna(0).sum())
       
    def generate_0200(self):
        # Jalankan proses
        self.cek0200()
        self.proses0200()

        # Tambahkan kolom awal
        self.data0200['Awal'] = 'D01'

        # Pilih kolom sesuai format
        self.res0200 = self.data0200[
            [
                'Awal', 'Kode Komponen / Baris', 'Status Pertanggungan',
                'Nomor Polis', 'Nama Pemegang Polis', 'NIK/NPWP',
                'Lini Usaha', 'Jenis Klaim', 'Nilai Klaim'
            ]
        ]

        # Header & footer
        header_line = (
            f"H01|031202|2000003822|"
            f"{str(self.period)[0:4]}-{str(self.period)[4:6]}-{str(self.period)[6:]}|"
            f"PLSASRUK|0200|0|"
        )
        footer_line = f"D01|0020020000|||||||{self.total_klaim}"

        # Konversi dataframe jadi text (tanpa index, tanpa header)
        body = self.res0200.to_csv(sep="|", index=False, header=False, lineterminator="\r\n")

        # Gabungkan semua ke satu string
        content = header_line + "\r\n" + body + footer_line + "\r\n"

        return content

