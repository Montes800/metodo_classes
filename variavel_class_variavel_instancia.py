class Estudante: 
    escola = "DIO"  # atributo de classe

    def __init__(self, nome, matricula):  # construtor correto
        self.nome = nome  # atributo de instância
        self.matricula = matricula

    def __str__(self):  # método correto para printar objetos
        return f"{self.nome} - {self.matricula} - {self.escola}"

def mostrar_valores(*objs):  # parâmetro corrigido
    for obj in objs:
        print(obj)

aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"  # altera o atributo de classe
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)

