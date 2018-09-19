class PessoaJuridica:
    razSocial = ''
    cnpj = 0
    insEstadual = 0
    caixa = 0.0

    def setRazSocial(self, razSocial):
        self.razSocial = razSocial
    def getRazSocial(self):
        return self.razSocial

    def setCnpj(self, cnpj):
        self.cnpj = cnpj
    def getCnpj(self):
        return self.cnpj

    def setInscEstadual(self, inscEstadual):
        self.insEstadual = inscEstadual
    def getInscEstadual(self):
        return self.insEstadual

    def setCaixa(self, caixa):
        self.caixa = caixa
    def getCaixa(self):
        return self.caixa

empresa = PessoaJuridica()