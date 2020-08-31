from time import sleep

s = 0
m = 0
h = 0

while s <= 59:
	s += 1
	#print('s ', s)
	if s == 60:
		s = 0
		m += 1
		print('m', m)
		if m == 60:
			m = 0
			h += 1
			print('h ', h)
			if h == 24:
				h = 0
				sleep(0.0000000001)