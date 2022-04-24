import sqlite3
import random


def get_random_word():
    with sqlite3.connect("database.db") as db:
        cursor = db.cursor()
        cursor.execute("SELECT count(1) FROM verbs")
        count = cursor.fetchone()
        r = random.randint(1, count[0])
        cursor.execute(f"SELECT infinitive, past_simple, past_participle, translation FROM verbs WHERE rowid = {r}")
        return cursor.fetchone()


print("Print all forms separated by space:")
while True:
    word = get_random_word()
    print(word[3] + ":")
    forms = input().split()
    flag = True
    if len(forms) == 3:
        for i, j in zip(word[:3], forms):
            if i != j:
                flag = False
    else:
        flag = False
    if flag:
        print("Yes")
    else:
        print(f"No, {', '.join(word[:3])}")
