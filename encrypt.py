from M2Crypto import EVP, RSA
from os import urandom

aesKey = urandom(256)
aesIv = urandom(256)

with open("in.txt", "rb") as fin: 
    with open("out.enc", "wb") as fout:
        # Add the (encrypted with RSA) AES key and the initial vector at the start of the file

        rsa = RSA.load_pub_key("public.pem")
        fout.write(
            rsa.public_encrypt(aesKey, RSA.pkcs1_oaep_padding) + 
            rsa.public_encrypt(aesIv, RSA.pkcs1_oaep_padding)
        ) # Always 512 bytes using a 4kb key

        # Encrypt the file using AES encryption
        aes = EVP.Cipher(alg="aes_128_cbc", key=aesKey, iv=aesIv, op=1)

        while True:
            buf = fin.read(1024)
            if not buf:
                break
            fout.write(aes.update(buf))

        fout.write(aes.final())
