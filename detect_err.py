#from scapy.all import * 
#def check_err(dest_IP):
#    print(sniff(filter="tcp and src 192.168.29.143 and dest"+dest_IP, count=5))
# Implementing TCP SYN attack detection Using Scapy
# import modules

pktc1=0
pktc2=0

def pkt_count(pkt):
    global pktc1
    pktc1=pktc1+1
def pkt_count2(pkt):
    global pktc2
    pktc2=pktc2+1


def det_syn_atk(t,p):
    print("Detecting for TCP SYN Flood Attack....")
    if(abs(t-p)<=1):
        print("Information safe from TCP SYN Flood attackers!!")
    else:
        print("CAUTION!! TCP SYN Flood attacks detected. Kindly secure the network!!")
    




   
   
   