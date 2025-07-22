class Pessoa:
    def __init__(self, nome, idade=None):
        self.nome = nome               # atributo de instância
        self.idade = idade             # atributo de instância

    @classmethod  # transforma o método em um método de classe
    def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2025 - ano             # calcula a idade com base no ano de nascimento
        return cls(nome, idade)        # usa cls para retornar uma nova instância da classe Pessoa

    def __str__(self):
        return f"{self.nome} - {self.idade} anos"  # define como o objeto será representado ao usar print()

    @staticmethod  # transforma o método em método estático (não acessa self nem cls)
    def e_maior_idade(idade):
        return idade >= 18             # retorna True se a idade for maior ou igual a 18

# p = Pessoa("João", 27)               # instanciando manualmente
# print(p.nome, p.idade)

# Criando pessoa a partir da data de nascimento usando método de classe
p2 = Pessoa.criar_apartir_data_nascimento(1998, 8, 26, "João")
print(p2)                              # exibe: João - 27 anos

# Verificando se é maior de idade usando método estático
print(Pessoa.e_maior_idade(18))        # True
print(Pessoa.e_maior_idade(8))         # False
