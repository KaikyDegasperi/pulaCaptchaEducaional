"""
Script de Automação - Emissão e Validação de Certidão de Embargos em Site Governamental

Este script utiliza Selenium para automatizar a emissão e validação de certidão de embargos em um site governamental.

Requisitos:
1. Python 3.x instalado
2. Bibliotecas Python necessárias:
    - selenium
    - pandas

Configuração:
1. Certifique-se de ter o WebDriver do Chrome instalado.
2. Substitua "caminho/para/chromedriver" pelo caminho real do chromedriver.exe.
3. Certifique-se de ter um arquivo Excel com as colunas 'cpf_cnpj', 'nome_razao_social' e 'numero_certidao'.

Instalação de bibliotecas necessárias:
    pip install selenium pandas

Uso:
1. Coloque o caminho do arquivo Excel no script (variável 'caminho_excel').
2. Execute o script: python nome_do_script.py
3. O script abrirá um navegador, preencherá o formulário para cada conjunto de dados do Excel e validará a certidão.

Avisos:
- Certifique-se de cumprir os Termos de Serviço do site ao qual você está automatizando.
- O uso de automação em sites pode estar sujeito a restrições legais e políticas do site.
- Este script é fornecido apenas para fins educacionais e de demonstração.

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

# Configurações do WebDriver (certifique-se de ter o WebDriver do Chrome)
chrome_path = "caminho/para/chromedriver"  # Substitua pelo caminho real do chromedriver.exe
driver = webdriver.Chrome(chrome_path)


# Função para acessar a primeira página
def acessar_pagina_inicial():
    driver.get("https://www.go.gov.br/servicos/servico-id/1148")

    # Clicar no botão "Acessar"
    driver.find_element(By.CLASS_NAME , "nav-acessar").click()


# Função para preencher o formulário na segunda página
def preencher_formulario_e_emitir_certidao(dados):
    # Esperar até que a página esteja completamente carregada
    time.sleep(3)

    # Preencher os campos do formulário com dados do Excel
    cpf_cnpj = dados['cpf_cnpj']
    nome_razao_social = dados['nome_razao_social']

    # Preencher os campos no formulário
    driver.find_element(By.NAME , "cgc").send_keys(cpf_cnpj)
    driver.find_element(By.NAME , "razaoSocial").send_keys(nome_razao_social)

    # Clicar no botão "Enviar"
    driver.find_element(By.ID , "ok").click()

    # Esperar um pouco antes de prosseguir para a próxima etapa
    time.sleep(3)


# Função para acessar a segunda página e validar a certidão
def validar_certidao(numero_certidao):
    # Acessar a URL da segunda página
    driver.get("https://www.go.gov.br/servicos-digitais/semad/obter-certidao-de-embargos/selecionar-opcao")

    # Preencher o número da certidão no formulário
    driver.find_element(By.NAME , "num_cnpfcnpj").send_keys(numero_certidao)

    # Clicar no botão "Pesquisar"
    driver.find_element(By.CSS_SELECTOR , 'input[value="Pesquisar"]').click()

    # Aguardar a validação ou realizar outras ações conforme necessário
    # ...


# Ler os dados do Excel
caminho_excel = 'caminho/para/seu/arquivo.xlsx'
dados_excel = pd.read_excel(caminho_excel)

# Executar as ações
acessar_pagina_inicial()

for indice , linha in dados_excel.iterrows():
    preencher_formulario_e_emitir_certidao(linha)
    validar_certidao(linha['numero_certidao'])

# Fechar o navegador no final
driver.quit()
