import socket
import imagecap
import tes3
import gui_app
import time


HEADER = 1024
PORT = 12345
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
#SERVER = socket.gethostbyname(socket.gethostname())
SERVER = '127.0.0.1'
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    #print(client.recv(2048).decode(FORMAT))

# def search():
#     global img
#     img = filedialog.askopenfilename(parent=root, initialdir="/", title='Please select a file')
#     if len(img) > 0:
#         browseBox.delete(0,END)
#         browseBox.insert(0,img)
    
gui_app.gui_client()
print('Welcome to auto immigration!! Please scan your passport:-')
#img= 'Passport_sample_2.png'
send(gui_app.img)
extimg=tes3.extract_info(gui_app.img)
#print(extimg)
send(extimg)

time.sleep(5) # Sleep for 3 seconds
print("Please get ready for your photo:-")
fn=imagecap.captureimg()
#print(fn)
send(fn)
print(client.recv(2048).decode(FORMAT))

msg2="!DISCONNECT"
send(msg2)

