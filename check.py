from scapy.all import *
import os
import binascii

#targeting folder and file pcap 
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'CtrlCapture.pcap')

#reading file pcap save as variabel pcap_data
pcap_data=rdpcap(my_file)

"""
print(pcap_data[17].payload)
print("--")
print(binascii.hexlify(bytes(pcap_data[17].payload)))
print(pcap_data[17].load)
pcap_data[17].show()
"""

val = str("123+22")
pcap_data[17].load = val.encode()
pcap_data[17][IP].src = "100.6.0.21"
pcap_data[17][IP].dst = "100.6.0.11"
pcap_data[17][TCP].dport = 992
pcap_data[17][IP].len = 57

sendp(pcap_data[17])




