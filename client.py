import json
import time


def display_recipes(file_name):
    with open(file_name, "r") as file:
        recipes = json.load(file)
        
    if not recipes:
        print("Note:")
        print("    No recipe contains all of these ingredients!")
        print(f"    The {file_name} is empty")
    
    for name, details in recipes.items():
        print(f"Name: {name}")
        print("• Ingredients:")
        for i in details["ingredients"]:
            print(f"  {i["name"]}, {i["quantity"]}")
        print("• Instructions:")
        print(f"  {details["instructions"]}")
        print("• Preparation Time:")
        print(f"  {details["prep_time"]}")
        print()



choice = input(
'''
Please enter your choice:

1. Sort by recipe name
2. Sort by preparation time
3. Filter by ingredients
'''
)

# If sort by recipe name
if choice == '1':
    order = input(
'''How would you like to sort the data?

1. Ascending
2. Descending
''')
    if order == '1':
        with open('communication.txt', 'w') as file:
            file.write(f'sort name {order}')
    elif order == '2':
        with open('communication.txt', 'w') as file:
            file.write(f'sort name {2}')

# If sort by preparation time
elif choice == '2':
    with open('communication.txt', 'w') as file:
        file.write('sort time')

# If filter by ingredients
elif choice == '3':
    ingredients = input("Enter the ingredient(s) you want to filter by, "
                            "separated by commas: ")

    with open('communication.txt', 'w') as file:
        file.write(f'filter\n{ingredients}')

print("Sending a request ...")

while True:
    with open('communication.txt', 'r') as file:
        response = file.read()
        if response.strip().endswith('.json'):
            print(f"The sorted recipes are stored in the {response}")
            display_recipes(response)
            break