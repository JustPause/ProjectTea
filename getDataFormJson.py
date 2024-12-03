import json

def teaList():
    with open('Front-End/public/teav2.json', 'r') as file:
        data = json.load(file)
        Green = Black = White = []
        for i in data['Green Teas']['tealist']:
            Green.append({
                "type": i['type'],
                "name": i['tea']['name'],
                "link": i['tea']['name']
            })
            # Green={"type": i['type']}
            # Green={"name": i['tea']['name']}
            
        for i in data['Black Teas']['tealist']:
            Black.append({
                "type": i['type'],
                "name": i['tea']['name'],
                "link": i['tea']['name']
            })
            # Black={"type": i['type']}
            # Black={"name": i['tea']['name']}

        for i in data['White Teas']['tealist']:
            White.append({
                "type": i['type'],
                "name": i['tea']['name'],
                "link": i['tea']['name']
            })
            # White={"type": i['type']}
            # White={"name": i['tea']['name']}
            
    return Green, Black, White

def recipeList():
    pass
