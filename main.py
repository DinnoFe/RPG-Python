from random import randint

lista_mobs = []

def creat_monster():
    level =randint(0, 50)

    new_mob = {
        "nome": f"Monstro #{level}#",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
    }

    return new_mob

def gerar_mobs(n_mobs):  
    for x in range(n_mobs):
        new_mob = creat_monster()
        lista_mobs.append(new_mob)
def exibir_mobs():
    for mob in lista_mobs:
        print(
            f"Nome: {mob['nome']} // Level: {mob['level']} // Dano: {mob['dano']} // HP: {mob['hp']}"
        )

gerar_mobs(10)
exibir_mobs()

