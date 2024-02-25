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
url = "https://sigam.ambiente.sp.gov.br/fiscalizacao/Agenda/AgendamentoAmbiental/ConsultaExterna"

# Abra a página no navegador
driver.get(url)


# Função para preencher e enviar o formulário
def preencher_e_enviar_formulario(cpf_cnpj , n_auto):
    # Preencha os campos com os dados do Excel
    campo_cpf_cnpj = driver.find_element(By.Id , "CpfCnpjAutuado")
    campo_cpf_cnpj.clear()
    campo_cpf_cnpj.send_keys(str(cpf_cnpj))

    campo_n_auto = driver.find_element(By.ID , "NumeroAia")
    campo_n_auto.clear()
    campo_n_auto.send_keys(str(n_auto))

    # Clique no botão "Consultar"
    driver.find_element(By.CSS_SELECTOR , 'input[value="Consultar"]').click()

    # Aguarde um pouco para a página carregar completamente
    time.sleep(3)


# Itere sobre as linhas do DataFrame e realize as ações
for indice , linha in dados_excel.iterrows():
    cpf_cnpj = linha['cpf']
    n_auto = linha["n_auto"]

    # Execute a função para preencher e enviar o formulário
    preencher_e_enviar_formulario(cpf_cnpj , n_auto)

    # Clique no link "Imprimir tudo"
    driver.find_element(By.CSS_SELECTOR,'.buttons-print').click()

    # Aguarde um pouco para a página de impressão carregar completamente
    time.sleep(3)

    # Volte para a página inicial para a próxima iteração
    driver.back()

# Feche o navegador no final
driver.quit()
