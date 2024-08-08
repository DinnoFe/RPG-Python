from random import randint

lista_mobs = []

player = {
    "nome": "Dinno",
    "level": 1,
    "exp": 0,
    "exp_max": 30,
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
        "hp_max": 100 *level,
        "exp": 7 * level,
    }

    return new_mob

def gerar_mobs(n_mobs):  
    for x in range(n_mobs):
        new_mob = creat_monster(x + 1)
        lista_mobs.append(new_mob)


def exibir_mobs():
    for mob in lista_mobs:
        exibir_mobs(mob)   

def exibir_mob(mob):
        print(
            f"Nome: {mob['nome']} // Level: {mob['level']} // Dano: {mob['dano']} // HP: {mob['hp']} // EXP: {mob['exp']}"
        )

def exibir_player():
        print(
            f"Nome: {player['nome']} // Level: {player['level']} // Dano: {player['dano']} // HP: {player['hp']} // {player['hp_max']} // EXP: {player['exp']} // {player['exp_max']}"
        )

def reset_player():
     player['hp'] = player['hp_max']

def reset_mob(mob):
     mob['hp'] = mob['hp_max']


def level_up():
     if player["exp"] >= player["exp_max"]:
          player["level"] += 1
          player["exp"] = 0
          player["exp_max"] = player["exp_max"] * 2
          player['hp_max'] += 20


def iniciar_batalha(mob):
    while player['hp'] > 0 and mob['hp'] > 0:    
        atacar_mob(mob)
        atacar_player(mob)
        exibir_info_batalha(mob)

    if player['hp'] > 0:
        print(f"O {player['nome']} venceu e ganhou {mob['exp']} de EXP")
        player['exp'] += mob['exp']
        exibir_player()
    else:
        print(f"O {mob['nome']} venceu")
        exibir_mob(mob)

    level_up()
    reset_player()
    reset_mob(mob)


def atacar_mob(mob):
    mob['hp'] -= player['dano']

def atacar_player(mob):
    player['hp'] -= mob['dano']

def exibir_info_batalha(mob):
    print(f"Player: {player['hp']}/{player['hp_max']}")
    print(f"MOB {mob['nome']}: {mob['hp']}/{mob['hp_max']}")
    print("----------------------\n")

gerar_mobs(5)
# exibir_mobs()

mob_selecionado = lista_mobs[0]

iniciar_batalha(mob_selecionado)
iniciar_batalha(mob_selecionado)
iniciar_batalha(mob_selecionado)
iniciar_batalha(mob_selecionado)
iniciar_batalha(mob_selecionado)

exibir_player()

