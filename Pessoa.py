import PessoaFisica
class Pessoa(PessoaFisica):
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
print('Nome: {} \nIdade: {} \nAltura: {} \nPeso: {}Kg'.format(pessoa.getNome(),pessoa.getIdade(),pessoa.getAltura(),pessoa.getPeso()))
pessoa.andar()
pessoa.falar()