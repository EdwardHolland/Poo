from PessoaFisica import *
from PessoaJuridica import *
class Pessoa(PessoaFisica, PessoaJuridica):
    altura = 0.00
    idade = 0
    nome = ""
    __peso = 0

    def setNome(self, nome):
        self.nome = nome
    def getNome(self):
        return self.nome

    def setIdade(self, idade):
        self.idade = idade
    def getIdade(self):
        return self.idade

    def setAltura(self, altura):
        self.altura = altura
    def getAltura(self):
        return self.altura

    def setPeso(self, peso):
        self.__peso = peso
    def getPeso(self):
        return self.__peso

    def andar(self):
        print('{} está andando...'.format(pessoa.getNome()))

    def falar(self):
        print('{} está falando...'.format(pessoa.getNome()))

pessoa = Pessoa()
pessoa.setNome('Eduardo')
pessoa.setIdade(18)
pessoa.setAltura(1.75)
pessoa.setPeso(90)
pessoa.setTituEleitor(False)

print('==================VOTAR==================')
if(pessoa.getIdade() >= 18):
    if(pessoa.getTituEleitor() == True):
        pessoa.vote()
    else:
        print('Você precisa tirar seu título de eleitor!')
else:
    print('Você não pode votar!')

print('==========================================')
print('===============Calcular IMC===============')
imc = pessoa.getPeso()/(pessoa.getAltura()*pessoa.getAltura())
print('Seu IMC é: {} '.format(imc))

if(imc < 18,5):
    print("{}, você está abaixo do peso!".format(pessoa.getNome()))
if(imc > 18,5 & imc < 24,9):
    print("{}, você está com o peso normal!".format(pessoa.getNome()))
if(imc > 24,9 & imc < 29,9):
    print('{}, você está com sobre peso!'.format(pessoa.getNome()))
if(imc > 29,9):
    print('{}, sua vida está em risco!'.format(pessoa.getNome()))