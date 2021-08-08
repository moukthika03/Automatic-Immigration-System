import socket 
import threading
import detect_err
import tes3
import facial_rec
from scapy.all import*
import imagecrp

HEADER = 1024
PORT = 12345
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

passenger_det=[]

def handle_client(conn, addr):
    #print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                connected = False
                t.stop()
                p.stop()
                print(detect_err.pktc1)
                print(detect_err.pktc2)
                detect_err.det_syn_atk(detect_err.pktc1,detect_err.pktc2)
            else:
                print("Details recieved.")
                print(msg)
                passenger_det.append(msg)
                if msg[:11]=="Immigration":
                    similarity=facial_rec.check_sim(passenger_det[0],msg)
                    conn.send(similarity.encode(FORMAT))
                elif "Passport_sample" in msg:
                    passenger_det.append(imagecrp.crop_img(msg))
                #tes3.extract_info(msg)
            
            #print(f"[{addr}] {msg}")
            #conn.send("Please get ready for your photo:-".encode(FORMAT))
            #msg2 = conn.recv(HEADER).decode(FORMAT)
            #print(msg2)


    conn.close()
        

def start_ser():
    server.listen()
    print(f"Passenger scanning passport:-")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))

        thread.start()
       # print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
    

print("Welcome! Serving the next passenger....")
t=AsyncSniffer(prn=detect_err.pkt_count,store=False, filter="((tcp[tcpflags] & (tcp-syn|tcp-ack|tcp-push) == tcp-syn) and (tcp[tcpflags] & (tcp-syn|tcp-ack|tcp-push) != tcp-ack)) and dst port "+str(PORT)+" or src port "+str(PORT),iface="lo0")
p=AsyncSniffer(prn=detect_err.pkt_count2,store=False, filter="((tcp[tcpflags] & (tcp-syn|tcp-ack|tcp-push) == tcp-syn) and (tcp[tcpflags] & (tcp-syn|tcp-ack|tcp-push) == tcp-ack)) and dst port "+str(PORT)+" or src port "+str(PORT),iface="lo0")

t.start()
p.start()
start_ser()
 


