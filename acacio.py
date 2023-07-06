def imprimesoma (a,b):
    """
    Imprime a soma de dois números
    """
    c = a + b
    return print ('A soma é %d'%c)
def multiplica (a, b):
    """
    Imprime a multiplicação de dois números
    """
    c = a * b
    return print ('A multiplicação é %d'%c)
#1. Classe bola
class Bola:
    def __init__ (self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor(self, cor):
        self.cor = cor
        print('A nova cor é '+ self.cor)
    def mostraCor(self):
        print('A cor atual é ' + self.cor)