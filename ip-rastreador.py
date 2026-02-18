vermelho = "\033[91m"
reset = "\033[0m"

import requests
import os
#pip install requests
os.system("clear")

asci_art = r"""
._____________  .__                        __                 
|   \______   \ |  |   ____   ____ _____ _/  |_  ___________  
|   ||     ___/ |  |  /  _ \_/ ___\\__  \\   __\/  _ \_  __ \ 
|   ||    |     |  |_(  <_> )  \___ / __ \|  | (  <_> )  | \/ 
|___||____|     |____/\____/ \___  >____  /__|  \____/|__|    
                                 \/     \/
===================================================
"""
print(vermelho + asci_art + reset)
print("ip-dress")

def localizar_ip():
    ip = input("Digite o IP: ")

    url = f"http://ip-api.com/json/{ip}"
    resposta = requests.get(url)
    dados = resposta.json()

    if dados["status"] == "success":
        print("\n===== INFORMAÇÕES DO IP =====")
        print("IP:", dados.get("query"))
        print("País:", dados.get("country"))
        print("Região:", dados.get("regionName"))
        print("Cidade:", dados.get("city"))
        print("CEP:", dados.get("zip"))
        print("Latitude:", dados.get("lat"))
        print("Longitude:", dados.get("lon"))
        print("Provedor:", dados.get("isp"))
        print("Organização:", dados.get("org"))
        print("ASN:", dados.get("as"))
        print("Fuso Horário:", dados.get("timezone"))
    else:
        print("IP inválido ou não encontrado.")

if __name__ == "__main__":
    localizar_ip()

