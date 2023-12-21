# Projetos-desenvolvidos

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)
#Passo 1
navegador.get('https://sermilweb.eb.mil.br/login.action#bc')

#passo 2 preencher dados
navegador.find_element('xpath','//*[@id="cpf"]').send_keys(10541731920)
navegador.find_element('xpath','//*[@id="password"]').send_keys('w*r&4kFz')

#passo 3 clique
navegador.find_element('xpath', '//*[@id="login"]/div[3]/button').click()
navegador.find_element('xpath','//*[@id="menuCS"]').click()
navegador.find_element('xpath','//*[@id="navbar-default"]/ul[1]/li[2]/ul/li[1]/a').click()
#contador de tempo
time.sleep(1)
navegador.find_element('xpath','//*[@id="cs"]').click()
time.sleep(1)
navegador.find_element('xpath','//*[@id="cs"]/option[2]').click()
time.sleep(1)
navegador.find_element('xpath','//*[@id="bc"]/div[3]/form/div[4]/button').click()
