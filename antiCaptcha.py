"""
Script de Automação - Quebra de Captcha usando Anticaptcha para o site do IBAMA

Este script utiliza Selenium para interagir com o site do IBAMA, preenche um captcha usando a API Anticaptcha,
e realiza uma ação no site após a resolução do captcha.

Requisitos:
1. Python 3.x instalado
2. Bibliotecas Python necessárias:
    - selenium
    - anticaptchaofficial
    - webdriver_manager

Instalação de bibliotecas necessárias:
    pip install selenium anticaptchaofficial webdriver_manager

Configuração:
1. Certifique-se de ter o WebDriver do Chrome instalado (ou ajuste o script para usar outro navegador).
2. Registre-se no Anticaptcha (https://anti-captcha.com/).
3. Obtenha uma chave da API Anticaptcha e substitua 'sua_chave_api' no script pela sua chave.

Uso:
1. Execute o script: python nome_do_script.py
2. O script abrirá um navegador, acessará o site do IBAMA, resolverá o captcha e realizará a ação no site.

Avisos:
- Certifique-se de cumprir os Termos de Serviço do site ao qual você está automatizando.
- O uso de captchas e a quebra de captchas podem estar sujeitos a restrições legais e políticas do site.
- Este script é fornecido apenas para fins educacionais e de demonstração.

"""

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from anticaptchaofficial.hcaptchaproxyless import *
import time

# Credenciais Anticaptcha
chave_api_antc = 'sua_chave_api'  # Substitua pela sua chave Anticaptcha

# Aqui vai criar o navegador que a gente vai usar
navegador = webdriver.Chrome()

link = 'https://servicos.ibama.gov.br/ctf/publico/areasembargadas/'

navegador.get(link)

# Criando a função quebra captcha
def quebrarCaptcha(nomedaclasse, chave_api, link, id, nomedobutao, tipodecaptcha):
    from anticaptchaofficial.hcaptchaproxyless import hCaptchaProxyless
    chave_captcha = navegador.find_element(By.CLASS_NAME, f'{nomedaclasse}').get_attribute('data-sitekey')

    # Criando a variável para resolver o captcha
    solver = hCaptchaProxyless()

    # Acompanhar o requerimento
    solver.set_verbose(1)

    # No arquivo chave.py, pegue a chave que você realizou o cadastro no anticaptcha
    solver.set_key(chave_api)
    # URL do site
    solver.set_website_url(link)

    # Setando o site que vamos resolver
    solver.set_website_key(chave_captcha)

    resposta = solver.solve_and_return_solution()

    if resposta != 0:
        # H-captcha-response-0vwwpzvba5x
        # Aqui colocamos nossa variável resposta para marcar o captcha
        navegador.execute_script(f"document.getElementById(f'{id}').innerHTML = '{resposta}'")
        navegador.find_element(By.ID, f'{nomedobutao}').click()
    else:
        print(solver.err_string)

    # Coloque um time para não congestionar servidor

time.sleep(100)
