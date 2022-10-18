import os
import rsa
import sys
from relay8p import caminho

def encrypt_pwd(pwd):
    if os.path.exists(caminho('keys\public.pem')) != True and os.path.exists(caminho('keys\private.pem')) != True:
        generate_pem()

    with open(caminho('keys\public.pem'), 'r') as file:
        leituraArqByKeyPubli = file.read()
    public_key = rsa.PublicKey.load_pkcs1(leituraArqByKeyPubli)
    textocrypt = rsa.encrypt(pwd, public_key)
       
    # print(textocrypt)
    # print('----------------------------------')

    return carregaOuCria(textocrypt), textocrypt
    

def generate_pem():
    public_key, private_key = rsa.newkeys(1024)

    public_pem = caminho('keys\public.pem')
    private_pem = caminho('keys\private.pem')
    try:
        with open(private_pem, 'w+') as f:
            f.write(private_key.save_pkcs1().decode())
        with open(public_pem, 'w+') as f:
            f.write(public_key.save_pkcs1().decode())

    except Exception as ex:
        pass

    return public_pem, private_pem


def carregaOuCria(textocrypt):
    pathConfig = caminho('config\config.txt')

    if os.path.exists(pathConfig) != True:
      with open(pathConfig, 'wb') as file:
            file.write(textocrypt)
      with open(pathConfig, 'rb') as file2:
                 txt = file2.read()
    else: 
         with open(pathConfig, 'rb') as file3:
                txt = file3.read()
    return txt


def escreveSenhaNova(pwd):
    pwd = str(pwd)
    var = encrypt_pwd(pwd.encode())
    lista = []
    pathConfig = caminho('config\config.txt')

    for i in var:
        lista.append(i)
    novaSenhaEncry = lista[1]
    with open(pathConfig, 'wb') as file:
        file.write(novaSenhaEncry)
    # print('-----------------------')
    # print("Escreveu")
    

def descrypt_pwd():
    pathPriv = caminho('keys\private.pem')
    pathConfig = caminho('config\config.txt')

    with open(pathPriv, 'rb') as file:
        leituraArqByKeyPriv = file.read()

    with open(pathConfig, 'rb') as file2:
        encryMessage = file2.read()

    private_key = rsa.PrivateKey.load_pkcs1(leituraArqByKeyPriv)
    deencryMessage = rsa.decrypt(encryMessage, private_key) 
    return deencryMessage.decode('utf-8')