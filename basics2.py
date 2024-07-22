import requests
from bs4 import BeautifulSoup
url = "http://www.ibm.com"
url1 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

data  = requests.get(url).text 
data1  = requests.get(url1).text
soup = BeautifulSoup(data,"html.parser")
soup2 = BeautifulSoup(data1,"html.parser")
# for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>

#     print(link.get('href'))
#     print(link['href'])
# for link in soup.find_all('img'):# in html image is represented by the tag <img>
#     print(link)
#     print(link.get('src'))
table = soup2.find('table')
print(table)
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))