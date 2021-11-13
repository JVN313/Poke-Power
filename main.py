from bs4 import BeautifulSoup
from fpdf import FPDF
import requests

pokemon = input("Enter Pokemon Name: ")
def poke_stat_getter(pokemon):
    site = requests.get(f"https://pokemondb.net/pokedex/{pokemon}").text
    soup = BeautifulSoup(site, "lxml")
    stats = soup.find("div", class_="resp-scroll").text
    #stat_list = stats.split()
    return str(stats)

def poke_image_getter(pokemon):
     r = requests.get(f"https://img.pokemondb.net/artwork/{pokemon}.jpg")
     image_open= open(f"{pokemon}.jpg", "wb")
     image_open.write(r.content)
     image_open.close()

print(poke_stat_getter(pokemon))
poke_image_getter(pokemon)


pdf = FPDF("P", "mm", "Letter")
pdf.add_page()
pdf.image(f"{pokemon}.jpg")
pdf.set_font("helvetica", "", 16)
pdf.cell(40, 30, poke_stat_getter(pokemon))
pdf.output(f"{pokemon}.pdf")