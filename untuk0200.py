from variables import *

def cek_status2(x):
    try:
        x = int(x)
    except:
        return '100'
    if str(x) in ['100', '200']:
        return str(x)
    else:
        return '100'


def ambil_nama(x, y):
    return y[x]


def ambil_nik(x, y):
    return y[x]


def atur_lini_usaha(x):
    try:
        int(x)
    except:
        return '501'
    if int(x) in [i for i in range(501, 522)]:
        return str(x)
    else:
        return '501'
    

def atur_jenis_klaim(x, status_pertanggungan):
    try:
        if str(status_pertanggungan) == '200':
            if int(x) in [i*100 for i in range(4, 9)]:
                return str(int(x))
            else:
                return '600'
        else:
            return ''
    except:
        return '600'
    

def atur_nilai_klaim(x, status_pertanggungan):
    if int(status_pertanggungan) == 100:
        return 0
    else:
        if int(status_pertanggungan) == 200:
            try:
                if abs(int(x)) == 0:
                    return -1
                else:
                    return int(x)
            except:
                return -1
        else:
            return -1

        
