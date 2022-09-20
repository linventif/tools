from urllib.request import urlopen
from bs4 import BeautifulSoup

import os

workshop = ["-- GMOD Py Workshop-Downloader CREATOR - - Created by Linventif --"]
#Url de la collection a workshop dl
url = "https://steamcommunity.com/sharedfiles/filedetails/?id=2852090999"

html_code = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html_code, "lxml")

prod = soup.find("div", class_="collectionChildren")

addons = prod.findAll("div", class_="collectionItemDetails")


for addon in addons:
    title_addon = addon.find("a", href_="")

    workshop.append(f'("{title_addon.get("href")}") -- {title_addon.text}')


workshop = "\nresource.AddWorkshop".join([str(elem) for elem in workshop])
workshop = workshop.replace("https://steamcommunity.com/sharedfiles/filedetails/?id=", "")


try:
    os.remove("workshop.lua")
    open("workshop.lua", "x")
    with open("workshop.lua", "w", encoding='utf8') as fichier:
        fichier.write(workshop)

except IOError:
    open("workshop.lua", "x")
    with open("workshop.lua", "w", encoding='utf8') as fichier:
        fichier.write(workshop)
