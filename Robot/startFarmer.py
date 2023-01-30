import os
from Robot.locateInScreen import get_resource, get_map
import re

def checkResource():
    # Ejemplo de uso
    path = "./Images"
    images = [f for f in os.listdir(path) if f.endswith('.png')]

    for image in images:
        url = f"{path}/{image}"

        pattern = "^\.\/Images\/map"

        if re.match(pattern, url):
            get_map(url)
        else:
            get_resource(url)
            

