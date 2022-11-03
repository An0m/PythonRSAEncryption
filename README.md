# Python RSA Encryption with M2Crypto
 A (probably vulnerable) way to encrypt files using the python M2Crypto RSA (and AES) module.
 
 If you're starting to code and you just want a way to encrypt and decrypt files with assymetric encryption, in python, and you just want something that works... you shouldn't but there you go.

 I wrote this thing in 10min without thinking about possible vulnerabilities, and considering I only have a base knowledge of asymetric encryption this code is probably an insult to Ron Rivest, but hey, how am i to judge.

## Why?
 I have no clue. It's 1am, I'm bored.

## Yes but why python?
 Yes.

<br>
Note: In this algoritm, the AES key and the AES initial vector (256b each) after the encryption (with a 4096b pub key) always weight 512b each. With a 8192b pub. key they whould weight 1024b each and so on.
