from M2Crypto import EVP, RSA

with open("out.enc", "rb") as fin: 
    with open("dec.txt", "wb") as fout:
        # Read the (encrypted with RSA) AES key and the initial vector at the start of the file

        rsa = RSA.load_key("private.pem")
        aesKey = rsa.private_decrypt(fin.read(512), RSA.pkcs1_oaep_padding) # Always 512 bytes using a 4kb key
        aesIv = rsa.private_decrypt(fin.read(512), RSA.pkcs1_oaep_padding) # Same as before

        # Decrypt the file using AES encryption
        aes = EVP.Cipher(alg="aes_128_cbc", key=aesKey, iv=aesIv, op=0)

        while True:
            buf = fin.read(1024)
            if not buf:
                break
            fout.write(aes.update(buf))

        fout.write(aes.final())
