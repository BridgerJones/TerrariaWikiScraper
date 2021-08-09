import requests
import re
from bs4 import BeautifulSoup
r = requests.get("https://terraria.fandom.com/wiki/Banners_(enemy)")
soup = BeautifulSoup(r.text, 'html.parser')
list_of_banners = soup.find_all('span', {'id': re.compile(r'_Banner')})
for banner_span in list_of_banners:
    print(banner_span['id'])
