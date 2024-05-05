# Cocktail Exercise: https://github.com/Terri14/Cocktail

# Test Cases:
1. test_ingredient_response: Test for a status code 200 from ingredient search api call
2. test_cocktail_response; Test for a status code 200 from cocktail search api call
3. test_validate_ingredient_schema: Validate json from ingredient response 
4. test_validate_cocktail_schema: Validate json from cocktail response 
5. test_non_alcoholic_ingredient: Validate Alcohol is No and ABV is null for a non-alcoholic beverage
6. test_alcoholic_ingredient: Validate Alcohol is Yes and ABV is not null for an alcoholic beverage
7. test_non_existant_cocktail: Validate that the response json is null if a cocktail does not exist
8. test_non_existant_ingredient: Validate that the response json is null if an ingredient does not exist
9. test_cocktail_case_insensitivity: Validate that the response is the same regardless of the case of cocktail name input 
10. test_ingredient_case_insensitivity: Validate that the response is the same regardless of the case of ingredient name input 
11. test_existant_cocktail: Validate that response is not null if a cocktail exists
12. test_existant_ingredient: Validate that response is not null if an ingredient exists
13. test_invalid_ingredient_schema: Validate that an invalid ingredient response fails schema validation and raises an exception
14. test_invalid_cocktail_schema: Validate that an invalid cocktail response fails schema validation and raises an exception

# Non-functional tests:

1. Load test - Determine how the application will handle an average load
2. Stress test - Determine how the application will handle an increased load
3. Spike test - Determine how the application will handle sharp spikes in load
4. Soak test - Determine how the application will handle an increased load over an extended period of time

- Non-functional tests could be automated using k6: https://k6.io/ 

# Execution instructions:

Scripts were written using Python 3.12.3, in addition the following libraries are needed:
- jsonschema 4.22.0
- pytest 8.2.0
- requests 2.31.0

Libraries can be installed by running the following lines via cmd:
- pip install jsonschema==4.22.0
- pip install pytest==8.2.0
- pip install requests==2.31.0

A full list of all libraries installed can be found in installed_libraries.txt

The automated tests can be run via cmd, from the Cocktail_DB directory run the following command:
- pytest test_cocktail_db.py --verbose

Script output should look like below:
![Output](https://github.com/Ash274/CocktailDB_Exercise/blob/master/images/cmd_output.PNG)



