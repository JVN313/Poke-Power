from bs4 import BeautifulSoup
import requests
pokemon = input("Enter Pokemon Name: ")
def poke_stat_getter(pokemon):
    site = requests.get(f"https://pokemondb.net/pokedex/{pokemon}").text
    soup = BeautifulSoup(site, "lxml")
    stats = soup.find("div", class_="resp-scroll").text
    #stat_list = stats.split()
    print(stats)

def poke_image_getter(pokemon):
     r = requests.get(f"https://img.pokemondb.net/artwork/{pokemon}.jpg")
     image_open= open(f"{pokemon}.jpg", "wb")
     image_open.write(r.content)
     image_open.close()

poke_stat_getter(pokemon)
poke_image_getter(pokemon)
