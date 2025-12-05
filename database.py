import sqlite3
from typing import List

# MusicDatabase module - provides CRUD & Report methods for all entities in
# the database - designed to be imported into a manager/orchestrator
class MusicDatabase:
    def __init__(self, db_name: str = "music.db"):
        self.db_name = db_name
        self.connection = None

    # ===== DB Initialization & Connection Methods ======

    def connect(self):
        # Create new or access existing database
        self.connection = sqlite3.connect(self.db_name)
        self.connection.row_factory = sqlite3.Row
        return self.connection
    
    def close(self):
        # Close database connection
        if self.connection:
            self.connection.close()

    def initialize_database(self, schema_file: str = "schema.sql"):
        # Use schema.sql file to create db tables if not existent
        try:
            with open(schema_file, 'r') as f:
                schema = f.read()
            cursor = self.connection.cursor()
            cursor.executescript(schema)
            self.connection.commit()
            print("Database Initialized")
        except FileNotFoundError:
            print(f"Error: {schema_file} not found")
        except Exception as e:
            print(f"Error initializing: {e}")

    # ==================== Artist Methods ======================

    def create_artist(self, name: str):
        # Create a new entry in the Artist table
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Artist (Name) VALUES (?)", (name,))
        self.connection.commit()
        return cursor.lastrowid
    
    def get_all_artists(self):
        # Retrieve all artist entries
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Artist ORDER BY Name")
        return cursor.fetchall()
    
    def get_artist_by_name(self, name: str):
        # Retrieve an artist entry by name
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Artist WHERE Name = ?", (name,))
        return cursor.fetchone()
    
    def update_artist_by_name(self, old_name: str, new_name: str):
        # Update an artist entry
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Artist SET Name = ? WHERE Name = ?", (new_name, old_name))
        self.connection.commit()
        # Return true if a row was modified
        return cursor.rowcount > 0
    
    def delete_artist_by_name(self, name: str):
        # Delete an artist by name
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Artist WHERE Name = ?", (name,))
        self.connection.commit()
        # Return true if a row was deleted
        return cursor.rowcount > 0
    
    # ================= Category Methods ======================

    def create_category(self, name: str):
        # Create a new entry in the category table
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Category (CategoryName) VALUES (?)", (name,))
        self.connection.commit()
        return cursor.lastrowid
    
    def get_all_categories(self):
        # Retrieve all categories
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Category ORDER BY CategoryName")
        return cursor.fetchall()
    
    def get_category_by_name(self, name: str):
        # Retrieve a category by name
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Category WHERE CategoryName = ?", (name,))
        return cursor.fetchone
    
    def update_category_by_name(self, old_name: str, new_name: str):
        # Update a category by name
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Category SET CategoryName = ? WHERE CategoryName = ?", (new_name, old_name))
        self.connection.commit()
        return cursor.rowcount > 0
    
    def delete_category_by_name(self, name: str):
        # Delete a category by name
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Category WHERE CategoryName = ?", (name,))
        self.connection.commit()
        return cursor.rowcount > 0
    
    # =================== Album Methods =========================

    def create_album(self, title:str, year:int):
        # Create new entry in album table
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Album (Title, Year) VALUES (?, ?)", (title, year))
        self.connection.commit()
        return cursor.lastrowid
    
    def get_all_albums(self):
        # Retrieve all albums
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Album ORDER BY Title")
        return cursor.fetchall()
    
    def get_album_by_name(self, title: str):
        # Retrieve album by name
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Album WHERE Title = ?", (title,))
        return cursor.fetchone()
    
    def update_album_by_name(self, old_title: str, new_title: str, year: int):
        # Update an album by title
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Album SET Title = ?, Year = ? WHERE Title = ?", (new_title, year, old_title))
        self.connection.commit()
        return cursor.rowcount > 0
    
    def delete_album_by_name(self, title: str):
        # Delete an album by title
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Album WHERE Title = ?", (title,))
        self.connection.commit()
        return cursor.rowcount > 0

    # ================ Song Methods =========================

    def create_song(self, title: str):
        # Create new entry in song table
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Song (Title) VALUES (?)", (title,))
        self.connection.commit()
        return cursor.lastrowid
    
    def get_all_songs(self):
        # Retrieve all songs
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Song ORDER BY Title")
        return cursor.fetchall()
    
    def get_song_by_name(self, title: str):
        # Retrieve a song by name
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Song WHERE Title = ?", (title,))
        return cursor.fetchone()
    
    def update_song_by_name(self, old_title: str, new_title: str):
        # Update a song by name
        cursor = self.connection.cursor()
        cursor.execute("UPDATE Song SET Title = ? WHERE Title = ?", (new_title, old_title))
        self.connection.commit()
        return cursor.rowcount > 0
    
    def delete_song_by_name(self, title: str):
        # Delete a song by name
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Song WHERE Title = ?", (title,))
        self.connection.commit()
        return cursor.rowcount > 0
    
    # =========== Conjoining Table Methods ===================

    def add_artist_to_song(self, song_id: int, artist_id: int):
        # Add an artist to a song (Plays relationship)
        cursor = self.connection.cursor()
        cursor.execute("INSERT OR IGNORE INTO Plays (SongID, ArtistID) VALUES (?, ?)", 
                      (song_id, artist_id))
        self.connection.commit()
    
    def remove_artist_from_song(self, song_id: int, artist_id: int):
        # Remove an artist from a song
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM Plays WHERE SongID = ? AND ArtistID = ?", 
                      (song_id, artist_id))
        self.connection.commit()
    
    def get_artists_for_song(self, song_id: int) -> List[sqlite3.Row]:
        # Get all artists for a song
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT a.ArtistID, a.Name
            FROM Artist a
            JOIN Plays p ON a.ArtistID = p.ArtistID
            WHERE p.SongID = ?
            ORDER BY a.Name
        """, (song_id,))
        return cursor.fetchall()
    
    def add_category_to_song(self, song_id: int, category_id: int):
        # Add a category to a song (IsIn relationship)
        cursor = self.connection.cursor()
        cursor.execute("INSERT OR IGNORE INTO IsIn (CategoryID, SongID) VALUES (?, ?)", 
                      (category_id, song_id))
        self.connection.commit()
    
    def remove_category_from_song(self, song_id: int, category_id: int):
        # Remove a category from song entity
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM IsIn WHERE CategoryID = ? AND SongID = ?", 
                      (category_id, song_id))
        self.connection.commit()
    
    def get_categories_for_song(self, song_id: int) -> List[sqlite3.Row]:
        # Get all categories for a song
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT c.CategoryID, c.CategoryName
            FROM Category c
            JOIN IsIn i ON c.CategoryID = i.CategoryID
            WHERE i.SongID = ?
            ORDER BY c.CategoryName
        """, (song_id,))
        return cursor.fetchall()
    
    def add_song_to_album(self, song_id: int, album_id: int):
        # Add a song to an album (IsOn relationship)
        cursor = self.connection.cursor()
        cursor.execute("INSERT OR IGNORE INTO IsOn (SongID, AlbumID) VALUES (?, ?)", 
                      (song_id, album_id))
        self.connection.commit()
    
    def remove_song_from_album(self, song_id: int, album_id: int):
        # Remove a song from an album
        cursor = self.connection.cursor()
        cursor.execute("DELETE FROM IsOn WHERE SongID = ? AND AlbumID = ?", 
                      (song_id, album_id))
        self.connection.commit()
    
    def get_albums_for_song(self, song_id: int) -> List[sqlite3.Row]:
        # Get all albums for a song
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT a.AlbumID, a.Title, a.Year
            FROM Album a
            JOIN IsOn i ON a.AlbumID = i.AlbumID
            WHERE i.SongID = ?
            ORDER BY a.Title
        """, (song_id,))
        return cursor.fetchall()  

    # =============== Report Generation Methods ====================

    def see_all_songs_played_by_artist(self, name: str):
        # Retrieve all songs played by input artist
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT s.Title AS Title, a.Name AS ArtistName 
            FROM Song s
            JOIN Plays p ON s.SongID = p.SongID
            JOIN Artist a ON p.ArtistID = a.ArtisdID
            WHERE a.Name = ?
            ORDER BY a.Name       
         """, (name,))
        return cursor.fetchall()
    
    def see_all_artists_with_albums_in_year(self, year: int):
        # Retrieve all artist names w/ albums in input year
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT a.Name AS Artist
            FROM Artist a
            JOIN Plays p ON a.ArtistID = p.ArtistID
            JOIN Song s ON p.SongID = s.SongID
            JOIN IsOn io ON s.SongID = io.SongID
            JOIN Album al ON io.AlbumID = al.AlbumID
            WHERE al.Year = ?
            ORDER BY a.Name             
            """, (year,))
        return cursor.fetchall()
    
    def see_all_albums_in_category(self, category: str):
        # Find all albums w/ songs in the input category
        cursor = self.connection.cursor()
        cursor.execute("""
            SELECT DISTINCT al.Title AS AlbumTitle, a.Name AS ArtistName
            FROM Album al
            JOIN IsOn io ON al.AlbumID = io.AlbumID
            JOIN Song s ON io.SongID = s.SongID
            JOIN Plays p ON s.SongID = p.SongID
            JOIN Artist a ON p.ArtistID = a.ArtistID
            JOIN IsIn ii ON s.SongID = ii.SongID
            JOIN Category c ON ii.CategoryID = c.CategoryID
            WHERE c.CategoryName = ?
            ORDER BY al.Title   
            """, (category,))
        return cursor.fetchall()