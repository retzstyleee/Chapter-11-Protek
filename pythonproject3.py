from datetime import *

def diffDate(x,y):
    x = x.split('-')
    y = data[extract+4].split('-')
    tgl= date(int(x[0]),int(x[1]),int(x[2]))
    tgl1= date(int(y[0]),int(y[1]),int(y[2]))
    result = tgl - tgl1
    result = result.days
    return result

def cariKode(source, kodex):
	myfile = open(source, 'r')
	isi = myfile.read()
	global data
	data = isi.replace('\n', '|')
	data = data.split('|')
	try:
		global extract
		extract = data.index(kodex)
		if kodex in data:
			print('='*50)
			print('Data Peminjam Buku')
			print('Kode member\t\t\t:', data[extract])
			print('Nama member\t\t\t:', data[extract + 1])
			print('Judul Buku\t\t\t:', data[extract + 2])
			print('Tanggal mulai peninjaman\t:', data[extract + 3])
			print('Tanggal Maks peninjaman\t\t:', data[extract + 4])
			mulai = data[extract + 3]
			kembali = input('Masukkan Tanggal Pengembalian\t: ')
			date = diffDate(kembali, mulai)
			if date >= 0:
				print('Terlambat\t\t\t:',date,'hari')
				denda = int(date)*2000
				print('Denda\t\t\t\t: Rp.',denda)
	except ValueError:
			print('Data tidak ditemukan')

print('='*50)
print('')
source = input('Masukkan nama file\t\t: ')
while True:
	kodex = input('Masukkan kode pinjam\t\t: ').upper()
	data = cariKode(source, kodex)
	ulangi = input('Ulangi lagi? (y/n) ')
	ulangi.lower()
	if ulangi == 'y':
		continue
	elif ulangi == 'n':
		break
	else:
		print('Input tidak valid')
		continue