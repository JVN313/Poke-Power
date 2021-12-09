from bs4 import BeautifulSoup
import requests

def ErrorCatch(pokemon, evolve):
    try:
        site = requests.get(f"https://pokemondb.net/pokedex/{pokemon}").text
        soup = BeautifulSoup(site, "lxml")
        evolve = soup.find("div", class_="infocard-list-evo").text
        return evolve

    except AttributeError:
        evolve = soup.find("em")

