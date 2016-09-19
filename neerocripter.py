#!/usr/bin/python
def Main():
    print(arg.help)
import classe
import argparse
dic = ["a","b","c","d",'e','f''g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dic2 = []
menu = argparse.ArgumentParser("A cripto tool")
menu.add_argument("--cc","--cript_caesar",help="Caesar Cipher",action="store")
menu.add_argument("--key","--kk",help="Argument for chipher were needs keys",action="store")
menu.add_argument("--dc","--dca",help="Decrypt Caesar Chipher",action="store")
menu.add_argument("--caesar", "--caesar", help="Option to cript and decript caesar ciphers", action="store_true",default="false")
menu.add_argument("--vig","--vig",help="Vigenere cypher",action="store_true",default="false")
menu.add_argument("--cvig","--cvig",help="Cript Vigenere Cypher",action="store")
menu.add_argument("--dvig","--dvig",help="Decrypt Vigenere Cypher",action="store")
menu.add_argument("--md5","--md5",help="md5 function",action="store_true",default="false")
menu.add_argument("--cmd5","--cmd5",help="cript md5",action="store")
arg = menu.parse_args()

if arg.caesar == True:
    c = classe.neero(arg.cc,arg.key,dic)
    print(c.cript_caesar())
    print(c.decrypt_caesar())
if arg.vig == True:
    c = classe.neero(arg.cvig,arg.dic,arg.d)
    print("Criptografia vig")
    elementos = input("Digite os número de elementos do dicionario:")
    if elementos.isalpha:
        print("Você colocou uma letra por favor digite um número")
    else:
        for number in int(elementos):
            dados = input("Digite os dados do dicionario")
            dic2.insert(dados)
    print(c.cript_vigenere())
    print(c.decrypt_vigenere())
print(c.cript_md5())