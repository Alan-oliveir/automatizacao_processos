import pyautogui
import time
import cv2
import os
import logging

# obtem o diretório do arquivo
dir_path = os.path.dirname(os.path.realpath(__file__))

# Configurar o logger
logging.basicConfig(filename="application.log", level=logging.INFO,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# informa o diretório no arquivo de log
logging.info("Local do arquivo: " + dir_path)

# varável que armazena o número de registros
count_register = 0

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.hotkey("win", "r")
pyautogui.typewrite("https://forms.gle/otsFeQsiKjmhdnqC8 \n")

# espera 5 segundos para a página
time.sleep(5)

# abre o arquivo csv contendo os dados dos membros da biblioteca
with open(dir_path + "/files/membros_biblioteca.csv") as f:
    # pular a primeira linha do arquivo
    next(f)

    # para cada linha do arquivo csv:
    for line in f:
        # extrai os dados dos membros: nome, e-mail e telefone
        line = line.strip()
        line = line.split(";")

        # imprime na tela os dados dos membros que foi cadastrado
        print("Dados:", line)
        name = line[0]
        email = line[1]
        phone = line[2]

        log_dados = str("Nome: " + line[0]) + " Email: " + \
            str(line[1]) + " Telefone:" + str(line[2])

        # registra os dados no arquivo de log
        logging.info("Dados - " + log_dados)

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
        pyautogui.screenshot(f"Exemplos/screenshots/cadastro_{name}.png")

        # clica no botão enviar
        pyautogui.click(pyautogui.locateCenterOnScreen(
            "Exemplos/files/enviar.png", confidence=0.8), duration=1)

        # espera 3 segundos
        time.sleep(3)

        # clica no botão "outro cadastro"
        pyautogui.click(pyautogui.locateCenterOnScreen(
            "Exemplos/files/outrocadastro.png", confidence=0.8), duration=1)

        # atualiza o número de registros
        count_register += 1

# exibe uma mensagem de alerta, informando que o programa foi finalizado com sucesso
pyautogui.alert(text="Programa finalizado com sucesso",
                title="Aviso do sistema", button="OK")

# registra as informações no arquivo de log
logging.info("Numero de usuarios registrados: " + str(count_register))
logging.info("Programa finalizado com sucesso")
