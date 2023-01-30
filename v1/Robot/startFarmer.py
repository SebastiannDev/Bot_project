from Robot.locateInScreen import get_resource, get_map
import json


def checkResource():

    with open("data.json", "r") as file:
        data = json.load(file)

    for key in data:

        tipo = data[key]["type"]
        url = str(data[key]["url"])
        print(f"Tipo: {tipo}, Imagen: {url}")
        
        if url.startswith("./Images/resource_"):
            get_resource(url)
        else:
            get_map(url)

