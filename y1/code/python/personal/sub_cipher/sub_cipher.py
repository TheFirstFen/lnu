# sub_cipher.py
#
# Author: Samuel Berg
# Date: 10-Sep-2019

import base64
import hashlib
import sys

# encryption key which could be anything
KEY = b'akKJ6779N8*n73*66876934nHUHkoajjfh86%(T96'

# create a list of all the characters in base64 w/ padding
b64_chars = [
    c for c in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/=']


def convert(string, type):
    # take sha512 hash of the key
    hash = hashlib.sha512(KEY).hexdigest()

    # initial cipher is a copy of the base64 characters
    cipher = b64_chars[:]

    # loop over each element in the hash and rearrange the cipher
    for c in hash:
        char_int = int(c, 16)
        pos = 65 * (char_int / 15)

        # move the element to the beginning of the list and reverse the list
        cipher.insert(0, cipher.pop(int(pos) - 1))
        cipher = cipher[:: - 1]

    sbox = {}

    # create the mapping between base64 characters and the rearranged base64 characters
    for i, c in enumerate(b64_chars):
        sbox[c] = cipher[i]

    # if this operation is decryption, keys/values must be reverse
    if type == 'd':
        sbox = dict((v, k) for k, v in sbox.items())

    # substitute characters in the string according to the sbox
    for i, c in enumerate(string):
        string[i] = sbox[c]

    return ''.join(string)


def encrypt(string):
    # base64 encode plaintext and convert to list of characters
    string = [c for c in base64.b64encode(string.encode()).decode()]

    return convert(string, 'e')


def decrypt(string):
    string = [c for c in string.strip()]

    return base64.b64decode(convert(string, 'd')).decode()


if sys.argv[1] == '-d':
    print(decrypt(sys.stdin.read()))
