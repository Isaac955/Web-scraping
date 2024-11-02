# 📊 Web Scraping

- Ce projet permet d'extraire et de structurer automatiquement les informations des projets présents sur mon site portfolio, pour une visualisation simplifiées. 
- Ce script collecte les informations de chaque projet, notamment le titre, la description, et les liens associés.

## 📚 Bibliothèques nécessaires : 
#### - `requests` pour l'envoi des requêtes HTTP
#### - `BeautifulSoup4` pour le parsing HTML
#### - `pandas` : pour exporter les données en fichiers Excel 

## 📂 Structure du Projet : 
#### - `scraper.py` : Script Python principal pour l’extraction des données.
#### - `portfolio.html` : Page HTML sauvegardée localement
#### - `projects.xlsx` : Fichier généré contenant les données extraites sous format Excel.

## 🖥️ Résultats et export :
Le fichier Excel généré contient les informations suivantes pour chaque projet :
- Langages : Les technologies utilisées (Python, HTML, CSS, etc.).
- Description : Un bref résumé du projet.
- Lien : Lien direct vers le projet (GitHub ou autre).
