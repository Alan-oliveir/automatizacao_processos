import pyautogui
import time
import cv2

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.hotkey("win", "r")
pyautogui.typewrite("https://forms.gle/otsFeQsiKjmhdnqC8 \n")

# espera 5 segundos para a página carregar
time.sleep(5)


# abre o arquivo csv contendo os dados dos membros da biblioteca
# with open("/Exemplos/files/membros_biblioteca.csv") as f:
with open("D:/Arquivos/GitHub/Automatizacao_Processos/Exemplos/files/membros_biblioteca.csv") as f:
    # pular a primeira linha do arquivo
    next(f)

    # para cada linha do arquivo csv:
    for line in f:
        # extrai os dados dos membros: nome, e-mail e telefone
        line = line.strip()
        line = line.split(";")

        # imprime na tela os dados dos membros que foi cadastrado
        print('Dados:', line)
        name = line[0]
        email = line[1]
        phone = line[2]

        # localizar na tela a imagem do campo "Nome", encontrar sua resposta e clicar nela
        pyautogui.locateCenterOnScreen(
            "Exemplos/files/nome.png", confidence=0.8)
        pyautogui.click(pyautogui.locateCenterOnScreen(
            "Exemplos/files/resposta.png", confidence=0.8), duration=1)
        # Digita o nome do membro no campo "Resposta"
        pyautogui.typewrite(name, interval=0.25)

        # localizar na tela a imagem do campo e-mail e clicar nela
        pyautogui.locateCenterOnScreen(
            "Exemplos/files/email.png", confidence=0.8)
        pyautogui.click(pyautogui.locateCenterOnScreen(
            "Exemplos/files/resposta.png", confidence=0.8), duration=1)
        pyautogui.typewrite(email, interval=0.25)

        # localizar na tela a imagem do campo telefone e clicar nela
        pyautogui.locateCenterOnScreen(
            "Exemplos/files/telefone.png", confidence=0.8)
        pyautogui.click(pyautogui.locateCenterOnScreen(
            "Exemplos/files/resposta.png", confidence=0.8), duration=1)
        pyautogui.typewrite(phone, interval=0.25)

        # tira uma captura de tela do formulário preenchido e salva com nome "cadastro_{nome}.png"
        pyautogui.screenshot(f"cadastro_{name}.png")

        # clica no botão enviar
        pyautogui.click(pyautogui.locateCenterOnScreen(
            "Exemplos/files/enviar.png", confidence=0.8), duration=1)

        # espera 3 segundos
        time.sleep(3)

        # clica no botão "outro cadastro"
        pyautogui.click(pyautogui.locateCenterOnScreen(
            "Exemplos/files/outrocadastro.png", confidence=0.8), duration=1)


# exibe uma mensagem de alerta, informando que o programa foi finalizado com sucesso
pyautogui.alert(text="Programa finalizado com sucesso",
                title="Aviso do sistema", button="OK")
