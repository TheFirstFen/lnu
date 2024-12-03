import requests
from pathlib import Path
import re
import hashlib
from concurrent.futures import ThreadPoolExecutor

# Assumes the server runs on localhost, port 80.
server = '127.0.0.1'
port = 8888

# Points to the files themselves
dirbase = Path('./public')

# Allow for .htm solutions
fe = '.html'


def killWS(s):
    return re.sub(r'\s', '', s)


def loadPage(fn):
    s = open(dirbase / fn).read()
    return killWS(s)


def loadImage(fn):
    s = open(dirbase / fn, 'rb').read()
    return s


def requestPageOK(p, pn):
    try:
        if not (dirbase / p).is_file():
            fn = Path(p) / f'index{fe}'
        else:
            fn = p

        r = requests.get(f'http://{server}:{port}/{p}')

        if r.status_code != requests.codes.ok:
            print(f'Error: {pn} failed with code {r.status_code}')
            return

        if r.headers['content-type'] != 'text/html':
            print(f'Error: {pn} has content type {r.headers["content-type"]}')
            return

        if killWS(r.text) != loadPage(fn):
            print(f'Error: {pn} not same as local copy')
            return

        print(f'OK: {pn}')
    except Exception as e:
        print(f'Error: {pn} encountered exception {e}')


def requestPageNotOK(p, pn, code):
    try:
        r = requests.get(f'http://{server}:{port}/{p}')

        if r.status_code == requests.codes.ok:
            print(f'Error: {pn} succeeded with code {r.status_code}')
            return

        if r.status_code != code:
            print(f'Error: {pn} expected code {code}, got {r.status_code}')
            return

        print(f'OK: {pn}')
    except Exception as e:
        print(f'Error: {pn} encountered exception {e}')


def requestImage(p, pn):
    try:
        r = requests.get(f'http://{server}:{port}/{p}')

        if r.status_code != requests.codes.ok:
            print(f'Error: {pn} failed with code {r.status_code}')
            return

        if r.headers['content-type'] not in ['image/png', 'image/x-png']:
            print(f'Error: {pn} has content type {r.headers["content-type"]}')
            return

        image = loadImage(p)
        if 'content-length' in r.headers:
            contentLengthVar = r.headers['content-length']
            if not r.headers['content-length'].isdigit():
                print(f'Error: {pn} content length not a number.')
                return
            elif int(r.headers['content-length']) != len(image):
                print(f'Error: {pn} content length incorrect')
                return
        else:
            print(f'Notice: {pn} has no content length header')

        image_h = hashlib.sha256()
        image_h.update(image)

        r_image_h = hashlib.sha256()
        r_image_h.update(r.content)

        if r_image_h.digest() != image_h.digest():
            print(f'Error: {pn} not same digest as local copy')
            return

        print(f'OK: {pn}')
    except Exception as e:
        print(f'Error: {pn} encountered exception {e}')


# Define test cases
test_cases = [
    lambda: requestPageOK('', 'Main index page'),
    lambda: requestPageOK(f'named{fe}', 'Named page'),
    lambda: requestImage('clown.png', 'Clown PNG'),
    lambda: requestImage('a/b/bee.png', 'Bee PNG'),
    lambda: requestImage('world.png', 'World PNG'),
    lambda: requestPageOK('a/', 'Index a'),
    lambda: requestPageOK(f'a/a{fe}', 'Page a'),
    lambda: requestPageNotOK(f'nosuchpage{fe}', 'Page fail', 404),
    lambda: requestPageNotOK('a/b/c/noimage.png', 'Image fail', 404),
    # Add more test cases as needed
]

# Run test cases concurrently
if __name__ == '__main__':
    with ThreadPoolExecutor() as executor:
        executor.map(lambda test: test(), test_cases)

