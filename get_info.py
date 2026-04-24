import requests
from bs4 import BeautifulSoup
import datetime

def get_psp_info():
    try:
        url = "https://www.psp.cz/sqw/hp.sqw?k=181" # Stránka s aktuálním programem
        response = requests.get(url)
        response.encoding = 'utf-8'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Hledáme text schůze (přizpůsobeno webu PSP)
        info_text = soup.find("h2", class_="section-title") # Toto budeme zítra ladit podle reality
        title = info_text.text.strip() if info_text else "Jednání Poslanecké sněmovny"
        
        # Čas poslední aktualizace
        now = datetime.datetime.now().strftime("%H:%M")
        
        with open("overlay.txt", "w", encoding="utf-8") as f:
            f.write(f"{title} | Aktualizováno: {now}")
            
    except Exception as e:
        with open("overlay.txt", "w", encoding="utf-8") as f:
            f.write("Jednání Poslanecké sněmovny ŽIVĚ")

if __name__ == "__main__":
    get_psp_info()
