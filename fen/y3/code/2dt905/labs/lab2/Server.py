from socket import *
import threading
from pathlib import Path
basedir = 'public'

def handlereq(cs):
    try:
        req = cs.recv(1024) # 
        m, l, p = parsereq(req.decode()) #parse based on method location and protocol
        resp = flfile(l)   #generate resposne by finding and loading file
        cs.sendall(resp)  # send the response and close the socket
    finally:
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
    resp = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<h1>404 Not Found</h1>'
    return resp.encode()

def main():
    with socket(AF_INET, SOCK_STREAM) as s:
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # Allow immediate reuse of the port
        s.bind(('', 8888))
        s.listen()
        print("Server is listening on port 8888...")

        try:
            while True:
                conn, addr = s.accept()
                print(f'Accepted connection from {addr[0]}:{addr[1]}...')
                t = threading.Thread(target=handlereq, args=(conn,))
                t.start()
        except KeyboardInterrupt:
            print("\nShutting down server...")
        finally:
            s.close()  # Ensure the socket is closed

if __name__ == "__main__":
    main()
