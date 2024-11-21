import pyautogui
from time import sleep

# 1 - clicar e digitar meu usuário
pyautogui.click(993, 541, duration=2)
pyautogui.write('jessica')
# 2 - clicar e digitar minha senha
pyautogui.click(977, 567, duration=2)
pyautogui.write('123456')
# 3 - clicar em "Entrar"
pyautogui.click(870, 595, duration=2)

# 4 - extrair cada produto
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        produto, quantidade, preco = linha.strip().split(',')  # Extrai os dados e remove espaços em branco
        # 1 - clicar e digitar o produto
        pyautogui.click(678, 527, duration=2)
        pyautogui.write(produto)
        # 2 - clicar e digitar a quantidade
        pyautogui.click(673, 555, duration=2)
        pyautogui.write(quantidade)
        # 3 - clicar e digitar o preço
        pyautogui.click(674, 581, duration=2)
        pyautogui.write(preco)
        # 4 - clicar em registrar
        pyautogui.click(593, 740, duration=1)
        sleep(1)  # Esperar um pouco antes de registrar o próximo produto
