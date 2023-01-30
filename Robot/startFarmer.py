import os
from Robot.locateInScreen import locate_image

def checkResource():
    # Ejemplo de uso
    path = "./Images"
    images = [f for f in os.listdir(path) if f.endswith('.png')]

    for image in images:
        url = f"{path}/{image}"
        locate_image(url)

