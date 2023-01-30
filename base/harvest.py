import json, pyautogui as pg, time

def change_map(x,y):
    print("changing map...")
    pg.moveTo(x, y)
    pg.click()

    while True:
        image_map = pg.locateOnScreen("./Images/background.png", confidence=0.8)
        print("buscando")
        if image_map == None:
            continue
        else:
            print("cambiando...")
            time.sleep(1)
            break
            

def harvest_resource(x,y):
    print("seeking...")
    
    pg.moveTo(x,y)
    time.sleep(0.1)

    try:
        image_checked = pg.locateOnScreen("./Images/resource_1.png", confidence=0.8)

        if image_checked:
            print("None founded...")
        else:
            print("Resource founded")
            pg.click()
            time.sleep(5)
    except:
        print("picture not founded.")

def run_harvest():

    with open("data.json", "r") as file:
        data = json.load(file)

    for key in data:
        # getting current position and type of search.
        type = (data[key]["type"])
        x = (data[key]["x"])
        y = (data[key]["y"])

        if type == "map":
            change_map(x,y)
        else:
            harvest_resource(x,y)