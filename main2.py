import keyboard
from base.harvest import run_harvest
from base.position import capture_position

program = True

def main():
    while program:
        showUI()

def showUI():
    print("""
    1. Iniciar Farmeo
    2. Capturar coordenada
    3. Salir
    """)

    while True:
        global program

        if keyboard.is_pressed('q'):
            program = False
            print("Adios...")
            break
        elif keyboard.is_pressed('1'):
            run_harvest()
            break
        elif keyboard.is_pressed('2'):
            capture_position()
            break
        elif keyboard.is_pressed('3'):
            program = False
            print("Adios...")
            break

main()