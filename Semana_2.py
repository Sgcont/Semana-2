import random
class jogo:
    def __init__(self, nome):
        self.nome = nome
    def pegar_palavras(self):
        palavras = ["jogo", "casa", "pedra", "papel", "tesoura", "vento"]
        i = random.randint(0,len(palavras)-1)
        self.palavra = palavras[i]
        pass
    def start(self):
        self.r = "*"*len(self.palavra)
        k=0
        while k<10:
            print(f"Temos a palavra {self.r} com {len(self.r)}")
            resposta = input("Diga a letra que quer buscar na palavra:")
            if len(resposta) != 1:
                print("Você não escreveu uma letra\n")
                continue
            if resposta in self.palavra:
                for j in range(len(self.palavra)):
                    if resposta == self.palavra[j]:
                        self.r = self.r[:j] + resposta + self.r[j+1:]
            else:
                print(f"A letra {resposta} não está na palavra!")
            if self.r == self.palavra:
                break
            k+=1
    def end(self):
        if self.r == self.palavra:
            print(f"Parabéns {self.nome}! Você venceu!")
        else:
            print("Vishh... Voce tem algum chute do que seria?")
            palavra_ = input()
            if palavra_ == self.palavra:
                print(f"Ai sim {self.nome}! Venceu!")
            else:
                print(f"Não... Não era essa {self.nome}... Era {self.palavra}. It's over, wake up Neo")

jogo1 = jogo("Lucas")
jogo1.pegar_palavras()
jogo1.start()
jogo1.end()

#A do "pedra,papel e tesoura" eu acabei já usando função ksksksksksksksk então, da semana passada já conta teoricamente ksks