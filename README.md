# 🐍 Curso de Python - DIO: Classes, Métodos e Atributos

Este repositório contém exemplos práticos desenvolvidos durante a aula do curso de Python da [DIO (Digital Innovation One)](https://www.dio.me/), abordando os principais conceitos de **POO - Programação Orientada a Objetos** em Python.

## 📚 Conteúdo da aula

### 1. ✅ Classe Abstrata com `abc`

Arquivo: `class_abstrata.py`

- Utilização do módulo `abc` para criar **interfaces/contratos** com métodos obrigatórios.
- A classe `ControleRemoto` é uma **classe abstrata**.
- A classe `ControleTV` implementa os métodos obrigatórios `ligar()` e `desligar()`.

```python
from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self): pass]

2. ✅ Métodos de Classe e Estáticos
Arquivo: metodo_class_metodo_estatico.py

Uso do @classmethod para criar instâncias a partir de outra lógica (data de nascimento).

Uso do @staticmethod para validar maioridade sem acessar atributos da classe.

O método __str__ personaliza a saída do print().

@classmethod
def criar_apartir_data_nascimento(cls, ano, mes, dia, nome):
    idade = 2025 - ano
    return cls(nome, idade)

3. ✅ Atributos de Classe vs Atributos de Instância
Arquivo: variavel_class_variavel_instancia.py

Demonstração da diferença entre:

Atributos de classe (compartilhados por todas as instâncias)

Atributos de instância (individuais por objeto)

A classe Estudante começa com a escola "DIO", depois é alterada para "Python" para mostrar como o atributo de classe muda.

python
Copiar
Editar
class Estudante:
    escola = "DIO"  # atributo de classe
