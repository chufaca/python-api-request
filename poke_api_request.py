import requests

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica errores HTTP
        data = response.json()
        
        print(f"\nInformación de {pokemon_name.capitalize()}:")
        print(f"Altura: {data['height'] / 10} metros")
        print(f"Peso: {data['weight'] / 10} kg")
        print(f"Tipos: {[t['type']['name'] for t in data['types']]}")
        
    except requests.exceptions.HTTPError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error inesperado: {e}")

if __name__ == "__main__":
    pokemon = input("Ingresa el nombre de un Pokémon: ")
    get_pokemon_info(pokemon)