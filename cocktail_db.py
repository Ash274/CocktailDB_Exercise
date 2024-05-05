import requests
import json

# Schemas generated using: https://www.liquid-technologies.com/online-json-to-schema-converter
INGREDIENT_URL = "https://www.thecocktaildb.com/api/json/v1/1/search.php?i="
COCKTAIL_URL = "HTTPS://www.thecocktaildb.com/api/json/v1/1/search.php?s="


def search_ingredients(ingredient:str) -> requests.models.Response:
    '''Search ingredients by name'''

    return requests.get(f"{INGREDIENT_URL}{ingredient}")

def search_cocktail(drink:str) -> requests.models.Response:
    '''Search cocktails by name'''

    return requests.get(f"{COCKTAIL_URL}{drink}")
    
def get_schemas() -> dict[dict, dict]:
    '''Reads and returns the json schemas for the ingredient and cocktail schemas'''

    with open(r'json/ingredient_schema.json', 'r') as f:
        ingredient_schema = json.load(f)

    with open(r'json/cocktail_schema.json', 'r') as f:
        cocktail_schema = json.load(f)

    return {
        'ingredient': ingredient_schema, 
        'cocktail': cocktail_schema,
        }

if __name__ == '__main__':
    # Nothing is supposed to happen here
    ...