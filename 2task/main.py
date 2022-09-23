from bs4 import BeautifulSoup

with open("Карелия_Википедия.htm", 'r', encoding='utf-8') as file:
        src = file.read()

soup = BeautifulSoup(src, "lxml")

find_theatres = soup.find_all("ul")[39].find_all("a")

for item in find_theatres:
        item_url = item.get("href")
        item_text = item.text
        print(f"{item_text}: {item_url}")
