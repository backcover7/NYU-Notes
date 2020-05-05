import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from Crypto import Random
from Crypto.Random import random
from Crypto.PublicKey import ElGamal
from Crypto.Util.number import GCD
from Crypto.Cipher import DES3


# Asymmetric - RSA
def RSAEncrypt(message, key_size = 2048):
    '''

    :param message: str
    :param key_size: 2048 or 4096
    :return: byte object
    '''

    private_key = rsa.generate_private_key(public_exponent = 65537,
                                           key_size = key_size,
                                           backend = default_backend())
    public_key = private_key.public_key()
    message_byte = bytes(message, encoding = 'utf-8')
    cipher_text = public_key.encrypt(message_byte,
                                     padding.OAEP(mgf = padding.MGF1(algorithm = hashes.SHA256()),
                                                  algorithm = hashes.SHA256(),
                                                  label = None)
                                     )

    # serializition
    pem = private_key.private_bytes(encoding=serialization.Encoding.PEM,format=serialization.PrivateFormat.TraditionalOpenSSL,encryption_algorithm=serialization.NoEncryption())
    return cipher_text

# message = 'a'
# print(RSAEncrypt(message))


def RSADecrypt(cipher_text, pem):
    '''

    :param cipher_text: bytes object
    :param pem: byte object
    :return: byte object
    '''

    cipher_text = cipher_text
    pem = pem
    private_key = serialization.load_pem_private_key(pem, None, backend=default_backend())
    plain_text = private_key.decrypt(cipher_text,
                                     padding.OAEP(mgf = padding.MGF1(algorithm = hashes.SHA256()),
                                                  algorithm = hashes.SHA256(),
                                                  label = None)
                                     )
    return plain_text

