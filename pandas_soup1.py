from bs4 import BeautifulSoup as soup
import pandas as pd

#download table and turn it into csv file

dfs = pd.read_html("https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population", header = 0)
#for df in dfs:
print(dfs[4].head())
dfs[4].to_csv('city_population.csv')