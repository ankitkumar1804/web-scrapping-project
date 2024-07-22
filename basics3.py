import requests
import pandas as pd
from bs4 import BeautifulSoup
url = "https://en.wikipedia.org/wiki/World_population"
data  = requests.get(url).text
soup = BeautifulSoup(data,"html.parser")
tables = soup.find_all('table')
print(len(tables))
for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)
#print(tables[6].prettify())
population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])
# for row in tables[table_index].tbody.find_all("tr"):
#     col = row.find_all("td")
#     if (col != []):
#         rank = col[0].text
#         country = col[1].text
#         population = col[2].text.strip()
#         area = col[3].text.strip()
#         density = col[4].text.strip()
#         population_data = population_data._append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

# print(population_data)

# population_data_read_html = pd.read_html(str(tables[table_index]), flavor='bs4')
# print(population_data_read_html)
dataframe_list = pd.read_html(url, flavor='bs4')
print(dataframe_list[0])
print(pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0])