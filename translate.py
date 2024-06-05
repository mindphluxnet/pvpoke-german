import requests
import json


def load_json(uri):
    try:
        response = requests.get(uri)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/pvpoke/pvpoke/master/src/data/gamemaster/pokemon.json"
    print("Loading gamemaster data ...")
    json_data = load_json(url)
    if json_data:
        print("Translating ...")
        with open("german.json") as f:
            translation = json.load(f)

            for pokemon in json_data:
                dex = str(pokemon["dex"])
                if dex in translation:
                    translated_name = translation[dex]
                    name_parts = pokemon["speciesName"].split(" ", 1)
                    name_parts[0] = translated_name
                    pokemon["speciesName"] = " ".join(name_parts)

    print("Writing out pokemon.json ...")
    with open("pokemon.json", mode="x") as f:
        f.write(json.dumps(json_data, indent=4))

