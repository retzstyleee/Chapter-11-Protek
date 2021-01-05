from datetime import *

def pinjamBuku(soure,kode,nama,judul):
	file = open(source, 'a')
	waktu = datetime.date(datetime.now())
	waktuKembali = waktu + timedelta(days=7)
	inputList = [kode,nama,judul,str(waktu),str(waktuKembali)]
	file.write('|'.join(inputList)+'\n')
	file.close()


source = input('Masukkan nama file\t\t: ')
while True:
	kode = input('Masukkan kode member\t\t: ').upper()
	nama = input('Masukkan nama member\t\t: ')
	judul = input('Masukkan judul buku\t\t: ')
	pinjamBuku(source,kode,nama,judul)
	menu = input('Ulangi lagi? (y/n) ')
	menu.lower()
	if menu == 'y':
		continue
	elif menu == 'n':
		break
	else:
		print('Input tidak valid')
		continue