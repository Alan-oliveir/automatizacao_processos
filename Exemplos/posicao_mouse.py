import pyautogui
import time

# Pega o retorno da posição atual de x e y do mouse e passa o valor da tupla para as duas variáveis
print('Posicione o mouse')
time.sleep(3)
x, y = pyautogui.position()

# Retorna True se x e y estiverem dentro da tela
resp = pyautogui.onScreen(x, y)
print("Está dentro da tela: " + (str(resp)))

# Retorna a pposição atual do mmouse
print("Posicao atual do mouse: x = " + str(x) + " e y = " + str(y))
