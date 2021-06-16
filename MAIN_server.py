import socket, time, threading
#Firt one recevie second video
One_s_sec=socket.socket()
One_s_sec.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

#Firt one recevie third video
One_s_thr=socket.socket()
One_s_thr.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

#Second one recevie one's video
Sec_s_one=socket.socket()
Sec_s_one.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

#Second one recevie third's video
Sec_s_thr=socket.socket()
Sec_s_thr.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)


#Third one recevie second video
thr_s_sec=socket.socket()
thr_s_sec.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

#third one recevie one video
thr_s_one=socket.socket()
thr_s_one.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

#Firt one send connection
One_r=socket.socket()
One_r.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

#Second one send connection
Sec_r=socket.socket()
Sec_r.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)

#Third one send connection
thr_r=socket.socket()
thr_r.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR, 1)


One_r_port= 2024 #Port for one send func
Sec_r_port= 2025 #port for second send func
thr_r_port = 2026 #Port for third send func

One_s_sec_port= 2027 # port for one recevie func second video
One_s_thr_port = 2028 # port for one recevie func thr video

Sec_s_one_port= 2029 # port for second recevie func ones video
Sec_s_thr_port= 2030 # port for second recevie func third video

thr_s_one_port = 2031 # Port for third recevie func one video
thr_s_sec_port = 2032 # Port for third recevie func sec video



ip=""

#binding all send and recevie connection
#for first one
One_r.bind((ip, One_r_port))
print ("connecte this ip: {} with this port: {}".format(ip, One_r_port))
One_s_sec.bind((ip, One_s_sec_port))
print ("connecte this ip: {} with this port: {}".format(ip, One_s_sec_port ))
One_s_thr.bind((ip, One_s_thr_port))
print ("connecte this ip: {} with this port: {}".format(ip, One_s_thr_port ))

#for Second one
Sec_r.bind((ip, Sec_r_port))
print ("connecte this ip: {} with this port: {}".format(ip, Sec_r_port))
Sec_s_one.bind((ip, Sec_s_one_port))
print ("connecte this ip: {} with this port: {}".format(ip, Sec_s_one_port))
Sec_s_thr.bind((ip, Sec_s_thr_port))
print ("connecte this ip: {} with this port: {}".format(ip, Sec_s_thr_port))

#for Third one
thr_r.bind((ip, thr_r_port))
print ("connecte this ip: {} with this port: {}".format(ip,thr_r_port ))
thr_s_one.bind((ip, thr_s_one_port))
print ("connecte this ip: {} with this port: {}".format(ip,thr_s_one_port ))
thr_s_sec.bind((ip, thr_s_sec_port))
print ("connecte this ip: {} with this port: {}".format(ip, thr_s_sec_port))

One_r.listen()
One_s_sec.listen()
One_s_thr.listen()
Sec_r.listen()
Sec_s_one.listen()
Sec_s_thr.listen()
thr_r.listen()
thr_s_one.listen()
thr_s_sec.listen()


One_r_secsession, One_r_secaddr = One_r.accept()
One_s_sec_onesession, One_s_sec_oneaddr = One_s_sec.accept()
One_s_thr_secsession, One_s_thr_oneaddr = One_s_thr.accept()
Sec_r_session, Sec_r_oneaddr = Sec_r.accept()
Sec_s_one_secsession, Sec_s_one_oneaddr = Sec_s_one.accept()
Sec_s_thr_session, Sec_s_thr_oneaddr = Sec_s_thr.accept()
thr_r_session, thr_r_oneaddr = thr_r.accept()
thr_s_one_session, Sthr_s_one_oneaddr = thr_s_one.accept()
thr_s_sec_session, thr_s_sec_oneaddr = thr_s_sec.accept()
def One_rec():
    while True:
        data=One_r_secsession.recv(10000000)
        time.sleep(0.5)
        One_s_sec_onesession.send(data)
        One_s_thr_secsession.send(data)

def Sec_rec():
    while True:
        data=Sec_r_session.recv(10000000)
        time.sleep(0.5)
        Sec_s_one_secsession.send(data)
        Sec_s_thr_session.send(data)

def thr_rec():
    while True:
        data=thr_r_session.recv(10000000)
        time.sleep(0.5)
        thr_s_one_session.send(data)
        thr_s_sec_session.send(data)
  

One_main=threading.Thread(target=One_rec)
Sec_main=threading.Thread(target=Sec_rec)
Thr_main=threading.Thread(target=thr_rec)
One_main.start()
Sec_main.start()
Thr_main.start()