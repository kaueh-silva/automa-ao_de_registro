

import pandas
import pyautogui
import time

# pyautogui.click = clicar com o mouse
# pyautogui.write = escrever texto
# pyautogui.press = pressionar tecla
# pyautogui.hotkey =  combinaçao de tecla, exemplo : ctrl c
# pyautogui.scroll = descer ou subir pagina


# Passo 1 - Entrar no sistema, e abrir o navegador
pyautogui.PAUSE = 0.5

pyautogui.press("win")

pyautogui.write("Microsoft Edge")

pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

time.sleep(1.5)

# Passo 2 - Fazer Login

pyautogui.click(x=956, y=352)

pyautogui.hotkey("ctrl", "a")

pyautogui.write("kauesilva107@gmail.com")

time.sleep(0.5)

pyautogui.click(x=651, y=459)

pyautogui.hotkey("ctrl", "a")

pyautogui.write("kauechris123")

pyautogui.press("enter")


time.sleep(1)

# Passo 3 - importar a base de dados

dados = pandas.read_csv("produtos.csv")

print(dados)

# Passo 4 - Cadastrar produto
for linha in dados.index:
    # codigo
    pyautogui.click(x=657, y=234)
    codigo = str(dados.loc[linha, "codigo"])
    pyautogui.write(codigo)

    # marca
    pyautogui.press("tab")
    marca = str(dados.loc[linha, "marca"])
    pyautogui.write(marca)

    # tipo
    pyautogui.press("tab")
    tipo = str(dados.loc[linha, "tipo"])
    pyautogui.write(tipo)
    # categoria
    pyautogui.press("tab")
    categoria = str(dados.loc[linha, "categoria"])
    pyautogui.write(categoria)
    # preço_unitario
    pyautogui.press("tab")
    preco = str(dados.loc[linha, "preco_unitario"])
    pyautogui.write(preco)
    # custo
    pyautogui.press("tab")
    custo = str(dados.loc[linha, "custo"])
    pyautogui.write(custo)
    # obs
    obs = str(dados.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    # clicar em enviar
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(-5000)
    time.sleep(0.5)
    pyautogui.scroll(5000)
