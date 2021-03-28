import csv
import datetime
import sqlite3

base = sqlite3.connect('db.sqlite3')
cursor = base.cursor()

with open("data/category.csv", "r") as data:
    for row in csv.DictReader(data):
        cursor.execute(
            "INSERT INTO api_category "
            "(id, name, slug) "
            "VALUES(?, ?, ?)",
            (row['id'], row['name'], row['slug'])
        )
        base.commit()

with open("data/comments.csv", "r") as data:
    for row in csv.DictReader(data):
        cursor.execute(
            "INSERT INTO api_comment "
            "(id, text, pub_date, author_id, review_id) "
            "VALUES(?, ?, ?, ?, ?)",
            (row['id'],  row['text'], row['pub_date'],
             row['author'], row['review_id'])
        )
        base.commit()

with open("data/genre.csv", "r") as data:
    for row in csv.DictReader(data):
        cursor.execute(
            "INSERT INTO api_genre "
            "(id, name, slug) "
            "VALUES(?, ?, ?)",
            (row['id'], row['name'], row['slug'])
        )
        base.commit()

with open("data/genre_title.csv", "r") as data:
    for row in csv.DictReader(data):
        cursor.execute(
            "INSERT INTO api_title_genre "
            "(id, title_id, genre_id) "
            "VALUES(?, ?, ?)",
            (row['id'], row['title_id'], row['genre_id'])
        )
        base.commit()

with open("data/review.csv", "r") as data:
    for row in csv.DictReader(data):
        cursor.execute(
            "INSERT INTO api_review "
            "(id, text, score, pub_date, author_id, title_id) "
            "VALUES(?, ?, ?, ?, ?, ?)",
            (row['id'], row['text'], row['score'],
             row['pub_date'], row['author'], row['title_id'])
        )
        base.commit()

with open("data/titles.csv", "r") as data:
    for row in csv.DictReader(data):
        cursor.execute(
            "INSERT INTO api_title "
            "(id, name, year, category_id) "
            "VALUES(?, ?, ?, ?)",
            (row['id'], row['name'], row['year'], row['category'])
        )
        base.commit()

with open("data/users.csv", "r") as data:
    for row in csv.DictReader(data):
        id = row['id']
        password = '12345678'
        username = row['username']
        email = row['email']
        role = row['role']
        bio = row['description']
        first_name = row['first_name']
        last_name = row['last_name']
        date_joined = datetime.datetime.now()
        if role == 'user':
            is_superuser = False
            is_staff = False
            is_active = True
        elif role == 'moderator':
            is_superuser = False
            is_staff = True
            is_active = True
        elif role == 'admin':
            is_superuser = True
            is_staff = False
            is_active = True
        cursor.execute(
            "INSERT INTO api_user "
            "(id, password, username, email, role, bio, first_name, "
            "last_name, is_superuser, is_staff, is_active, date_joined) "
            "VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (id, password, username, email, role, bio, first_name,
             last_name, is_superuser, is_staff, is_active, date_joined)
        )
        base.commit()

base.close()