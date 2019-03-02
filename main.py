#!/usr/bin/python

import moduli


inputs = (
	0b00111000,
	0b01110110,
	0b00111100,
	210435464482,
	432892345,
	323452532130,
	323452532131,
	323452532132,
	323452532133,
	323452532134,
	323452532135,
	323452532136,
	323452532137,
	323452532138,
	323452532139,
	323452532140,
	0x0fffffffffffffffffffffffffffff,
	0x10fffffffffffffffffff123ffffffffff321,
	13234214044,
	14323452532132,
	101,
	102,
	103,
	104,
	105,
	106,
	107,
	108,
	109,
	110,
	111,
	112,
	113,
	114,
	115,
	116,
	117,
	118,
	119,
	120,
	121,
	122,
	123,
	124,
	125,
	126,
	127,
	128,
	129,
	130,
	131,
	132,
	133,
	134,
	135,
	136,
	137,
	138,
	139,
)

divisors = (
	2, 3, 4, 5, 6, 7, 8, 9,
	10, 11, 12, 13, 14, 15, 16, 17,
	24, 28, 
	30, 31, 32, 33,
	48,
	56,
	60, 62, 63, 64, 65,
)

for divisor in divisors:
	func = getattr(moduli, 'mod'+str(divisor))
	for inp in inputs:
		a = inp % divisor
		b = func(inp)
		print("divisor="+str(divisor))
		print(a)
		print(b)
		assert a == b

