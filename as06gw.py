import binascii
import _thread
import time
import socket


HOST1 = '100.6.0.11'
PORT1 = 993
PORT2 = 994
PORTS1 = 881
PORTS2 = 883

# Define a function for the thread
def serverOne():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sc1:
		sc1.connect((HOST1, PORT1))
		
		a = 1
		while a < 6:
			#recive data from server A
			data1 = sc1.recv(1024)

			strval1 = "mu01+"+str(data1.decode("utf-8"))

			print(strval1)



# Create two threads as follows
try:
   _thread.start_new_thread( serverOne, ( ) )

except:
   print ("Error: unable to start thread")

while 1:
   pass
