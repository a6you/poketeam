import requests
import requests_cache
import html


while True:
    pokemon = input('Enter your Pokémon (or q to quit): ')
    if pokemon == 'q':
        break
    pokemon_name = html.escape(pokemon).lower()
    pokemon_name = '-'.join(pokemon_name.split(' '))
    requests_cache.install_cache('demo_cache')
    request = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    if request.status_code != 200:
        print("Sorry, we couldn't get information on that Pokemon.")
    else:
        pokemon_types = request.json()['types']

        if len(pokemon_types) == 1:
            type_name = pokemon_types[0]['type']['name']
            damage_relations = requests.get(f'https://pokeapi.co/api/v2/type/{type_name}').json()['damage_relations']
            weak = set(i['name'] for i in damage_relations['double_damage_from'])
            immune = set(i['name'] for i in damage_relations['no_damage_from'])
            resistant = set(i['name'] for i in damage_relations['half_damage_from'])
        elif len(pokemon_types) == 2:
            primary_type_name = pokemon_types[0]['type']['name']
            secondary_type_name = pokemon_types[1]['type']['name']

            damage_relations_1 = requests.get(f'https://pokeapi.co/api/v2/type/{primary_type_name}').json()['damage_relations']
            weak_1 = set(i['name'] for i in damage_relations_1['double_damage_from'])
            immune_1 = set(i['name'] for i in damage_relations_1['no_damage_from'])
            resistant_1 = set(i['name'] for i in damage_relations_1['half_damage_from'])

            damage_relations_2 = requests.get(f'https://pokeapi.co/api/v2/type/{secondary_type_name}').json()['damage_relations']
            weak_2 = set(i['name'] for i in damage_relations_2['double_damage_from'])
            immune_2 = set(i['name'] for i in damage_relations_2['no_damage_from'])
            resistant_2 = set(i['name'] for i in damage_relations_2['half_damage_from'])

            immune = immune_1.union(immune_2)

            # T1.weak n T2.weak -> x4 weak
            # T1.weak n T2.neutral -> x2 weak
            # T1.neutral n T2.weak -> x2 weak
            weak = (weak_1.intersection(weak_2)).union(weak_1.difference(resistant_2)).union(weak_2.difference(resistant_1))
            weak = weak.difference(immune)

            # T1.resistant n T2.resistant -> x4 resistant
            # T1.resistant n T2.neutral -> x2 resistant
            # T1.neutral n T2.resistant -> x2 resistant
            resistant = (resistant_1.intersection(resistant_2)).union(resistant_1.difference(weak_2)).union(resistant_2.difference(weak_1))
            resistant = resistant.difference(immune)

        print('(Ignoring abilities)')
        print(f"Weaknesses: {', '.join(i.title() for i in list(weak)) if weak else 'None'}")
        print(f"Immunities: {', '.join(i.title() for i in list(immune)) if immune else 'None'}")
        print(f"Resistances: {', '.join(i.title() for i in list(resistant)) if resistant else 'None'}")



