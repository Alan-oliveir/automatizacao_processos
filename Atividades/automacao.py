import pyautogui
import time

# Aguarde alguns segundos para você abrir a janela ou guia onde deseja inserir os dados
time.sleep(5)

# Simule o preenchimento do RA (ajuste as coordenadas x e y)
# Substitua as coordenadas x e y pela posição do campo RA
pyautogui.click(x=100, y=100)
pyautogui.write("num_ra")  # Deve ser substituido por RA

# Mova para o próximo campo (por exemplo, pressionando a tecla "Tab")
pyautogui.press("tab")

# Simule o preenchimento do nome (ajuste as coordenadas x e y)
# Substitua as coordenadas x e y pela posição do campo Nome
pyautogui.click(x=100, y=200)
pyautogui.write("nome")  # Deve ser substituido pelo nome

# Mova para o próximo campo
pyautogui.press("tab")

# Simule o preenchimento da data de nascimento (ajuste as coordenadas x e y)
# Substitua as coordenadas x e y pela posição do campo Data de Nascimento
pyautogui.click(x=100, y=300)
# Deve ser substituido pela data de nascimento
pyautogui.write("data_nascimento")

# Mova para o próximo campo
pyautogui.press("tab")

# Agora você pode adicionar código adicional para clicar no botão "Salvar" ou realizar outra ação.

# Exemplo de como clicar no botão "Salvar" (ajuste para o seu caso)
# Substitua as coordenadas x e y pelas coordenadas do botão "Salvar"
pyautogui.click(x=500, y=600)

# Aguarde um momento para garantir que a ação seja concluída
time.sleep(2)

# Exiba uma mensagem de êxito ou erro com base em alguma condição (por exemplo, se a tela mudou)
if pyautogui.locateOnScreen("sucesso.png"):
    print("Registro salvo com sucesso!")
else:
    print("Erro ao salvar o registro.")
