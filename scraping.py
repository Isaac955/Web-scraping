# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:02:45 2024

@author: ISAAC S
"""
import requests
from bs4 import BeautifulSoup



url = "https://isaacserhane.alwaysdata.net/"
response = requests.get(url)
response.enconding = response.apparent_encoding
if response.status_code == 200:
    html = response.text
    #print(html)
    #print(response)
    
    f = open("portfolio.html", "w")
    f.write(html)
    f.close()
    
    soup = BeautifulSoup(html, "html.parser")
    titre = soup.find("h1").text
    #print(titre)
    
    description = (soup.find("p")).text
    #print(description)
    
    # Description "About me" sur mon portfolio
    div_aboutme = soup.find("div", class_ ="about-caption")
    e_aboutme = div_aboutme.find_all("p")
   # for e_aboutme in e_aboutme:
       # print(e_aboutme.text)
    #Projets
    projects = soup.find_all("div", class_="portfolio-card")
    for project in projects:
        titre = project.find("h4").text
        description = project.find("p", class_="font-weight-normal").text
        lien = project.find("a")["href"]
        print(f"Languages: {titre}\nDescription: {description}\Lien: {lien}\n")

else:
    print("Erreur", response.status_code)
#print("end")

