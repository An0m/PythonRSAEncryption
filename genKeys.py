from M2Crypto import  RSA, Rand
import os

Rand.rand_seed(os.urandom(1024))
rsa_key = RSA.gen_key(4096, 65537)
rsa_key.save_key('private.pem', None)
rsa_key.save_pub_key('public.pem')
