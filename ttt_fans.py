import bluetooth
import time
import sys
import urllib2
from datetime import datetime


bd_addr = "98:D3:32:30:80:B2"  # here need to modify. use hciconfig to get address
port = 1

sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))
print ('Connected')
#sock.settimeout(1.0)	

def is_ascii(s):
	return all(ord(c)<128 for c in s)

def func1():
	sock.send('1')
def func2():
	sock.send('2')
def func3():
	sock.send('3')
def func4():
	sock.send('4')
def func5():
	sock.send('5')
def func6():
	print('sec?')
	sec = raw_input()
	time.sleep( float(sec)*60 )
	sock.send('1')
def defalutfunc():
	print ('default')

options ={
    '1': func1,
    '2': func2,
    '3': func3,
    '4': func4,
    '5': func5,
    '6': func6,
    'default':defalutfunc
    }

print ('1. On/Off')
print ('2. Fan Speen')
print ('3. Set Time')
print ('4. Swing L/R')
print ('5. Swing U/D')
print ('6. Set time (sec')
while 1:
	tosend = raw_input()
	if tosend != 'q':
		result = options.get(tosend, options.get('default'))()
	else:
		print('quit !')
		break;
	#################################
	
	while(1):
		data = sock.recv(1)
		if is_ascii(data):
			
			print(data)
			break
	
	


