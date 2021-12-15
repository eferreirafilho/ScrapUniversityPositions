import requests
#Simulate browser
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36'} # This is chrome, you can set whatever browser you like
import urllib.request
import time
from bs4 import BeautifulSoup

#Email setup
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
fromaddr = "filhoedson365@gmail.com"
toaddr = "dom100n@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Concurso UFSJ"
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "am318700")

#####UEMG (Only gets first post in UEMG website)
#url = 'http://uemg.br/component/phocadownload/category/300-pss-processo-seletivo-simplificado'
##Simulate Browser
#response = requests.get(url, headers=headers)
##if response.status_code==200:
#soup = BeautifulSoup(response.text, 'html.parser')
##Search for location in website
#t=soup.find("div", {"class": "pd-subcategory"})
##Body of email
##t.contents[0] has all the contents? Wait for new listing
#body = f'Vagas Designacao UEMG: {t.text.strip()} \n'
#msg.attach(MIMEText(body, 'plain'))

#####UFSJ-OB
url = 'https://ufsj.edu.br/secop/cpd_cap_2020.php'
#response = requests.get(url, headers=headers)
response = requests.get(url,verify=False)
#if (response.status_code==200):
soup = BeautifulSoup(response.text, 'html.parser')
time.sleep(2)
t=soup.find("div", {"id": "c-f-info-right"})
body = f'Ultima Atualizacao site UFSJ-OB: {t.contents[2]} \n'
msg.attach(MIMEText(body, 'plain'))
#####UFSJ-SJ
url = 'https://ufsj.edu.br/secop/cpd_sjdr_2020.php'
#response = requests.get(url, headers=headers)
response = requests.get(url,verify=False)
#if (response.status_code==200):
soup = BeautifulSoup(response.text, 'html.parser')
time.sleep(2)
t=soup.find("div", {"id": "c-f-info-right"})
body = f'Ultima Atualizacao site UFSJ-SJ: {t.contents[2]} \n'
msg.attach(MIMEText(body, 'plain'))
#####UFSJ-Dona Lindu
url = 'https://ufsj.edu.br/secop/cpd_cco_2020.php'
#response = requests.get(url, headers=headers)
response = requests.get(url,verify=False)
#if (response.status_code==200):
soup = BeautifulSoup(response.text, 'html.parser')
time.sleep(2)
t=soup.find("div", {"id": "c-f-info-right"})
body = f'Ultima Atualizacao site UFSJ-DL: {t.contents[2]} \n'
msg.attach(MIMEText(body, 'plain'))
#####UFSJ-SL
url = 'https://ufsj.edu.br/secop/cpd_csl_2020.php'
#response = requests.get(url, headers=headers)
response = requests.get(url,verify=False)
#if (response.status_code==200):
soup = BeautifulSoup(response.text, 'html.parser')
time.sleep(2)
t=soup.find("div", {"id": "c-f-info-right"})
body = f'Ultima Atualizacao site UFSJ-SL: {t.contents[2]} \n'
msg.attach(MIMEText(body, 'plain'))

##UFOP
#url = 'http://www.concurso.ufop.br/'
#response = requests.get(url)
##if response.status_code==200:
#soup = BeautifulSoup(response.text, 'html.parser')
#time.sleep(2)
#t1=soup.find("tr", {"class": "sectiontableentry1"})
###Send last update
#body = f'Ultima Atualizacao site UFOP: {t1.text.strip()} \n'
#msg.attach(MIMEText(body, 'plain')) 

##CEFET
url = 'http://www.segep.cefetmg.br/setores/cgap/coordenacao-de-concursos/editais/'
response = requests.get(url)
#if response.status_code==200:
soup = BeautifulSoup(response.text, 'html.parser')
time.sleep(2)
t=soup.find("div", {"class": "entry-content"})
body = f'CEFET-> {t.contents[3].text.strip()} \n'
msg.attach(MIMEText(body, 'plain')) 

##PUC MG
url = 'https://www.pucminas.br/selecaodocentes/Paginas/default.aspx'
response = requests.get(url, verify=False)##This is unsafe!
#if response.status_code==200:
soup = BeautifulSoup(response.text, 'html.parser')
time.sleep(2)
t=soup.find("div", {"class": "ms-rtestate-field"})
body = f'PUC-MG-> {t.contents[0].text.strip()} \n'
msg.attach(MIMEText(body, 'plain')) 

#Send email               
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
        
server.quit()
