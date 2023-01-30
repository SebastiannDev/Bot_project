import pyautogui as pg
import time

# una vez encuentra la imagen con el recurso activo -> click
# el programa se actualiza cada 1s hasta que retorne falso
# cuando retorna falso pasa a evaluar la siguiente imagen

# pasar de mapa require una automatizacion adicional

def collect(image_pos):
    # getting atributes from image
    x, y, width, height = image_pos
    center_x, center_y = x + width / 2, y + height / 2

    # move cursos to center img and click them
    pg.moveTo(center_x, center_y)
    pg.click()
    time.sleep(1)
    
    counter += 1
    print(f'Coincidencia encontrada {counter} ')

counter = 0
def locate_image(url_img):
    global counter

    try:
        while True:
            image_pos = pg.locateOnScreen(url_img, confidence=0.8)
            collect(image_pos)
    except:
        print(f"next resource {counter}")
