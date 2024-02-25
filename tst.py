"""
Script de Automação - Emissão de Certidão no Site do TST

Este script utiliza Selenium para automatizar o processo de emissão de certidão no site do Tribunal Superior do Trabalho (TST).

Requisitos:
1. Python 3.x instalado
2. WebDriver do Chrome instalado
3. Biblioteca Python necessária:
    - selenium

Configuração:
1. Substitua "caminho/para/chromedriver" pelo caminho real do chromedriver.exe.
2. Certifique-se de baixar o webdriver adequado para o seu navegador: https://sites.google.com/chromium.org/driver/

Instalação de bibliotecas necessárias:
    pip install selenium

Uso:
1. Execute o script: python nome_do_script.py
2. O script abrirá um navegador, realizará interações na página e salvará o conteúdo após as interações.

Avisos:
- Certifique-se de cumprir os Termos de Serviço do site ao qual você está automatizando.
- O uso de automação em sites pode estar sujeito a restrições legais e políticas do site.
- Este script é fornecido apenas para fins educacionais e de demonstração.

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Caminho do webdriver (certifique-se de baixar o webdriver adequado para o seu navegador)
# Exemplo usando o ChromeDriver: https://sites.google.com/chromium.org/driver/
# URL da página
url = "https://www.tst.jus.br/certidao1"

# Configuração do Selenium
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Execute sem abrir a janela do navegador (opcional)

# Inicialize o navegador
driver = webdriver.Chrome()

try:
    # Acesse a página
    driver.get(url)

    # Aguarde até que o iframe esteja presente na página
    iframe = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )

    # Mude para o iframe
    driver.switch_to.frame(iframe)

    # Encontre e clique no botão "Emitir Certidão"
    emitir_certidao_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//input[@value="Emitir Certidão"]'))
    )
    emitir_certidao_button.click()

    # Se necessário, adicione mais interações aqui, como preenchimento de formulários, etc.

    # Aguarde até que a página carregue (substitua conforme necessário)
    WebDriverWait(driver, 10).until(
        EC.title_contains("Título da Página Após Clique")
    )

    # Salve o conteúdo da página após as interações (substitua conforme necessário)
    with open("saida.html", "w", encoding="utf-8") as arquivo_saida:
        arquivo_saida.write(driver.page_source)

finally:
    # Feche o navegador
    driver.quit()
