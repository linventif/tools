from urllib.request import urlopen
from bs4 import BeautifulSoup

import os

workshop = []
traiter = 0

#Url de la collection a workshop dl
url = "https://steamcommunity.com/sharedfiles/filedetails/?id=2717270825"

html_code = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html_code, "lxml")

prod = soup.find("div", class_="collectionChildren")

addons = prod.findAll("div", class_="collectionItemDetails")



for addon in addons:
    print(f" - - - Nombre d'addons {len(addons)} - - - {traiter} / {len(addons)} - - - ")
    traiter += 1

    title_addon = addon.find("a", href_="")
    url = title_addon.get("href")

    html_code = urlopen(url).read().decode("utf-8")
    soup = BeautifulSoup(html_code, "lxml")
    prod = soup.find("div", class_="detailsStatRight")

    workshop.append(f' {prod} -- {title_addon.get("href")} -- {title_addon.text}')



workshop = "\n".join([str(elem) for elem in workshop])
workshop = workshop.replace("https://steamcommunity.com/sharedfiles/filedetails/?id=", "")

try:
    os.remove("workshop.txt")
    open("workshop.txt", "x")
    with open("workshop.txt", "w") as fichier:
        fichier.write(workshop)


except IOError:
    open("workshop.txt", "x")
    with open("workshop.txt", "w") as fichier:
        fichier.write(workshop)