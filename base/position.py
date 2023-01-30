import keyboard, pyautogui, json

def capture(type):
    print("capturando posision...")

    # caputre (x,y) current position cursor
    x, y = pyautogui.position()

    # open file json and load the data.
    try:
        with open("data.json", "r") as file:
            loadedData = json.load(file)
    except:
        loadedData = []

    # load previous data and concat with new info
    if len(loadedData) == 0:
        loadedData = {0:{"type": type, "x": x, "y": y}}
    else:
        index = len(loadedData)
        loadedData[index] = {"type": type, "x": x, "y": y}

    # save in json
    with open("data.json", "w") as file:
        json.dump(loadedData, file)
    print("datos guardados...")


def capture_position():
    pos = True

    print("Para capturar la cordenada oprima '}'")
    print("Para capturar un mapa oprima '-'")
    print("Para terminar de capturar oprima 'q'")

    while pos:

        if keyboard.is_pressed('q'):
            pos = False
            print("Adios...")
            break
        elif keyboard.is_pressed('}'):
            capture("resource")
            break
        elif keyboard.is_pressed('-'):
            capture("map")
            break
