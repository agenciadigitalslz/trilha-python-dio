class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def trocar(self):
        print("Trocando a bicicleta!")

    def trocada(self):
        print("Bicicleta trocada!")
    
    def agora(self):
        print("Estou na biscicleta!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("Vermelha", "Caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b1.trocar()
b1.trocada()
b1.agora()

b2 = Bicicleta("Verde", "Monark", 2000, 189)
print(b2.cor, b2.modelo, b2.ano, b2.valor)
# print(b2)
b2.correr()