import time

def print_slow(text, delay=0.05):
    """Imprime texto com efeito de digitação."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def batalha(stats, inimigo, vida_inimigo):
    print_slow(f"Um {inimigo} apareceu!")

    while stats["Vida"] > 0 and vida_inimigo > 0:
        print_slow("O que deseja fazer?")
        print("1. Atacar\n2. Defender\n3. Fugir")
        acao = input("Escolha: ")

        if acao == "1":
            dano = stats["Força"]
            vida_inimigo -= dano
            print_slow(f"Você atacou o {inimigo} e causou {dano} de dano.")
        elif acao == "2":
            print_slow("Você se defendeu e reduziu o dano do próximo ataque!")
            continue
        elif acao == "3":
            print_slow("Você fugiu da batalha!")
            return
        else:
            print_slow("Ação Inválida!")
            continue

        dano_inimigo = 10
        stats["Vida"] -= dano_inimigo
        print_slow(f"O {inimigo} atacou e causou {dano_inimigo} de dano! Sua vida: {stats['Vida']}.")

        if vida_inimigo <= 0:
            print_slow(f"Você derrotou o {inimigo}!")
            return
        if stats["Vida"] <= 0:
            print_slow("Você morreu de forma horrível.")
            exit()

def iniciar_aventura():
    print_slow("Bem-vindo ao RPG de Texto!")
    nome = input("Qual é o seu nome, aventureiro? ")
    classe = input("Escolha sua classe (Mago, Guerreiro, Ladino): ").capitalize()

    atributos = {
        "Mago": {"Vida": 50, "Mana": 100, "Força": 10, "Inteligência": 25},
        "Guerreiro": {"Vida": 100, "Mana": 30, "Força": 20, "Inteligência": 10},
        "Ladino": {"Vida": 75, "Mana": 50, "Força": 15, "Inteligência": 15}
    }

    if classe not in atributos:
        print_slow("Classe inválida! Você será um Aventureiro comum.")
        classe = "Aventureiro"
        stats = {"Vida": 60, "Mana": 40, "Força": 12, "Inteligência": 12}
    else:
        stats = atributos[classe]
        print_slow(f"Bem-vindo, {nome} o {classe}! Seus atributos são:")
        for key, value in stats.items():
            print_slow(f"{key}: {value}")

    print_slow("Sua aventura começa em uma floresta sombria.")
    batalha(stats, "Goblin", 30)

    print_slow("Você continua explorando e encontra uma uva misteriosa.")
    comer = input("Deseja comer a uva? (sim/não): ").lower()
    if comer == "sim":
        print_slow("Você comeu a uva e se sentiu revigorado! +10 de Vida.")
        stats["Vida"] += 10
    else:
        print_slow("Você não comeu a uva e seguiu em frente.")

def main():
    while True:
        iniciar_aventura()
        print_slow("A aventura terminou!")
        escolha = input("Deseja jogar novamente ou sair? (jogar/sair): ").lower()

        if escolha == "sair":
            print_slow("Obrigado por jogar! Até a próxima.")
            break
        elif escolha != "jogar":
            print_slow("Escolha inválida. Encerrando o jogo.")
            break

if __name__ == "__main__":
    main()
