import calcsha256
import socket

def netcat(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    data = str(s.recv(1024))
    print(data)
    stringstart = data.split(" ")[6]
    print(type(stringstart))
    ans = calcsha256.shaSoln(stringstart)
    print(ans)
    
    s.sendall(ans)
    print("done send")
    data = s.recv(1024)
    
    
    
    print(data)
    s.close()

netcat("fastrology.chal.pwni.ng", 1337)
