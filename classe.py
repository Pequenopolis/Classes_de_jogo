class Heroi: #Tirei o acento (como o Chat GPT sugeriu)
    def __init__(self, nome, idade, tipo) -> None:
        self.nome = nome
        self.idade = idade
        self.lista_tipo = ["Mago", "Guerreiro", "Monge", "Assassino", "Paladino", "Espadachim"]
        self.lista_ataques = {
            "Mago": "Tempestade de Mana",
            "Guerreiro": "Machadada Enfurecida",
            "Monge": "Palma Budista",
            "Assassino": "Ataque furtivo",
            "Paladino": "Benção da Luz",
            "Espadachim": "Sequência de lâminas"
        }  

        if tipo in self.lista_tipo:
            self.tipo = tipo
            self.ataque_correspondente = self.lista_ataques[tipo]
        else:
            raise Exception("Tipo Inválido")

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Tipo: {self.tipo}")
        print(f"Ataque Correspondente: {self.ataque_correspondente}")
    
    def atacar(self):
        print(f'O {self.tipo} atacou utilizando a habilidade {self.ataque_correspondente}')


Personagem = Heroi("Jonas","12","Paladino")

Personagem.exibir_informacoes()
Personagem.atacar()
