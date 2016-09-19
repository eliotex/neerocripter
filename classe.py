import _md5
class neero:
    def __init__(self,mensagem='',chave=0,dic=[],dic2=[]):
        self.mensagem = mensagem
        self.chave = chave
        self.dic = dic
        self.dic2 = dic2
    def cript_caesar(self):
        for letter in str(self.mensagem):
            print(self.dic[self.dic.index(letter)+int(self.chave)],end="")
    def decrypt_caesar(self):
        for letter in self.mensagem:
            print(self.dic[self.dic.index(letter)-int(self.chave)])
    def cript_vigenere(self):
        for letter in self.mensagem:
            print(self.dic2[self.dic.index(letter)])
    def decrypt_vigenere(self):
        for letter in self.mensagem:
            print(self.dic[self.dic2[self.dic.index(letter)]])
    def cript_md5(self,_md5):
        m = _md5.new()
        m.md5.new(self.mensagem).digest()
