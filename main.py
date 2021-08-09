import requests
import re
from bs4 import BeautifulSoup
r = requests.get("https://terraria.fandom.com/wiki/Banners_(enemy)")
soup = BeautifulSoup(r.text, 'html.parser')
list_of_banners = soup.find_all('span', {'id': re.compile(r'_Banner')})
x_count = 1
y_count = 1
for banner_span in list_of_banners:
    print(f"{banner_span['id']}, {x_count}, {y_count}")
    x_count += 1
    if x_count == 51:
        x_count = 1
        y_count += 1
        print("\n\n-----------------")
