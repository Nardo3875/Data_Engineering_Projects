from bs4 import BeautifulSoup
import requests
import pandas as pd

# URL Wikipedia 
url = 'https://en.wikipedia.org/wiki/Satellite_Data_System'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

# Find the correct table 
table = soup.find('table', class_='wikitable')

# Extract data 
data_rows = []
table_rows = table.find_all('tr')
for i, row in enumerate(table_rows):
    row_data = row.find_all(['td', 'th'])
    individual_row_data = [data.text.strip() for data in row_data]

    
    if i == 0:
        columns = individual_row_data
    else:
        data_rows.append(individual_row_data)

# Create a DataFrame
df = pd.DataFrame(data_rows, columns=columns)

# Show a description of DataFrame
print(df.columns)

