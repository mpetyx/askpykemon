__author__ = 'mpetyx'

import pykemon
# # print pykemon.get(pokemon='bulbasaur')
# p = pykemon.get(pokemon_id=1)
# print p.attack
# print p.defense
# # print pykemon.get(move_id=15)

class Team:

    pokemons = []
    attack = 0
    defense = 0

    def __init__(self, pokemon1, pokemon2, pokemon3, pokemon4, pokemon5, pokemon6 ):

        self.pokemons.append(pykemon.get(pokemon=pokemon1))
        self.pokemons.append(pykemon.get(pokemon=pokemon2))
        self.pokemons.append(pykemon.get(pokemon=pokemon3))
        self.pokemons.append(pykemon.get(pokemon=pokemon4))
        self.pokemons.append(pykemon.get(pokemon=pokemon5))
        self.pokemons.append(pykemon.get(pokemon=pokemon6))


        self.strength()


    def find_moves(self):

        for pokemon in self.pokemons:
            pokemon.moves

    def strength(self):

        attack = 0
        defense = 0

        for pokemon in self.pokemons:
            attack = attack + pokemon.attack
            defense = defense + pokemon.defense



        self.attack = attack
        self.defense = defense

