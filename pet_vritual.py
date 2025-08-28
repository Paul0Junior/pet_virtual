class Pet:
    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie
        self.fome = 50
        self.energia = 50
    
    def brincar(self):
        if self.energia < 10:
            print("Seu pet está muito cansado para brincar!")
        elif self.energia >=10 and self.fome > 95:
            print("Seu pet está com muita fome para brincar!")
        else: 
            self.energia -= 10
            self.fome += 5
    def dormir(self):
        if self.energia >= 50:
            print("Seu pet não está cansado!")
        else: self.energia += 10
    def comer(self):
        if self.fome <= 0:
            self.fome = 0;print("Seu pet não está com fome!")
        else: self.fome -= 10

class Cachorro(Pet):
    def acao(self):
        print(f'{self.nome}: Au Au!')
class Gato(Pet):
    def acao(self):
        print(f'{self.nome}: Miau Miau!')
    def brincar(self):
        if self.energia < 10:
            print("Seu pet está muito cansado para brincar!")
        elif self.energia >=10 and self.fome > 95:
            print("Seu pet está com muita fome para brincar!")
        else: 
            self.energia -= 15
            self.fome += 8

# Programa Principal
print("Bem-vindo ao jogo do Tamagoshi!")
print("Qual o nome do seu pet?")
nome = input('Nome: ')
print("Qual a espécie dele?")
print('1. Gato')
print('2. Cachorro')
especie = input('Espécie: ')

# Definir o pet com base na escolha do usuário

if especie == '1':
    meu_pet = Gato(nome, 'Gato')
elif especie == '2':
    meu_pet = Cachorro(nome, 'Cachorro')
print(f"\nStatus inicial: {meu_pet.nome} tem {meu_pet.fome} de fome e {meu_pet.energia} de energia.")

while True:
    print(f"\nStatus: Fome: {meu_pet.fome}, Energia: {meu_pet.energia}")
    print("O que você quer fazer?")
    print("1. Brincar")
    print("2. Comer")
    print("3. Dormir")
    print("4. Sair")

    escolha = input("Digite o número de sua escolha: ")

    if escolha == '1':
        meu_pet.brincar()
        print(f'{meu_pet.nome} está brincando....')
        wait = input("Pressione Enter para continuar...")
    elif escolha == '2':
        meu_pet.comer()
        print(f'{meu_pet.nome} está comendo....')
        wait = input("Pressione Enter para continuar...")
    elif escolha == '3':
        meu_pet.dormir()
        print(f'{meu_pet.nome} está dormindo....')
        wait = input("Pressione Enter para continuar...")
    elif escolha == '4':
        print("Obrigado por jogar!")
        meu_pet.acao()
        break
    else:
        print("Escolha inválida. Tente novamente.")

