from bs4 import BeautifulSoup
import requests
pokemon = input("Enter Pokemon Name: ")
site = requests.get(f"https://pokemondb.net/pokedex/{pokemon}").text
soup = BeautifulSoup(site, "lxml")
stats = soup.find("div", class_="resp-scroll").text

print(stats)