from bs4 import BeautifulSoup
from fpdf import FPDF
import requests
import os

pokemon = input("Enter Pokemon Name: ").lower()
    #TODO format varible strings for pdf text 
def poke_stat_getter(pokemon):
    global evolution, poke_name
    site = requests.get(f"https://pokemondb.net/pokedex/{pokemon}").text
    soup = BeautifulSoup(site, "lxml")
    stats = soup.find("div", class_="resp-scroll").text
    
    try:
        evolution = soup.find("div", class_="infocard-list-evo").text
    except AttributeError:
        evolution = soup.find("em").text + " Does Not Evolve"
    
    poke_name = soup.find("h1").text
    #full_stats = str(stats) + str(evolution)
    return str(stats)

def poke_image_getter(pokemon):
     r = requests.get(f"https://img.pokemondb.net/artwork/{pokemon}.jpg")
     image_open= open(f"{pokemon}.jpg", "wb")
     image_open.write(r.content)
     image_open.close()

    #TODO format pdf text
def poke_pdf(pokemon):
    pdf = FPDF("P", "mm", "Letter")
    pdf.add_page()
    pdf.set_font("helvetica", "", 55)
    pdf.cell(0, 30, poke_name, ln=True, align="C")
    pdf.image(f"{pokemon}.jpg", x=55)
    pdf.set_font("helvetica", "", 16)
    pdf.cell(1000, 20, poke_stat_getter(pokemon), ln=True)
    pdf.cell(0, 20, evolution, ln=True, align="C")
    pdf.output(f"Pokemon-Files/{pokemon}.pdf")
    os.remove(f"{pokemon}.jpg")


print(poke_stat_getter(pokemon))
poke_image_getter(pokemon)
poke_pdf(pokemon)