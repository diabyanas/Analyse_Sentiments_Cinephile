from bs4 import BeautifulSoup
import requests
import re
import mysql.connector as pymysql
import pandas as pd
import csv

#r = requests.get("https://www.barreaudenice.com/annuaire/avocats/")
#print(r.status_code)


class Allo_Cine :
    """ Script de scraping de 3 différents film """

    @staticmethod
    def get_all_pages():
        urls = []
        id_film = ['fichefilm-281203','fichefilm-143692','fichefilm-228473']
        page_number = 1
        for f in id_film:
            if f == 'fichefilm-281203':
                for i in range(13) :
                    i = f"https://www.allocine.fr/film/{f}/critiques/spectateurs/?page={page_number}"
                    page_number += 1
                    urls.append(i)
                    #print(urls)
            
            elif f == 'fichefilm-228473':
                    for i in range(44) :
                        i = f"https://www.allocine.fr/film/{f}/critiques/spectateurs/?page={page_number}"
                        page_number += 1
                        urls.append(i)

            else: 
                for i in range(2) :
                    i = f"https://www.allocine.fr/film/{f}/critiques/spectateurs/?page={page_number}"
                    page_number += 1
                    urls.append(i)
        return urls

    @staticmethod
    def parse_avis(url):
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")
        #print(soup)
        avis = soup.find_all('div', class_='review-card-review-holder')
        
        #movies = pd.DataFrame(columns=["commentaires","notes"])
        liste_avis = []
        #comment = []
        #note = []
        for av in avis:
            #print(av)
            try:
                commentaires = av.find("div", class_="content-txt review-card-content").text.strip()
                #comment.append(commentaires)
            except AttributeError as e:
                commentaires = ""

            try:    
                notes = av.find("span",class_="stareval-note").text.strip()
                #note.append(notes)
            except AttributeError as e:
                notes = ""
                

            # Génération de fichier txt contenant le résultat du scraping

            chemin = "/home/diaby/IA_dev_Python/py-sql/Scraping_Allo_Cine/Brief_allocine/avis_films.txt"
            with open(chemin, "a") as f:
                f.write(f"{commentaires}\n")
                f.write(f"{notes}\n")

            # Génération de fichier csv contenant le résultat du scraping

            avs = [commentaires,notes]
            liste_avis.append(avs)
            f= open('movies.csv', 'a')
            csv_writer = csv.writer(f)
            for i in liste_avis:
                csv_writer.writerow(i)
            f.close()

            
    @staticmethod
    def parse_all_avis():
        pagees = Allo_Cine.get_all_pages()

        for page in pagees:
            Allo_Cine.parse_avis(url=page)
            print(f"on scrape {page}")
        
avis = Allo_Cine.parse_all_avis()
