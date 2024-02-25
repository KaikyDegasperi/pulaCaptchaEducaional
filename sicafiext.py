"""
Script de Automação - IBAMA SICAFIEXT

Este script utiliza Selenium para automatizar a navegação em páginas do IBAMA SICAFIEXT, incluindo a quebra de CAPTCHA com o serviço Anti-Captcha.

Requisitos:
1. Python 3.x instalado
2. WebDriver do Chrome instalado
3. Bibliotecas Python necessárias:
    - selenium
    - antiCaptcha

Configuração:
1. Substitua "caminho/para/chromedriver" pelo caminho real do chromedriver.exe.
2. Substitua 'chaveDaApi' pela chave real do Anti-Captcha.

Instalação de bibliotecas necessárias:
    pip install selenium
    pip install antiCaptcha

Uso:
1. Execute o script: python nome_do_script.py
2. O script abrirá um navegador, realizará a navegação nas páginas do IBAMA SICAFIEXT e quebrará o CAPTCHA com o serviço Anti-Captcha.

Avisos:
- Certifique-se de cumprir os Termos de Serviço do site ao qual você está automatizando.
- O uso de automação em sites pode estar sujeito a restrições legais e políticas do site.
- Este script é fornecido apenas para fins educacionais e de demonstração.

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from antiCaptcha import quebrarCaptcha
import time


# Crie uma instância do driver (nesse exemplo, estou usando o Chrome)
driver = webdriver.Chrome()

# Abra a página desejada
driver.get("https://servicos.ibama.gov.br/sicafiext/")

wait = WebDriverWait(driver, 10)
# Localize o elemento pelo nome da classe
# Aguarde até que o iframe esteja presente na página
iframe = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.TAG_NAME, "iframe")))

# Agora, procure o elemento dentro do iframe
elemento = driver.find_element(By.CLASS_NAME, "style1")
elemento.click()

# Se você precisar sair do iframe, use:
driver.switch_to.default_content()
time.sleep(6)
# Aqui já estamos já na próxima página
# Aguarde até que o iframe esteja presente na página
iframe = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "corpo")))

# Primeiro link
link1_elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lnk1")))
link1_elemento.click()
# esperar carregar a página
#chama a função quebrar capthca, não consegui ir além pela falta de cpf
# A lógica da função é a seguinte, abra o inspecionar elementos do navegador aí você localiza o
# capctcha depois a div acima do iframe quebrarCaptcha(nomeDaClasseDoCaptcha,chaveDaApi,link,ClasseDoTextAreaDoCaptcha,nomeDoBotaoDePesquisa)

quebrarCaptcha('h-captcha','chaveDaApi','https://servicos.ibama.gov.br/sicafiext/','h-captcha-response-0in0ufid6aoc','btnPesquisar')
# Implemente a a lógica de inserção dos campos:


# Aguarde até que a página carregue completamente (se necessário)
# capctcha depois a div acima do iframe quebrarCaptcha(nomeDaClasseDoCaptcha,chaveDaApi,link,ClasseDoTextAreaDoCaptcha,nomeDoBotaoDePesquisa)
# Segundo link
link2_elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "lnk2")))
link2_elemento.click()

# Por favor olhe a lógica da função, não consigo ir além disso pois desconheço a forma de inserção
#Você terá que procurar os elementos pela lógica de inserção
quebrarCaptcha('h-captcha','chaveDaApi','https://servicos.ibama.gov.br/sicafiext/','h-captcha-response-0in0ufid6aoc','btnPesquisar')

time.sleep(5)
# Se você precisar sair do iframe, use:
driver.switch_to.default_content()


driver.quit()
