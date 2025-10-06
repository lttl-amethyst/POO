# class Livro:
#     def __init__(self, titulo, autor):
#         self.titulo = titulo
#         self.autor = autor 
    
#     def exibir_dados(self):
#         print(f"Título: {self.titulo}, Autor: {self.autor}")

# class Usuario:
#     def __init__(self, nome, codigo):
#         self.nome = nome
#         self.codigo = codigo 
    
#     def exibir_dados(self):
#         print(f"Nome: {self.nome}, Código: {self.codigo}")
        
# from projetopoo import Livro, Usuario

# livro1=Livro("Crime e Castigo", "Fiódor Dostoiévski")
# usuario1=Usuario("helo", 52108)

# livro1.exibir_dados()
# usuario1.exibir_dados()



class Jogador:
    def __init__(self, nome, pontos):
        self.nome = nome
        self.pontos = pontos 
        self.qtd_pontos = 0
    
    def exibir_dados(self):
        total = self.pontos + self.qtd_pontos
        print(f"Nome: {self.nome}, Pontos Iniciais: {self.pontos}, Pontos Adicionados: {self.qtd_pontos}, Total: {total}")
    def adicionar_pontos(self, valor):
        self.qtd_pontos += valor
    
from projetopoo import Jogador
jogador1 = Jogador("Arthur Luiz", 1200)
jogador1.adicionar_pontos(540)
jogador1.exibir_dados()
