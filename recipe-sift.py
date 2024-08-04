import time
import json


def read_request():
    with open('communication.txt', 'r') as file:
        request = file.readlines()
    return request


def read_json(file_name):
    """
    Function definition to read and return data from a JSON file.
    """
    with open(file_name, "r") as file:
        data = json.load(file)
    return data


def write_json(file_name, data):
    """
    Function definition to write data to a JSON file.
    """
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)


def sort_by_name(order, input_file, output_file):
    """
    Function definition to sort recipes by name in either ascending or
    descending order, and save the sorted data back to a new JSON file.
    """
    recipes = read_json(input_file)
    sorted_recipes = dict(sorted(recipes.items(), key=lambda x: x[0],
                                 reverse=(order == 2)))
    write_json(output_file, sorted_recipes)


def sort_by_time(input_file, output_file):
    """
    Function definition to sort the recipes by preparation time.
    """
    recipes = read_json(input_file)
    sorted_recipes = dict(sorted(recipes.items(),
                                 key=lambda x: int(x[1]['prep_time'])))
    write_json(output_file, sorted_recipes)


def filter_by_ingredients(ingredients, input_file, output_file):
    """
    Function to filer recipes by ingredients.
    """
    recipes = read_json(input_file)

    target_ingredients = [ingredient.strip().lower()
                          for ingredient in ingredients.split(",")]

    filtered_recipes = {}
    for name, details in recipes.items():
        ingredient_list = [ingredient['name'].lower()
                           for ingredient in details['ingredients']]

        if all(ingredient in ingredient_list
               for ingredient in target_ingredients):
            filtered_recipes[name] = details

    write_json(output_file, filtered_recipes)


def write_file_path(output_file):
    with open('communication.txt', 'w') as file:
        file.write(output_file)


# Loop to continuously check for request messages.
while True:

    time.sleep(1)

    request = read_request()

    if request:
        input_file = 'recipes.json'
        if request[0] == 'sort name 1':
            output_file = 'recipes_sorted_by_name_ascending.json'
            sort_by_name(1, input_file, output_file)
            write_file_path(output_file)

        elif request[0] == 'sort name 2':
            output_file = 'recipes_sorted_by_name_descending.json'
            sort_by_name(2, input_file, output_file)
            write_file_path(output_file)

        elif request[0] == 'sort time':
            output_file = 'recipes_sorted_by_time.json'
            sort_by_time(input_file, output_file)
            write_file_path(output_file)
                
        elif request[0] == 'filter\n':
            output_file = 'recipes_filtered_by_ingredients.json'
            filter_by_ingredients(request[1], input_file, output_file)
            write_file_path(output_file)