# cipher_text = b"\x18#0Y^f&\x06\xb9\xb4\xd8\xde`\x01\xa0j\x02&Tb\xfa\xa5iu\xfd\xf3\xce\x7f\xad\xbc\xdcC\xee\xcd\ty\x8a\xcb!\x8al\x97L\xa7\x12\x95\xc0\xf3\x15\xa1'\xd6\xf9\x16\xa0\x9bv;\xe3$1\xd1A3\x8f\x8f\x84\x92\xbfyr\x1cyo\x8bwD,\x10\xd2\xda\xc3I\xf9\xcd\x10\xf1\x83W\x99#\xe4X\x9cA\x1d,1Vl\x96\xbc\xf6\x87\xa7\x0c\xbe\xcc\x88kC\x9e\x85`R\xe5\xdc\xbc\xe3\xcf\xd4\x94\xab\x9a\xa8v\xef\xe4\xe7Dd\xacmL\xd3\xc2)s\xcc\x12W\x00\x87\xfe'c\xe3O\xfe\xf0.\x9e-r\x18[>\x9e<\xa8III\xc6\xd14\n\x06&\x02\xa8\xb8\xfe\x81\x1a\x12\x11\x9di\x04\xb1\xd6g5\xd1\xd78^\x0e\x17\x846\xeb\xb3\xa7\xa0\x04*\xf6\x8cd\xe2\x85\xd8<\xaf&\xdb\xbbp`V%Y\xa2'n\xf8\x04\x85\xe8\xbb\tG\x9d&\xee\xad~\x1f>\xd7i\x03\xc3\xbev\x12B\x86y\xef\xbd\x94\x1d\x99&5\xa9\x14J\x94!\xa2f\xba"
# pem = b'-----BEGIN RSA PRIVATE KEY-----\nMIIEpAIBAAKCAQEAyyJQBeSxKmeUxy8IgXZPXDK89nuiVevW79tbjEyRYj+nC+zo\nggSV4RfAZ3LFmIlVNcoziETm8/+38oeuj3a3vHcP0CdVSBv5ogROyWMNYWfX3OiA\nI2QCiJjH461e5LinFIdzqWNA0KJ/AD0RlOvq3oLUi30VLYuo0nZ8pV9cDymO11Ia\n7TIXk9mklJT1XyBModEaxU3v+dvwcPjLj+Z81tpUiJ5ZGjkvpI7MOWkJB/+pv/sJ\ny294PqW6/3oBI0qM+7vvpE6HSkpbvRuJaAIV3jjKF+nj7lZ2rMu9E65tSETzVNN6\nffwgOdYIHKsQl3gWTRpkgrsDBtc6mZS1tI97MwIDAQABAoIBADYMtTo8NZ/Q29d7\n/klkT416uqjjELjH/fLobR2RqgV4ZlxX9y3RRogUJ8/ezBDgSdn8KWYS31kBK9LO\no3Xs4sq063I5ZQnA19VyS/xt7LuEQ/21p5LDI6Fw9Y7xLJSzRVHDENV7YV2iPySz\nGyCC/YWjTiana6EozgziFhxymS43KQv/aKiCAzB/tqDzJcDlTkIQ0dKxT8/Hu7AY\n9DmQhksqAyGGFbo/2I9aJZv/rNeemw/+BEYojahv3v0V4tKD7uRewe9KSzdIsD8N\nMk/Im3iyhHwUmt1XuSHaXtQbjEzVoGqeCrR+VC7eUgvRYy/CH2xZVlmQDQhrKGew\nduwkOOECgYEA8VUEwNQL53rZQMwUOFolfM8Ek5sSNHJ9uGRaER50IexgE79DZIDf\niFxXyIydlNGxf8zd8iL8XecMb16naWa+XEHeZ1RQvH1om48Ljb5x5vvmGDh0Yy5g\nSPbLlw6xIsNfS9hs+RUHLOSLD9qEZBIUf0wnXhQIEzSv/MJexfkSvukCgYEA13r0\nhljD1RmTU2tX23dieBn746FkxaRxOTJl/28sxXFbto+dB3GpAToj+WV8qmTSTvce\nypya3FEd7aELb/I89Ag0wpB3E2MnV/Oczv1Ys5PPugbJdkTIbUi5woHqZ+dvKeAT\nKLs9spMArC58xoSqRjHiGlN5rH0mYMScwBH/b7sCgYEAgGiDYfKx7tYP+QldjOpy\nXels/vkZA60TteQ3hDpXAqHaMUeonTZxOgYgc0ZWppO4xU6Fncv9yh0hIbUUkOGp\nUj9+Di7v0otL+NFxDVeTFZtcv/ByBT/s3YXrqBGaMOwRrbKXsST+L2XflGzp2rFA\nFMe5frZb4ZQ8O9pUQTSZQ9kCgYEAnTBUsKyQLyQ5FOF5dd/hNTu/RI63tHYBInhh\nb7TqNB49iS+6nXOMlhiTpZsjFin2QSSEkcksLwv9iRux/Df5vws9cbFxK/No///2\npAisbFOndUz+KgiDLTWgTQP4u1NZBHMxhsUQfPQ/yVsgKrEchZheGFZMrEefd3f1\n4Sc/74ECgYAh2Es1u9rLXlmzJAAnzsdR309FUauOVUez/2dsAaoNFN2HSPDa3OEJ\nhT0iI8wlnB3ewFq3dg7AGlSBonGaw2Oo4/UI4Plw8Mz9rCzuygPdAMFrkwO2728w\naNS1+a/K+4ZHeTNmBMGzxF6U8mVbgSyqeLKeLBGYEBLpCg4V//QHfw==\n-----END RSA PRIVATE KEY-----\n'
# print(RSADecrypt(cipher_text,pem))




# Symmetric encryption - AES
def AESEncrypt(message, mode, key = None):
    '''

    :param message:  byte object
    :param key: bytes object
    :param mode:  (str) CBC, CTR, OFB, CFB
    :return: byte object
    '''
    if not key:
        key = os.urandom(16)
    iv = os.urandom(16)
    if mode == 'CBC':
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend())
        while len(message)% 16 != 0:
            message += b' '
    if mode == 'CTR':
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend = default_backend())
    if mode == 'OFB':
        cipher = Cipher(algorithms.AES(key), modes.OFB(iv), backend = default_backend())
    if mode == 'CFB':
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend = default_backend())

    encryptor = cipher.encryptor()
    ct = encryptor.update(message) + encryptor.finalize()
    return ct



message = b'a secret message'
print(AESEncrypt(message, 'CBC'))

def AESDecrypt(cipher_text, key, iv, mode):
    '''

    :param cipher_text: byte object
    :param key: byte object
    :param iv: byte object
    :param mode: (str) CBC, CTR, OFB, CFB
    :return: byte object
    '''

    if mode == 'CBC':
        cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend = default_backend())
    if mode == 'CTR':
        cipher = Cipher(algorithms.AES(key), modes.CTR(iv), backend = default_backend())
    if mode == 'OFB':
        cipher = Cipher(algorithms.AES(key), modes.OFB(iv), backend = default_backend())
    if mode == 'CFB':
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend = default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(cipher_text) + decryptor.finalize()

