#!/usr/bin/python
def Main():
    print(arg.help)
import classe
import argparse
menu = argparse.ArgumentParser("A cripto tool")
menu.add_argument('--fc','--fc',action="store_true",default="false")
menu.add_argument('-sc','-sc',action="store_true",default='false')
menu.add_argument('-k','-key',action="store",type=int)
menu.add_argument('-dc','-dc',action="store")
menu.add_argument('--md','--md',action="store_true",default='false')
menu.add_argument('--fv','-fv',action="store_true",default='false')
menu.add_argument('--sv','-sv',action="store_true",default='false')
menu.add_argument('--vdc','-vdc',action="store_true",default="false")
menu.add_argument('-cipher','-cipher',action="store")
menu.add_argument('-md5','-md5',action="store")
arg = menu.parse_args()

if arg.fc == True:
    mensagem = input("Digite sua mensagem:")
    cript = classe.neero(mensagem)
    cript.cript_caesar(arg.k)
if arg.sc == True:
    decrypt = classe.neero(arg.dc)
    cript.decrypt_caesar(arg.k)
if arg.fv == True:
    mensagem = input("Digite sua mensagem:")
    cript = classe.neero(mensagem)
    cript.cript_vigenere(arg.cipher)
if arg.sv == True:
    cript = classe.neero(arg.vdc)
    cript.decrypt_caesar(arg.cipher)
if arg.md == True:
    cript = classe.neero(arg.md5)
    print(cript.cript_md5())
