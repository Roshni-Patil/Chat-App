import socket
import threading 
import os

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


ip = input("\n\t\tEnter Your IP : ")
port = int(input("\n\t\tEnter Port number : "))



s.bind( (ip,port) )

sip = input("\n\t\tEnter Receiver IP : ")



os.system("cls")
print("""\t***********************************************************************
\t*                                                                     *
\t*                              Chat App                               *
\t*                                                                     *
\t***********************************************************************
         
         """)
try:
    if recip != sip:
        sip = recip
        def send():
            while True:
                msg=input("\n\t\t\t\t\t\t\t")
                # msg = input("\n\t\t\t\t\t\t\tYour message :")
                if msg !=  " " :
                    fmsg=msg.encode()
            
                
                s.sendto(fmsg,(sip,port))
                if fmsg.decode() == "exit":
                    os._exit(1)

except NameError:
    def send():
            while True:
                msg=input("\n\t\t\t\t\t\t\t")
                # msg = input("\n\t\t\t\t\t\t\tYour message :")
                if msg !=  " " :
                    fmsg=msg.encode()
            
                
                s.sendto(fmsg,(sip,port))
                if fmsg.decode() == "exit":
                    os._exit(1)


def recv():
    while True:
        # os.system('tput setaf 2')
        msg = s.recvfrom(1024)
        recip=msg[1][0]
        if msg[0].decode() == "exit":
            os._exit(1)
        
        print('\nReceived from '+ recip +" : " + msg[0].decode() + "\n\t\t\t\t\t\t\t" ,end="")
        # sip = recip
        # print("\n\t\t\t\t\t\t")
    



t1 = threading.Thread(target=send)
t2 = threading.Thread(target=recv)

t1.start()
t2.start()