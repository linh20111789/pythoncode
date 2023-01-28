## nhập dữ liệu vào
from calendar import c
import math

print("Hãy nhập 1 đoạn dữ liệu bất kì")
ds = []
a = ''

dscacbien = ['x']
quyuocso = {
	'một': '1',
	'hai': '2',
	'ba': '3',
	'bốn': '4',
	'năm': '5',
	'sáu': '6',
	'bảy': '7',
	'tám': '8',
	'chín': '9',
	'mười': '10',
}


def bangquyuoc(a):
	if a.find('bằng không') != -1:
		a = a.replace('bằng không', '= 0')
	if a.find('bằng 0') != -1:
		a = a.replace('bằng 0', '= 0')
	if a.find('= không') != -1:
		a = a.replace('= không', '= 0')
	if a.find('cộng') != -1:
		a = a.replace('cộng', '+')
	if a.find('trừ') != -1:
		a = a.replace('trừ', '-')
	if a.find('bằng') != -1:
		a = a.replace('bằng', '=')
	for i in quyuocso.keys():
		if a.find(i) != -1:
			a = a.replace(i,quyuocso[i])
	return a


# hàm nhập vào để test xem a nhập vào có phải phương trình bậc nhất, bậc 2 hoặc là không phải.
def kiemtra():
	print("kiem tra")
	test = '0'  # không phải phương trình
	if a.find('= 0') != -1:
		if a.find('bình phương') != -1:
			test = '2'  # phương trình bậc 2
			print("phương trình bậc 2")
		else:
			kiemtra = False
			for i in dscacbien:
				if a.find(i) != -1:
					kiemtra = True
					break
			if kiemtra:
				test = '1'  # phương trình bậc nhất
				print("phương trình bậc 1")
	return test


def chuyendoi(a):
	try:
		so = int(a)
		return True
	except:
		return False


def Pt_bac1(a):
	a = a.replace(' ', '')
	phepcong = True
	if a.find('-') != -1:
		phepcong = False
	dsmau = a.split('=')
	right = dsmau[0]
	c = dsmau[0]
	if phepcong:
		m = right.split('+')
	else:
		m = right.split('-')
	for p in m:
		if p.find('x') != -1:
			e = p.replace('x', '')
		else:
			f = p
	if chuyendoi(c) and chuyendoi(e) and chuyendoi(f):
		c_int = int(c)
		e_int = int(e)
		f_int = int(f)
		if f_int != 0:
			if phepcong:
				y = (c_int - f_int) / e_int
			else:
				y = (c_int + f_int) / e_int
		else:
			n = c_int / e_int
	else:
		if phepcong:
			n = '({0} - {1})/{2}'.format(c, e, f)
		else:
			n = '({0} + {1})/{2}'.format(c, e, f)
	return y


def Pt_bac2(a):
	a = a.replace(' ', '')
	dsmau = a.split('=')
	right = dsmau[0]
	d = dsmau[1]
	m = right.split('+')
	m_2 = []
	for p in m:
		lst = p.split('-')
		list.extend(lst)
	for p in list:
		if p.find('x bình phương') != -1:
			e = p.replace('x bình phương', '')
		elif p.find('x') != -1:
			f = p.replace('x', '')
		else:
			c = p
	toan_cong = True
	if right.find('-') != -1:
		toan_cong = False
	toan_tru = True
	if right.find('+') != -1:
		toan_tru = False
	if chuyendoi(c) and chuyendoi(e) and chuyendoi(f) and chuyendoi(d):
		c_int = int(c)
		e_int = int(e)
		f_int = int(f)
		d_int = int(d)
		if toan_tru:
			f_int = 0 - f_int
			c_int = 0 - c_int
		if toan_tru is False and toan_cong is False:
			kq_cong = right.find('+')
			kq_tru = right.find('-')
			if kq_cong > kq_tru:
				f_int = 0 - f_int
			else:
				c_int = 0 - c_int
		if e_int == 0:
			if f_int == 0:
				print("Phương trình vô nghiệm!")
			else:
				print("Phương trình có một nghiệm: x = ", + (-c_int / f))
		else:
			delta = f_int * f_int - 4 * e_int * c_int
			# tính nghiệm
			if delta > 0:
				x1 = float((-f_int + math.sqrt(delta)) / (2 * e_int))
				x2 = float((-f_int - math.sqrt(delta)) / (2 * e_int))
				print("Phương trình có 2 nghiệm là: x1 = ", x1, " và x2 = ", x2)
			elif delta == 0:
				x1 = (-f_int / (2 * e_int))
				print("Phương trình có nghiệm kép: x1 = x2 = ", x1)
			else:
				print("Phương trình vô nghiệm!")

# câu 1
while a !='2':
	a = input()
	print('Bạn đã nhập đoạn text: ', a)
	ds.append(a)

for a in ds:
	a = bangquyuoc(a)
	print('a', a)
	test = kiemtra()
	# câu 1. start
	if test == '0':
		print("Câu bạn vừa nhập là câu thông thường không phải là chương trình")
	elif test == '1':
		print("Phương trình bậc một")
	elif test == '2':
		print("Phương trình bậc hai")

# câu 2
print("Câu 2: Mời bạn nhập phương trình bậc nhất: ")
a = input()
print('Bạn đã nhập đoạn text: ', a)
a = bangquyuoc(a)
print('Kết quả x: ', Pt_bac1(a))

#câu 3
print("Câu 3: Mời bạn nhập phương trình bậc hai: ")
a = input()
print('Bạn đã nhập đoạn text: ', a)
a = bangquyuoc(a)
Pt_bac2(a)

#câu 4
print("Câu 4: Mời bạn nhập phương trình: ")
a = input()
print('Bạn đã nhập đoạn text: ', a)
a = bangquyuoc(a)
test = kiemtra(a)
if test == '0':
	print("Không phải là phương trình")
elif test == '1':
	print('Kết quả x: ', Pt_bac1(a))
elif test == '2':
	Pt_bac2(a)