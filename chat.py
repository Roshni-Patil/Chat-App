import socket
import threading 
import os

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


ip = input("\n\t\tEnter Your IP : ")
port = int(input("\n\t\tEnter Port number : "))



s.bind( (ip,port) )

sip = input("\n\t\tEnter Receiver IP : ")
# sport = int(input("\n\t\tEnter Receiver Port : "))

print()
print("********************************************************************")
print("\t\t\t\t\t\t\t\tChat App")
print("********************************************************************")

def send():

    while True:
        msg=input("\n\t\t\t\t\t\t")
        # msg = input('\n\t\t\t\t\t\t\tYour message :')
        fmsg=msg.encode()
      
        
        s.sendto(fmsg,(sip,port))
        if fmsg.decode() == "exit":
            os._exit(1)
        
def recv():
    while True:
        # os.system('tput setaf 2')
        msg = s.recvfrom(1024)
        if msg[0].decode() == "exit":
            os._exit(1)
        
        print('\nReceived from '+ sip +" : " + msg[0].decode() + "\n\t\t\t\t\t\t" ,end="")
        # print("\n\t\t\t\t\t\t")
    



t1 = threading.Thread(target=send)
t2 = threading.Thread(target=recv)

t1.start()
t2.start()