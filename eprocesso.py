"""
Script de Automação - Emissão de Certidão usando Selenium com Dados de CPFs de um Arquivo Excel

Este script utiliza Selenium para automatizar o preenchimento de um formulário web e emissão de certidão,
usando dados de CPFs provenientes de um arquivo Excel.

Requisitos:
1. Python 3.x instalado
2. Bibliotecas Python necessárias:
    - selenium
    - pandas
    - webdriver_manager

Instalação de bibliotecas necessárias:
    pip install selenium pandas webdriver_manager

Configuração:
1. Certifique-se de ter o WebDriver do Chrome instalado.
2. Certifique-se de ter um arquivo Excel com uma coluna 'cpf'.

Uso:
1. Coloque o caminho do arquivo Excel no script (variável 'caminho_excel').
2. Execute o script: python nome_do_script.py
3. O script abrirá um navegador, preencherá o formulário para cada CPF do arquivo Excel e emitirá certidões.

Avisos:
- Certifique-se de cumprir os Termos de Serviço do site ao qual você está automatizando.
- O uso de automação em sites pode estar sujeito a restrições legais e políticas do site.
- Este script é fornecido apenas para fins educacionais e de demonstração.

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Configurações do WebDriver (certifique-se de ter o WebDriver do Chrome)
driver = webdriver.Chrome()

# Função para preencher o formulário com CPFs da planilha Excel
def preencher_formulario_e_emitir_certidao(cpf):
    # Esperar até que a página esteja completamente carregada
    time.sleep(3)

    # Selecionar a opção de CPF no dropdown
    driver.find_element(By.NAME, "inscricaoEmpregadorDropdownList").click()
    driver.find_element(By.XPATH, "//li[text()='CPF Empregador']").click()

    # Preencher o campo de CPF
    cpf_input = driver.find_element(By.NAME, "Consulta.NrInscricao")
    cpf_input.clear()
    cpf_input.send_keys(cpf)

    # Clicar no botão "Emitir"
    driver.find_element(By.ID, "btnConsultarInscricaoCertidao").click()

    # Aguardar um pouco antes de prosseguir para a próxima iteração
    time.sleep(3)

# Ler os dados do Excel
caminho_excel = 'caminho/para/seu/arquivo.xlsx'
dados_excel = pd.read_excel(caminho_excel)

# Abrir o site
driver.get("https://eprocesso.sit.trabalho.gov.br/Certidao/Emitir")

# Iterar sobre os CPFs e emitir certidão
for indice, linha in dados_excel.iterrows():
    preencher_formulario_e_emitir_certidao(linha['cpf'])

# Fechar o navegador no final
driver.quit()
