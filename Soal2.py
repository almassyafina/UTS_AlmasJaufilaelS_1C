tahun = int(input('Masukan Tahun : '))

satu = (tahun/400)
dua = (tahun/4/100)



kabisat = (satu==dua)

if kabisat==True:
    print (f'Tahun {tahun} merupakan TAHUN KABISAT')