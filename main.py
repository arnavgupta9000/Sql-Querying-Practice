import sqlite3

class Query:
    
    def __init__(self):
        self.conn = sqlite3.connect('books.db')
        self.cursor = self.conn.cursor()

    def drop(self):
        # Drop existing tables if they exist
        self.cursor.execute("DROP TABLE IF EXISTS books")
        self.cursor.execute("DROP TABLE IF EXISTS authors")
        self.cursor.execute("DROP TABLE IF EXISTS publishers")
        self.conn.commit()

    def create_tables(self):
        # Create the publishers table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS publishers (
                                publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT NOT NULL)''')
        
        # Create the authors table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS authors (
                                author_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                first_name TEXT NOT NULL,
                                last_name TEXT NOT NULL)''')

        # Create the books table
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS books (
                                book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT NOT NULL,
                                genre TEXT NOT NULL,
                                author_id INTEGER,
                                publisher_id INTEGER,
                                FOREIGN KEY(author_id) REFERENCES authors(author_id),
                                FOREIGN KEY(publisher_id) REFERENCES publishers(publisher_id))''')
        self.conn.commit()

    def insert_data(self):
        # Insert sample data into publishers table
        self.cursor.executemany('''INSERT INTO publishers (name)
                                   VALUES (?)''', [
            ('Penguin Random House',),
            ('HarperCollins',),
            ('Simon & Schuster',)
        ])

        # Insert sample data into authors table
        self.cursor.executemany('''INSERT INTO authors (first_name, last_name)
                                   VALUES (?, ?)''', [
            ('George', 'Orwell'),
            ('J.K.', 'Rowling'),
            ('Stephen', 'King')
        ])

        # Insert sample data into books table
        self.cursor.executemany('''INSERT INTO books (title, genre, author_id, publisher_id)
                                   VALUES (?, ?, ?, ?)''', [
            ('1984', 'Dystopian', 1, 1),
            ('Harry Potter', 'Fantasy', 2, 2),
            ('The Shining', 'Horror', 3, 3),
            ('Animal Farm', 'Political Satire', 1, 1)
        ])
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


# Usage
query = Query()
query.drop()  # Drop existing tables
query.create_tables()  # Create the new tables
query.insert_data()  # Insert sample data


# get all books and their authors
print(query.cursor.execute('''select ''', () ).fetchall())


query.close()  # Close the connection
