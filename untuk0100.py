from variables_1 import *

def cek_nomor_polis(x, jenis_pertanggungan):
    if 100 <= int(jenis_pertanggungan) <= 400:
        x = str(x)
        allow = '1234567890abcdefghijklmnopqrstuvwxyz/-\',\"()*.'
        res = ''
        for i in x:
            if i.lower() in allow:
                res += i
            else:
                pass
        if len(res) > 50:
            return res[:50]
        return res
    else:
        return ''
    


def cek_nama(x, jenis_pertanggungan):
    if 100 <= int(jenis_pertanggungan) <= 400:
        x = str(x)
        allow = '1234567890abcdefghijklmnopqrstuvwxyz .,\''
        res = ''
        for i in x:
            if i.lower() in allow:
                res += i
            else:
                pass
        if len(res) > 255:
            return res[:255]
        else:
            return res
    else:
        return ''

def cek_nama(x, jenis_pertanggungan):
    if 100 <= int(jenis_pertanggungan) <= 400:
        x = str(x)
        allow = '1234567890abcdefghijklmnopqrstuvwxyz .,\''
        res = ''
        for i in x:
            if i.lower() in allow:
                res += i
            else:
                pass
        if len(res) > 255:
            return res[:255]
        else:
            return res
    else:
        return ''


def cek_jenis_polis(x):
    allow = [i*100 for i in range(1, 6)]
    if int(x) in allow:
        return x
    else:
        return '100'

def cek_mulai_polis(x, periode_lapor=20250731):
    if int(x) > int(periode_lapor):
        return #hapus
    else:
        return x

def cek_akhir_polis(x, periode_lapor=20250731):
    return x

def cek_nik_npwp(x):
    allow = '1234567890abcdefghijklmnopqrstuvwxyz'
    x = str(x).lower()   # biar konsisten huruf kecil
    res = ''.join([c for c in x if c in allow])

    # potong maksimal 22
    if len(res) > 22:
        res = res[:22]

    # cek jumlah karakter unik
    unique = []
    for c in res:
        if c not in unique:
            unique.append(c)

    # cek apakah ada karakter sama berurutan
    def has_consecutive_repeat(s):
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return True
        return False

    if len(unique) <= 2 or len(res) <= 14 or len(res) > 16 or has_consecutive_repeat(res):
        return '123456782345678'
    else:
        return res


def cek_tanggal_lahir(x, jenis_pertanggungan):
    try:
        jp = int(float(jenis_pertanggungan))
    except:
        return ''
    
    if jp in [200, 400]:
        try:
            if int(x) < 19000101 or int(x) > 21000101:
                return '19000101'
            else:
                return str(x)
        except:
            return '19000101'
    else:
        return ''

def cek_jenis_kelamin(x, jenis_pertanggungan):
    x = str(x)
    if str(jenis_pertanggungan) == '200' or str(jenis_pertanggungan) == '400':
        if not(x.upper() == 'L' or x.upper() == 'P'):
            return 'L'
        else:
            return x.upper()
    else:
        return ''


def cek_lokasi(x, jenis_pertanggungan):
    global lokasi
    allow = lokasi
    if 100 <= int(jenis_pertanggungan) <= 400:
        x = str(x)
        if not(x in allow) or len(x) != 4:
            return '3171'
        else:
            return x
    else:
        return ''


def cek_lini(x, jenis_pertanggungan):
    global lini
    if int(jenis_pertanggungan) != 500:
        if not(int(x) in lini):
            return '501'
        else:
            return str(x)
    else:
        return ''
    

def cek_cara_bayar(x, jenis_pertanggungan):
    global cara_bayar
    if int(jenis_pertanggungan) != 500:
        if not(int(x) in cara_bayar):
            return '200'
        else:
            return str(x)
    else:
        return ''
    

def cek_jumlah_premi(x, jenis_pertanggungan):
    if int(jenis_pertanggungan) != 500:
        return str(int(float(x)))
    else:
        return ''
    

def cek_uang_pertanggungan(x, jenis_pertanggungan):
    if int(jenis_pertanggungan) != 500:
        x = int(float(x))
        if x < 0:
            return '0'
        elif x > (10**20) - 1:
            return '0'
        else:
            return str(int(x))
    else:
        return ''
    

def cek_cadangan(x, jenis_pertanggungan):
    if int(jenis_pertanggungan) != 500:
        x = int(float(x))
        if x < 0:
            return '0'
        elif x > (10**20) - 1:
            return '0'
        else:
            return str(int(x))
    else:
        return ''
    

def cek_cadangan(x, jenis_pertanggungan):
    if int(jenis_pertanggungan) != 500:
        x = int(float(x))
        if x < 0:
            return '0'
        elif x > (10**20) - 1:
            return '0'
        else:
            return str(int(x))
    else:
        return ''
    

def cek_capybmp(x, jenis_pertanggungan):
    if int(jenis_pertanggungan) != 500:
        x = int(float(x))
        if x < 0:
            return '0'
        elif x > (10**20) - 1:
            return '0'
        else:
            return str(int(x))
    else:
        return ''
    

def cek_jumlah_tertanggung(x, jenis_pertanggungan):
    if int(jenis_pertanggungan) != 500:
        if int(jenis_pertanggungan) == 200 or int(jenis_pertanggungan) == 300:
            return '1'
        else:
            return str(min(max(int(x), 2), 10**10 - 1))
    else:
        return ''
    

