import pyautogui, keyboard, time, json

counter = 0
running = True

def saveInfo(url, type):
    
    try:
        with open("data.json", "r") as file:
            loadedData = json.load(file)
    except:
        loadedData = []

    if len(loadedData) == 0:
        loadedData = {0:{"type": type, "url": url}}
    else:
        index = len(loadedData)
        loadedData[index] = {"type": type, "url": url}

    
    with open("data.json", "w") as file:
        json.dump(loadedData, file)
    print("datos guardados...")

def stop_loop():
        global running
        running = False
        print("bye")

def capture():
    global counter
    x, y = pyautogui.position()

    left = x - 25
    top = y - 25
    right = x + 25
    bottom = y + 25

    im = pyautogui.screenshot()
    im = im.crop((left, top, right, bottom))
    return im

def resource():
    global counter
    im = capture()
    
    counter += 1

    url = f'./Images/resource_{counter}.png'
    im.save(url)
    saveInfo(url, "resource")
    print(f"Se ha capturado una recurso: {url}")

def location():
    global counter
    im = capture()
    
    counter += 1

    url = f'./Images/map_{counter}.png'
    im.save(url)
    saveInfo(url, "map")
    print(f"Se ha capturado un mapa: {url}")

def close():
    global running
    running = False

def capturar_imagen():

    while running:
        if(keyboard.is_pressed('q')):
            break
        elif(keyboard.is_pressed('}')):
            time.sleep(0.5)
            resource()
        elif keyboard.is_pressed('-'):
            time.sleep(.5)
            location()
        
  