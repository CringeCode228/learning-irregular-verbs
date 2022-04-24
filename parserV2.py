import requests
from bs4 import BeautifulSoup
import sqlite3


with sqlite3.connect("database.db") as db:
    cursor = db.cursor()
    cursor.execute("DELETE FROM verbs")

    url = "https://engblog.ru/table-of-irregular-verbs"
    page = requests.get(url)
    parser = BeautifulSoup(page.text, "html.parser")
    soup = parser.find_all("td")

    for tag_id in range(0, len(soup), 4):
        cursor.execute(f"INSERT INTO verbs (infinitive, past_simple, past_participle, translation) VALUES "
                       f"('{soup[tag_id].text}', '{soup[tag_id + 1].text}', '{soup[tag_id + 2].text}', "
                       f"'{soup[tag_id + 3].text}');")
    db.commit()