# cipher_text = b'\x1a`\xc9\xf9\x03\xbc\xbf\x93\xbb\x92M\xa20mL\xb5'
# key = b'T\xdf\x9f\xd8:%$\xa5\xad\x7f\xd6#&\xb12\xca'
# iv = b'\xa8\x1d\xee-\xf3\\\xab\xaf\xbb\xf3\x94\xa1b\xb9\xa9\xe6'
# print(AESDecrypt(cipher_text,key,iv,'CBC'))





# Symmetric encryption - 3DES
def tripleDesEncrypt(message,key_size,mode):
    '''
    :param message: byte object
    :param key_size: key size (must be either 16 or 24 bytes long)
    :param mode: OFB,CBC,CFB
    :return: byte object
    '''

    key = os.urandom(int(key_size))
    iv = Random.new().read(DES3.block_size)
    # plaintext length (in bytes) must be a multiple of block_size.
    while len(message) % 8 != 0:
        message = message + b' '
    if mode == 'OFB':
        cipher_encrypt = DES3.new(key, DES3.MODE_OFB, iv)
    if mode == 'CBC':
        cipher_encrypt = DES3.new(key,DES3.MODE_CBC,iv)
    if mode == 'CFB':
        cipher_encrypt = DES3.new(key,DES3.MODE_CFB,iv)

    if mode == 'CTR':
        cipher_encrypt = DES3.new(key,DES3.MODE_CTR,counter = lambda :iv)


    cipher_text = cipher_encrypt.encrypt(message)
    return (cipher_text,key,iv)

# message = b'hihihi'
# print(tripleDesEncrypt(message,16,'CFB'))

def tripleDESDescrypt(cipher_text, key, iv, mode):
    '''
    :param cipher_text: byte object
    :param key: byte object
    :param iv: byte object
    :param mode: OFB, CBC, CFB
    :return: byte object
    '''
    if mode == 'OFB':
        cipher_decrypt = DES3.new(key, DES3.MODE_OFB, iv)
    if mode == 'CBC':
        cipher_decrypt = DES3.new(key, DES3.MODE_CBC, iv)
    if mode == 'CFB':
        cipher_decrypt = DES3.new(key, DES3.MODE_CFB,iv)

    if mode =='CTR':
        cipher_decrypt = DES3.new(key,DES3.MODE_CTR,counter = lambda :iv)

    plain_text = cipher_decrypt.decrypt(cipher_text)
    return plain_text


# key = b'\xed\xf4\xbfqF\x11\xfcq\xf0}\xa5E\x1e\xcb\ny'
# iv = b'4\xbd\xe3\xaa\xf4\xd7\xb53'
# mode = 'CTR'
# cipher_text = b'\xd3\xb6?\x8a @\xff\xa5'
# print(tripleDESDescrypt(cipher_text, key, iv, mode))



# key exchange
def ECDHServer(peer_public_key):
    '''

    :param peer_public_key: ellipticalPublicKey Object
    :return: byte objects
    '''
    server_private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
    # server_pulic_key is used to send to peer
    server_pulic_key = server_private_key.public_key()
    shared_key = server_private_key.exchange(ec.ECDH(), peer_public_key)
    derived_key = HKDF(algorithm=hashes.SHA256(),
                       length=16,
                       salt=None,
                       info=b'handshake data',
                       backend=default_backend()).derive(shared_key)
    return derived_key



def ECDHPeer(server_public_key):
    '''

    :param server_public_key: ellipticalPublicKey Object
    :return: byte type
    '''
    peer_private_key = ec.generate_private_key(ec.SECP384R1(), default_backend())
    # peer_public_key is used to send to server
    peer_public_key =peer_private_key.public_key()
    shared_key = peer_private_key.exchange(ec.ECDH(), server_public_key)
    derived_key = HKDF(algorithm=hashes.SHA256(),
                       length=16,
                       salt=None,
                       info=b'handshake data',
                       backend=default_backend()
).derive(shared_key)
    return derived_key


def ElGamlaEncrypt(message):
    key = ElGamal.generate(1024, Random.new().read)
    while 1:
        k = random.StrongRandom().randint(1, key.p - 1)
        if GCD(k, key.p - 1) == 1: break
    cipher_text = key.encrypt(message,k)
    return cipher_text

# message = b'hello'
# print(EIGamlaEncrypt(message))

def ElGamlaDecrypt(cipher_text,key):
    plain_text = key.decrypt(cipher_text)
    return plain_text





