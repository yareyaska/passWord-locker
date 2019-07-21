import os, math, string, struct

def generate_password(pass_len):
    symbols = string.printable.strip()
    return ''.join([symbols[x * len(symbols) / 256] for x in struct.unpack('%dB' % (pass_len,), os.urandom(pass_len))])