import pyautogui

# Configurar um tempo entre as ações
pyautogui.PAUSE = 2.5

# Automatizar o meu teclado
# Utilizar funções capazes de abrir o Paint
pyautogui.hotkey("win","r")
pyautogui.write("mspaint")
pyautogui.press("enter")

# Mova o mouse para a posição e clique(seleciona o lápis)
x,y =(300,125)
pyautogui.click(x,y)

pyautogui.moveTo(390,315)
pyautogui.PAUSE = 2.0

distance = 400
while distance > 0:
    # Movendo mouse para a direita
    pyautogui.dragRel(distance,0,duration=0.5)
    distance -= 25
    # Move o mouse para baixo
    pyautogui.dragRel(0,distance,duration=0.5)
    # Move o mouse para a esquerda
    pyautogui.dragRel(-distance,0,duration = 0.5)
    distance -=25
    pyautogui.dragRel(0,-distance,duration = 0.5)