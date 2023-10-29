from tkinter import messagebox
import pyautogui
import time

# Pega o retorno da posição atual de x e y do mouse e passa o valor da tupla para as duas variáveis
print('Posicione o mouse')
time.sleep(3)
x, y = pyautogui.position()

# Retorna True se x e y estiverem dentro da tela
resp = pyautogui.onScreen(x, y)
print("Está dentro da tela: " + (str(resp)))

# Retorna a posição atual do mouse
print("Posicao atual do mouse: x = " + str(x) + " e y = " + str(y))

# Exibe a posição do mouse em uma messagebox
messagebox.showinfo(title="Posição do mouse",
                    message="Posicao atual do mouse: x = " + str(x) + " e y = " + str(y))
