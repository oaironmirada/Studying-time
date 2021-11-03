class Carro():
    def __init__(self, marca, modelo, ano, cor, statusFarol = 'desligado'):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.statusFarol = statusFarol
        self.velocimetro = 0
        self.__status = False

    def ligarFarol(self):
        if(self.statusFarol == 'desligado'):
            self.statusFarol = 'ligado'
            print('Farol Ligado')
        else:
            print("O farol já está ligado")
        
    def desligarFarol(self):
        if(self.statusFarol == 'ligado'):
            self.statusFarol = 'desligado'
            print('Farol desligado')

    def acelerar(self, acressVelocidade):
        self.velocimetro = self.velocimetro + acressVelocidade

    def frear(self, decressVelocidade = 5):
        if(self.velocimetro > decressVelocidade):
                self.velocimetro = self.velocimetro - decressVelocidade
        else:
            self.velocimetro = 0

    def getStatus(self):
        return self.__status

    def setStatus(self, novo_status, chave):
        chave_certa = self.__verificaChave(chave)
        if chave_certa:
            self.__status = novo_status
        else:
            print("O status não pode ser alterado")

    def __verificaChave(self, chave):
        if chave == 123456:
            return True
        else:
            return False
            
gol = Carro('wolks', 'gol', 2010, 'laranja')
fusca = Carro('wolks', 'fusca', 1990, 'azul claro')
uno = Carro('fiat', 'uno', 2000, 'azul escuro', statusFarol='ligado')
gol2 = Carro('wolks', 'gol', 2010, 'laranja')
jeep = Carro('jeep', 'renegate', 2015, 'branco')

fox = Carro('wolks', 'fox', 2009, 'prata')

fox.setStatus(True, 123456)
print(fox.getStatus())