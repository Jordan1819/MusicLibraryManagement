-- Music Collection Database Schema
-- Outlines architecture for music database

-- create Artist table
CREATE TABLE IF NOT EXISTS Artist (
    ArtistID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL UNIQUE
);

-- create Category table
CREATE TABLE IF NOT EXISTS Category (
    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryName TEXT NOT NULL UNIQUE
);

-- create Album table 
CREATE TABLE IF NOT EXISTS Album (
    AlbumID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL,
    Year INTEGER NOT NULL
);

-- create Song table 
CREATE TABLE IF NOT EXISTS Song (
    SongID INTEGER PRIMARY KEY AUTOINCREMENT,
    Title TEXT NOT NULL
);

-- create Plays conjoining table
CREATE TABLE IF NOT EXISTS Plays (
    SongID INTEGER NOT NULL,
    ArtistID INTEGER NOT NULL,
    PRIMARY KEY (SongID, ArtistID),
    FOREIGN KEY (SongID) REFERENCES Song(SongID) ON DELETE CASCADE,
    FOREIGN KEY (ArtistID) REFERENCES Artist(ArtistID) ON DELETE CASCADE
);

-- create IsIn conjoining table
CREATE TABLE IF NOT EXISTS IsIn (
    CategoryID INTEGER NOT NULL,
    SongID INTEGER NOT NULL,
    PRIMARY KEY (CategoryID, SongID),
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID) ON DELETE CASCADE,
    FOREIGN KEY (SongID) REFERENCES Song(SongID) ON DELETE CASCADE
);

-- create IsOn conjoining table
CREATE TABLE IF NOT EXISTS IsOn (
    SongID INTEGER NOT NULL,
    AlbumID INTEGER NOT NULL,
    PRIMARY KEY (SongID, AlbumID),
    FOREIGN KEY (SongID) REFERENCES Song(SongID) ON DELETE CASCADE,
    FOREIGN KEY (AlbumID) REFERENCES Album(AlbumID) ON DELETE CASCADE
);

-- create indexes for conjoining table fields for better query performance
CREATE INDEX IF NOT EXISTS idx_plays_artist ON Plays(ArtistID);
CREATE INDEX IF NOT EXISTS idx_plays_song ON Plays(SongID);
CREATE INDEX IF NOT EXISTS idx_isin_category ON IsIn(CategoryID);
CREATE INDEX IF NOT EXISTS idx_isin_song ON IsIn(SongID);
CREATE INDEX IF NOT EXISTS idx_ison_album ON IsOn(AlbumID);
CREATE INDEX IF NOT EXISTS idx_ison_song ON IsOn(SongID);