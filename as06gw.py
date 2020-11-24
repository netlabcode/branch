import binascii
import _thread
import time
import socket
import psycopg2


HOST1 = '100.6.0.11'
PORT1 = 993
PORT2 = 994
PORTS1 = 881
PORTS2 = 883

# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST1, PORT1))
		
		x = 1
		while x < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = str(data1.decode("utf-8"))

			a,b,c,d,e,f,g = strval1.split("+")

			print(a)



# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )

except:
   print ("Error: unable to start thread")

while 1:
   pass
