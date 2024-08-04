# Microservice: recipe-sift

## Introduction
`recipe-sift` is a microservice designed for sorting and filtering recipes. It has the following features:
- Sort recipes by name (ascending or descending)
- Sort recipes by preparation time (ascending)
- Filter recipes by ingredients

## Request
To make a request, write a request message to a text file named `communication.txt`. 

There are four different request messages that can be sent to this microservice:
- `"sort name 1"`: Sort recipes by name ascendingly
- `"sort name 2"`: Sort recipes by name descendingly
- `"sort time"`: Sort recipes by preparation time ascendingly
- `"filter\ningredient1, ingredient2, ingredient3"`: Filters recipes to include only those that contain the specified ingredients. The ingredients should be separated by commas.

Write one of these messages to the `communication.txt` file, the microservice will process the recipes accordingly. 

Example:
```python
with open('communication.txt', 'w') as file:
    file.write('filter\nflour, eggs')
```
The above message will filter the recipes so that only those contain the ingredients of both flour and eggs are kept.

## Response
After processing the recipes based on the request message, the microservice will save the results to a new JSON file. The name of the new file will be recorded in the communication.txt file.

Below is a simple UML for the microservice.

![UML](UML.PNG)