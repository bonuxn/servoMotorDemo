import wiringpi #GPIO制御ライブラリ
import time #タイマライブラリ
import sys


class Servo:

	def __init__(self,pin):
		self._pin = pin
	
	def 