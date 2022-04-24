import requests
from bs4 import BeautifulSoup
import sqlite3


with sqlite3.connect("database.db") as db:
    cursor = db.cursor()
    cursor.execute("DELETE FROM verbs")
    url = "https://www.ph4.ru/eng_irregular.php?ts=&al=a"

    page = requests.get(url)
    parser = BeautifulSoup(page.text, "html.parser")
    soup = parser.find_all("td")
    translations = parser.find_all("td", {"class": "silver"})

    i = 0
    for index, tag in enumerate(soup[52:-10]):
        count = tag.find_all("b")
        if len(count):
            if len(count[0].text) > 1:
                infinitive = count[0]
                past_simple = soup[index + 53].find_all("b")
                past_participle = soup[index + 54].find_all("b")
                if len(past_participle) and len(past_simple):
                    cursor.execute(f"INSERT INTO verbs (infinitive, past_simple, past_participle, translation) VALUES "
                                   f"('{infinitive.text.split()[0]}', '{past_simple[0].text.split()[0]}', "
                                   f"'{past_participle[0].text.split()[0]}', '{translations[i * 2 + 1].text}');")
                    i += 1
    db.commit()
