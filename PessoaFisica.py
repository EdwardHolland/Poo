class PessoaFisica:
    nome = ''
    idade = 0
    __cpf = 0
    cnh = 0
    dataNascimento = 0
    tituEleitor = bool
    _salario = 0


    def __init__(self, nome = None, idade = None):
        self.nome = nome
        self.idade = idade

    def getNome(self):
        return self.nome
    def getIdade(self):
        return self.idade

    def setCpf(self, __cpf):
        self.__cpf
    def getCpf(self):
        return self.__cpf

    def setCnh(self, cnh):
        self.cnh = cnh
    def getCnh(self):
        return self.cnh

    def setDateNasc(self, dataNasc):
        self.dataNascimento = dataNasc
    def getDateNasc(self):
        return self.dataNascimento

    def setTituEleitor(self, tituEleitor):
        self.tituEleitor = tituEleitor
    def getTituEleitor(self):
        return self.tituEleitor

    def setSalario(self, salario):
        self._salario = salario
    def getSalario(self, salario):
        return self._salario

    def vote(self):
        print('{} está votando no Bolsomito...'.format(pessoa.getNome()))

    def dirija(self):
        print('{} está dirigindo...'.format(pessoa.getNome()))

    def compra(self):
        print('{} está comprando...'.format(pessoa.getNome()))

    def ganheDinheiro(self):
        print('{} está ganhando dinheiro...'.format(pessoa.getNome()))

pessoa = PessoaFisica('Eduardo',18)

