import _md5
import random
class neero:
    def __init__(self,mensagem='',dic=[],dic2=[]):
        self.mensagem = mensagem
    def cript_caesar(self,chave):
        self.chave = chave
        for letter in self.mensagem:
            n = ord(letter) + int(self.chave)
            if letter.isspace():
                print(letter,end="")
            else:
                print(chr(n),end="")
        print("\n")
    def decrypt_caesar(self,chave):
        self.chave=chave
        for letter in self.mensagem:
            if letter.isspace():
                print(letter,end="")
            else:
                print(chr(ord(letter) - int(self.chave)),end="")
        print("\n")

    def cript_vigenere(self):
        for letter in self.mensagem:
            print(self.dic2[self.dic.index(letter)])

    def decrypt_vigenere(self):
        for letter in self.mensagem:
            print(self.dic[self.dic2[self.dic.index(letter)]])

    def cript_md5(self, _md5):
        m = _md5.new()
        m.md5.new(self.mensagem).digest()


