from datetime import *

def diffDate(x):
	x = x.split('-')
	tanggal = date(int(x[0]),int(x[1]),int(x[2]))
	skrg = datetime.date(datetime.now())
	selisih = tanggal - skrg
	selisih = selisih.days
	print('Tanggal sekarang\t\t\t   :',skrg)
	print('Selisih\t\t\t\t\t   :', selisih, 'hari')
	return selisih

tgl = input('Masukkan Tanggal yang Diminta (YYYY-MM-DD) : ')
diffDate(tgl)
