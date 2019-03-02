#!/usr/bin/python

def mod2(number):
	return number & 0x1

def mod3(number):
	number = mod15(number)
	number = (number & 0x3) + (number >> 2) 
	if number > 2:
		number -= 3
	return number

def mod4(number):
	return number & 0x3

def mod5(number):
	while number > 0xf:
		number = (number >> 4) + (number & 0xf)
	number = (number & 0x3) - (number >> 2)
	if number < 0:
		number += 5
	return number

def mod6(number):
	while number > 7:
		number = (number >> 3 << 1) + (number & 0x7)
	if number > 5:
		number -= 6 
	return number

def mod7(number):
	while number > 7:
		number = (number >> 3) + (number & 0x7)
	if number == 7:
		number = 0 
	return number

def mod8(number):
	return number & 0x7

def mod9(number):
	while number > 0x3f:
		number = (number >> 6) + (number & 0x3f)
	number = (number & 0x7) - (number >> 3)
	if number < 0:
		number += 9
	return number

def mod10(number):
	number = mod30(number)
	while number > 9:
		number -= 10 
	return number

def mod11(number):
	number = mod33(number)
	while number > 10:
		number -= 11
	return number

def mod12(number):
	while number > 15:
		number = (number >> 4 << 2) + (number & 0xf)
	if number > 11:
		number -= 12
	return number

def mod13(number):
	number = mod65(number)
	while number > 12:
		number -= 13
	return number

def mod14(number):
	while number > 15:
		number = (number >> 4 << 1) + (number & 0xf)
	if number > 13:
		number -= 14
	return number

def mod15(number):
	while number > 15:
		number = (number >> 4) + (number & 0xf)
	if number == 15:
		number = 0
	return number

def mod16(number):
	return number & 0xf

def mod17(number):
	while number > 255:
		number = (number >> 8) + (number & 0xff)
	number = (number & 0xf) - (number >> 4)
	if number < 0:
		number += 17
	return number

def mod24(number):
	while number > 31:
		number = (number >> 5 << 3) + (number & 0x1f)
	if number > 23:
		number -= 24
	return number

def mod28(number):
	while number > 31:
		number = (number >> 5 << 2) + (number & 0x1f)
	if number > 27:
		number -= 28
	return number

def mod29(number):
	while number > 31:
		number = (number >> 5 << 2) + (number & 0x1f)
	if number > 27:
		number -= 28
	return number

def mod30(number):
	while number > 31:
		number = (number >> 5 << 1) + (number & 0x1f)
	if number > 29:
		number -= 30
	return number

def mod31(number):
	while number > 31:
		number = (number >> 5) + (number & 0x1f)
	if number == 31:
		number = 0
	return number

def mod32(number):
	return number & 0x1f

def mod33(number):
	while number > 0x3ff:
		number = (number >> 10) + (number & 0x3ff)
	number = (number & 0x1f) - (number >> 5)
	if number < 0:
		number += 33
	return number

def mod48(number):
	while number > 0x3f:
		number = (number >> 6 << 4) + (number & 0x3f)
		'''
		letter = number & 0x3f
		number = letter + ((number ^ letter) >> 2)
		'''
	if number > 47:
		number -= 48 
	return number

def mod56(number):
	while number > 0x3f:
		number = (number >> 6 << 3) + (number & 0x3f)
	if number > 55:
		number -= 56 
	return number

def mod60(number):
	while number > 0x3f:
		number = (number >> 6 << 2) + (number & 0x3f)
	if number > 59:
		number -= 60 
	return number

def mod62(number):
	while number > 0x3f:
		number = (number >> 6 << 1) + (number & 0x3f)
	if number > 61:
		number -= 62 
	return number

def mod63(number):
	while number > 63:
		number = (number >> 6) + (number & 0x3f)
	if number == 63:
		number = 0
	return number

def mod64(number):
	return number & 0x3f

def mod65(number):
	while number > 0xfff:
		number = (number >> 12) + (number & 0xfff)
	number = (number & 0x3f) - (number >> 6)
	if number < 0:
		number += 65
	return number

