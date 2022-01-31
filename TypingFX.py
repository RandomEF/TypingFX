import time, sys, os

length = 0.01

def typeSpeed(speed):
    length = speed

def clearScreen():
	os.system("clear")

def tPrint(text):
	print()
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(length)

def tInput(text):
	print()
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(length)
	value = input()
	return value

def tIntInput(text):
	print()
	for char in text:
		sys.stdout.write(char)
		sys.stdout.flush()
		time.sleep(length)
	value = int(input())
	return value