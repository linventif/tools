from urllib.request import urlopen
from bs4 import BeautifulSoup
import os

workshop = []
traiter = 0
taille = 0
taille_total = 0.0

url = "https://steamcommunity.com/sharedfiles/filedetails/?id=2837811117"

html_code = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html_code, "lxml")

prod = soup.find("div", class_="collectionChildren")

addons = prod.findAll("div", class_="collectionItemDetails")

for addon in addons:
    print(f" - - - Nombre d'addons {len(addons)} - - - {taille_total}MB - - - {traiter} / {len(addons)} - - - {round(traiter / len(addons) * 100, 2)}% - - - ")
    traiter += 1

    title_addon = addon.find("a", href_="")

    url = title_addon.get("href")

    html_code = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html_code, "lxml")
    taille = soup.find("div", class_="detailsStatRight")
    taille = taille.text

    workshop.append(f' {taille} -- {title_addon.get("href")} -- {title_addon.text}')

    tt = taille.replace(" MB", "")
    taille_total = taille_total + float(tt)
    taille_total = round(taille_total,2)

print(f" - - - Nombre d'addons {len(addons)} - - - {taille_total}MB - - - {traiter} / {len(addons)} - - - {round(traiter/len(addons)*100,2)}% - - - ")

workshop.append(f" - - - Nombre d'addons {len(addons)} - - - {taille_total}MB - - - {traiter} / {len(addons)} - - - {round(traiter / len(addons) * 100, 2)}% - - - ")
workshop = "\n".join([str(elem) for elem in workshop])
workshop = workshop.replace("https://steamcommunity.com/sharedfiles/filedetails/?id=", "")

try:
    os.remove("workshop.txt")
    open("workshop.txt", "x")
    with open("workshop.txt", "w", encoding='utf8') as fichier:
        fichier.write(workshop)


except IOError:
    open("workshop.txt", "x")
    with open("workshop.txt", "w", encoding='utf8') as fichier:
        fichier.write(workshop)

