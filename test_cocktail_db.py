import cocktail_db
from jsonschema import validate
from jsonschema.exceptions import ValidationError
import json
import pytest

SCHEMAS = cocktail_db.get_schemas()

def test_ingredient_response():
    '''Validate response status code from ingredients API call'''
    response = cocktail_db.search_ingredients('vodka')
    assert response.status_code == 200

def test_cocktail_response():
    '''Validate response status code from cocktail API call'''
    response = cocktail_db.search_cocktail('margarita')
    assert response.status_code == 200

def test_validate_ingredient_schema():
    '''Validate the ingredient schema'''
    response = cocktail_db.search_ingredients('vodka')
    assert validate(response.json(), SCHEMAS['ingredient']) == None

def test_validate_cocktail_schema():
    '''Validate the cocktail schema'''
    response = cocktail_db.search_cocktail('Margarita')
    assert validate(response.json(), SCHEMAS['cocktail']) == None

def test_non_alcoholic_ingredient():
    '''Validate non-alcoholic ingredient ABV is null'''
    response = cocktail_db.search_ingredients('Orange Juice')
    json_data = response.json()['ingredients'][0]
    assert (
        json_data['strAlcohol'] == 'No' and
        json_data['strABV'] == None
        )   
    
def test_alcoholic_ingredient():
    '''Validate alcoholic ingredient ABV is not null'''
    response = cocktail_db.search_ingredients('rum')
    json_data = response.json()['ingredients'][0]
    assert (
        json_data['strAlcohol'] == 'Yes' and
        json_data['strABV'] != None
        )   
    
def test_non_existant_cocktail():
    '''Validate that drinks is null if a cocktail does not exist'''
    response = cocktail_db.search_cocktail('Peanut butter smoothie')
    assert response.json()['drinks'] == None

def test_non_existant_ingredient():
    '''Validate that ingredients is null if an ingredient does not exist'''
    response = cocktail_db.search_ingredients('qwerty')
    assert response.json()['ingredients'] == None

def test_cocktail_case_insensitivity():
    '''Validate cocktail name input is not case sensitive'''
    response1 = cocktail_db.search_cocktail('Margarita')
    response2 = cocktail_db.search_cocktail('MARGARITA')
    assert response1.json() == response2.json()

def test_ingredient_case_insensitivity():
    '''Validate ingredient name input is not case sensitive'''
    response1 = cocktail_db.search_ingredients('vodka')
    response2 = cocktail_db.search_ingredients('VODKA')
    assert response1.json() == response2.json()

def test_existant_cocktail():
    '''Validate that drinks is not null if a cocktail exists'''
    response = cocktail_db.search_cocktail('mojito')
    assert response.json()['drinks'] != None

def test_existant_ingredient():
    '''Validate that ingredients is not null if an ingredient exists'''
    response = cocktail_db.search_ingredients('cherry')
    assert response.json()['ingredients'] != None

def test_invalid_ingredient_schema():
    '''Validate that an incorrect record will fail against schema validation'''
    
    # Read invalid json from file, strABV is int instead of str
    with open(r'json/invalid_ingredient.json', 'r') as f:
        invalid_json = json.load(f)
    
    with pytest.raises(ValidationError):
        validate(invalid_json, SCHEMAS['ingredient']) == None
    
def test_invalid_cocktail_schema():
    '''Validate that an incorrect record will fail against schema validation'''
    
    # Read invalid json from file, strABV is int instead of str
    with open(r'json/invalid_cocktail.json', 'r') as f:
        invalid_json = json.load(f)
    
    with pytest.raises(ValidationError):
        validate(invalid_json, SCHEMAS['cocktail']) == None
    
