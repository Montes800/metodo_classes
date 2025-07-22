from abc import ABC, abstractmethod  # Importação correta

# Classe abstrata
class ControleRemoto(ABC):
    @abstractmethod  # Método abstrato
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

# Class que implementa a abstrata
class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("Ligado")

    def desligar(self):
        print("Desligando a TV")
        print("Desligado")

# Instância e uso
controle = ControleTV()
controle.ligar()
controle.desligar()
