from socket import *
import threading
from pathlib import Path
basedir = 'web'

def handlereq(cs):
    req = cs.recv(1024) # 
    m, l, p = parsereq(req.decode()) #parse based on method location and protocol
    resp = flfile(l)   #generate resposne by finding and loading file
    cs.sendall(resp)  # send the response and close the socket
    cs.close()

#parse the request
def parsereq(r):
    rr = r.split('\r\n')[0]
    return rr.split(' ')

#find and load the file
def flfile(l):
    p = Path(f'{basedir}/{l}')

    if p.is_file():
        return genokreq(p)

    elif p.is_dir():
        if (p / 'index.html').is_file():
            return genokreq(p / 'index.html')
        else:
            return gen404()
    else: 
        return gen404()

#generate ok response
def genokreq(fo):
    resp = 'HTTP/1.1 200 OK \r\n'
    if fo.suffix == '.html':
        resp += 'Content-Type: text/html\r\n'
        data = open(fo, 'r').read().encode()

    elif fo.suffix == '.png':
        resp += 'Content-Type: image/png\r\n'
        data = open(fo, 'br').read()

    else:
        resp += 'Content-Type: application/octet-stream\r\n'
        data = open(fo, 'br').read()
    resp += f'Content length {len(data)}\r\n'
    resp += '\r\n'

    resp = resp.encode()
    resp += data
    resp += '\r\n\r\n'.encode()

    return resp
    
#generate error
def gen404():
    pass

with socket() as s:
    s.bind(('', 8888))
    s.listen()
    

    while True:
        conn, addr = s.accept()
        print(f'Accepting a connection from {addr[0]}, {addr[1]}...')
        t = threading.Thread(target=handlereq, args=(conn,))
        t.start()

