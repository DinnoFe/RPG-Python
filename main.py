from random import randint

lista_mobs = []

player = {
    "nome": "Dinno",
    "level": 1,
    "exp": 0,
    "exp_max": 100,
    "hp": 100,
    "hp_max": 100,
    "dano": 25,
}

def creat_monster(level):
    
    new_mob = {
        "nome": f"Monstro #{level}#",
        "level": level,
        "dano": 5 * level,
        "hp": 100 * level,
        "exp": 7 * level,
    }

    return new_mob

def gerar_mobs(n_mobs):  
    for x in range(n_mobs):
        new_mob = creat_monster(x + 1)
        lista_mobs.append(new_mob)


def exibir_mobs():
    for mob in lista_mobs:
        print(
            f"Nome: {mob['nome']} // Level: {mob['level']} // Dano: {mob['dano']} // HP: {mob['hp']} // EXP: {mob['exp']}"
        )

def atacar_mod(mob):
    mob['hp'] -= player['dano']
    atacar_player(mob)

def atacar_player(mob):
    player['dano'] -= mob['hp']


gerar_mobs(5)
# exibir_mobs()

mob_selecionado = lista_mobs[0]

print("MOB selecionado =>", mob_selecionado)
atacar_mod(mob_selecionado)

print("#MOB Atacado# ", mob_selecionado)

