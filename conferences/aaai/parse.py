import re
from urllib.request import urlopen

from bs4 import BeautifulSoup

URL = "https://aaai.org/Awards/paper.php"


html = urlopen(URL)
soup = BeautifulSoup(html, "lxml")

content_class = soup.find("div", {"class": "content"})

contents = content_class.get_text().split("\n")

for i, content in enumerate(contents):
    cond = re.search(r"AAAI-\d{2} Outstanding Paper Award", content)
    if cond:
        print(contents[i + 1])
