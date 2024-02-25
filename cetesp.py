"""
Script de Automação - Preenchimento de Formulário Web com Dados do Excel usando Selenium

Este script utiliza Selenium para automatizar o preenchimento de um formulário web com dados de um arquivo Excel.
Ele iterará sobre as linhas do arquivo Excel, preencherá o formulário para cada conjunto de dados e realizará ações adicionais, se necessário.

Requisitos:
1. Python 3.x instalado
2. Bibliotecas Python necessárias:
    - selenium
    - pandas
    - webdriver_manager

Instalação de bibliotecas necessárias:
    pip install selenium pandas webdriver_manager
Configuração:
1. Certifique-se de ter o WebDriver do Chrome instalado (ou ajuste o script para usar outro navegador).
2. Certifique-se de ter um arquivo Excel com as colunas 'CNPJ', 'Razão Social', 'Endereço' e 'CEP'.

Uso:
1. Coloque o caminho do arquivo Excel no script (variável 'caminho_excel').
2. Execute o script: python nome_do_script.py
3. O script abrirá um navegador, preencherá o formulário para cada linha do arquivo Excel e realizará as ações necessárias.

Avisos:
- Certifique-se de cumprir os Termos de Serviço do site ao qual você está automatizando.
- O uso de automação em sites pode estar sujeito a restrições legais e políticas do site.
- Este script é fornecido apenas para fins educacionais e de demonstração.

"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Caminho para o arquivo Excel
caminho_excel = 'caminho/para/seu/arquivo.xlsx'

# Carregue os dados do Excel usando o pandas
dados_excel = pd.read_excel(caminho_excel)

# Inicialize o driver do Selenium (certifique-se de ter o WebDriver adequado instalado)
driver = webdriver.Chrome()

# URL do site
url = "https://autenticidade.cetesb.sp.gov.br/conslInfracao.php?cgc=&razaoSocial=&endereco=&cep="

# Abra a página no navegador
driver.get(url)

# Função para preencher e enviar o formulário
def preencher_e_enviar_formulario(cnpj, razao_social, endereco, cep):
    # Preencha os campos com os dados do Excel
    campo_cnpj = driver.find_element(By.ID, "cgc")
    campo_cnpj.clear()
    campo_cnpj.send_keys(str(cnpj))

    campo_razao_social = driver.find_element(By.ID, "razaoSocial")
    campo_razao_social.clear()
    campo_razao_social.send_keys(str(razao_social))

    campo_endereco = driver.find_element(By.ID, "endereco")
    campo_endereco.clear()
    campo_endereco.send_keys(str(endereco))

    campo_cep = driver.find_element(By.ID, "cep")
    campo_cep.clear()
    campo_cep.send_keys(str(cep))

    # Clique no botão "Enviar"
    driver.find_element(By.ID, 'ok').click()

    # Aguarde um pouco para a página carregar completamente
    time.sleep(3)

# Itere sobre as linhas do DataFrame e realize as ações
for indice, linha in dados_excel.iterrows():
    cnpj = linha['CNPJ']
    razao_social = linha['Razão Social']
    endereco = linha['Endereço']
    cep = linha['CEP']

    # Execute a função para preencher e enviar o formulário
    preencher_e_enviar_formulario(cnpj, razao_social, endereco, cep)

    # Realize a lógica necessária para extrair informações da página de resultados (se houver)

    # Volte para a página inicial para a próxima iteração
    driver.get(url)

# Feche o navegador no final
driver.quit()
