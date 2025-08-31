import sqlite3

conn = sqlite3.connect('database.db')

conn.execute('''CREATE TABLE transliteration_punjabi
             (content TEXT)''')
conn.execute('''CREATE TABLE transliteration_english
             (content TEXT)''')
conn.execute('''CREATE TABLE translation_punjabi
             (content TEXT)''')
conn.execute('''CREATE TABLE translation_english
             (content TEXT)''')

conn.execute("INSERT INTO transliteration_punjabi (content) VALUES ('ਪੰਜਾਬੀ ਲਿਪੀਅੰਤਰ')")
conn.execute("INSERT INTO transliteration_english (content) VALUES ('English Transliteration')")
conn.execute("INSERT INTO translation_punjabi (content) VALUES ('ਪੰਜਾਬੀ ਅਨੁਵਾਦ')")
conn.execute("INSERT INTO translation_english (content) VALUES ('English Translation')")

conn.commit()
conn.close()
