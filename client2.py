import cv2
import pickle
import struct
import imutils
import socket
import base64
import os
import time
import threading
import pyshine as ps


ip="65.2.143.184"


def videoReciever():
    try:
        s=socket.socket()
        port=2031
        s.connect((ip,port))
        data = b""
        payload_size = struct.calcsize("Q")
        while True:
            print("vr")
            while len(data) < payload_size:
                packet = s.recv(4*1024) # 4K
                if not packet: break
                data+=packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            print("data",data)
            msg_size = struct.unpack("Q",packed_msg_size)[0]
            
            while len(data) < msg_size:
                data += s.recv(4*1024)
            frame_data = data[:msg_size]
            data  = data[msg_size:]
            frame = pickle.loads(frame_data)
            text  =  f"Shubham"
            frame =  ps.putBText(frame,text,10,10,vspace=10,hspace=1,font_scale=0.7, background_RGB=(255,0,0),text_RGB=(255,250,250))
            cv2.imshow(f"FROM Shubham",frame)
           # time.sleep(1)
            key = cv2.waitKey(200) & 0xFF
            if key  == ord('q'):
                break
        s.close()
    except:
        print('error')
        
def videoReciever1():
    try:
        s=socket.socket()
        port=2032
        s.connect((ip,port))
        data = b""
        payload_size = struct.calcsize("Q")
        while True:
            print("vr")
            while len(data) < payload_size:
                packet = s.recv(4*1024) # 4K
                if not packet: break
                data+=packet
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            print("data",data)
            msg_size = struct.unpack("Q",packed_msg_size)[0]
            
            while len(data) < msg_size:
                data += s.recv(4*1024)
            frame_data = data[:msg_size]
            data  = data[msg_size:]
            frame = pickle.loads(frame_data)
            text  =  f"Shubham"
            frame =  ps.putBText(frame,text,10,10,vspace=10,hspace=1,font_scale=0.7, background_RGB=(255,0,0),text_RGB=(255,250,250))
            cv2.imshow(f"FROM Shubham",frame)
           # time.sleep(1)
            key = cv2.waitKey(200) & 0xFF
            if key  == ord('q'):
                break
        s.close()
    except:
        print('error')



def videosender():
    #sending video
    s=socket.socket()
    
    port=2024
    s.connect((ip,port))

    if s: 
        vid = cv2.VideoCapture(0) 
        while (vid.isOpened()):
            print("vs")
            try:
                img, frame = vid.read()
                frame = imutils.resize(frame,width=380)
                a = pickle.dumps(frame)
                message = struct.pack("Q",len(a))+a
                s.sendall(message)
                cv2.imshow(f"TO: {ip}",frame)
                #time.sleep(1)
                key = cv2.waitKey(200) & 0xFF
                if key == ord("q"):
                    s.close()
            except:
                print('VIDEO FINISHED!')
                break

t_recv=threading.Thread(target=videoReciever)
t_recv1=threading.Thread(target=videoReciever1)
t_send=threading.Thread(target=videosender)
t_send.start()
t_recv.start()
t_recv1.start()
