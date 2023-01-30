import pyautogui, keyboard, time

counter = 0
def stop_loop():
        global running
        running = False
        print("bye")

def capture():
        global counter
        x, y = pyautogui.position()

        left = x - 15
        top = y - 30
        right = x + 15
        bottom = y + 30

        im = pyautogui.screenshot()
        im = im.crop((left, top, right, bottom))

        counter += 1
        url = f'./Images/image_{counter}.png'
        im.save(url)
        print(f"Se ha capturado una imagen: {url}")
        

def close():
    global running
    running = False

running = True
def capturar_imagen():
    while running:

        if(keyboard.is_pressed('q')):
            break
        elif(keyboard.is_pressed('p')):
            time.sleep(0.5)
            capture()
  