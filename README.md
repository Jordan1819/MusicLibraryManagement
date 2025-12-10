# Music Collection Manager

A terminal-based application for managing a music collection with support for Artists, Albums, Songs, and Categories.

## Application Contents

The project includes:
1. ✅ `music_manager.py` - The entry point and source code orchestrator for this application
2. ✅ `schema.sql` - SQL statements to create the database
3. ✅ `database.py` - A custom database management module where SQLite methods are implemented - imported in music_manager.py
4. ✅ `README.md` - Instructions for running the program and info about the project

## Requirements

- Python 3.6 or higher
- SQLite3 (comes with Python)

No additional packages required!

## Project Structure

```
music_manager/
├── schema.sql          # Database schema (SQL statements)
├── database.py         # Database operations module
├── music_manager.py    # Main application
├── music.db           # SQLite database (auto-generated)
└── README.md          # This file
```

## Installation & Setup

1. **Download/Clone Project Folder**
2. **Run music_manager.py**

### First Time Setup
When you run the program for the first time, it will automatically:
1. Create the `music.db` SQLite database if it doesn't already exist
2. Create all necessary tables according to the schema
3. Display the main menu

### Main Menu Options

The application provides a simple numbered menu interface:
0. **View Instructions** - View a basic breakdown of instructions and user flow
1. **Manage Artists** - Create, view, update, and delete artists
2. **Manage Categories** - Create, view, update, and delete music categories
3. **Manage Albums** - Create, view, update, and delete albums
4. **Manage Songs** - Create, view, update, delete songs, and manage their relationships
5. **Generate Reports** - Run predefined reports
6. **Exit** - Close the application

### Creating Entities

#### Creating an Artist:
1. Select "Manage Artists" → "Create Artist"
2. Enter the artist name (must be unique)
3. The system automatically assigns an ArtistID

#### Creating a Category:
1. Select "Manage Categories" → "Create Category"
2. Enter the category name (must be unique)
3. The system automatically assigns a CategoryID

#### Creating an Album:
1. Select "Manage Albums" → "Create Album"
2. Enter the album title
3. Optionally enter the release year
4. The system automatically assigns an AlbumID

#### Creating a Song:
1. Select "Manage Songs" → "Create Song"
2. Enter the song title
3. Select artists who play the song (you can add multiple)
4. Select albums the song appears on (you can add multiple)
5. Select categories for the song (you can add multiple)
6. The system automatically assigns a SongID and creates all relationships

### Managing Relationships

Songs have many-to-many relationships with Artists, Albums, and Categories. Once a song has been created, these cannot be changed.
Songs and their relationships can be deleted and recreated at any time.

### Updating and Deleting

Each entity type has Update and Delete options in its respective menu:
- **Update**: Modify the entity's properties
- **Delete**: Remove the entity (WARNING: This cascades to relationships)

### Reports

Three pre-built reports are available for generation in the 'Generate Reports' menu:

1. **Songs by Artist**: Shows all songs performed by a selected artist
2. **Artists with Albums in Year**: Lists all artists who have songs on albums from a specific year
3. **Albums with Songs in Category**: Shows albums containing songs in a selected category

## Database Schema

The application implements the following ER diagram:

- **Artist** (ArtistID, Name)
- **Category** (CategoryID, CategoryName)
- **Album** (AlbumID, Title, Year)
- **Song** (SongID, Title)
- **Plays** (SongID, ArtistID) - Links artists to songs
- **IsIn** (CategoryID, SongID) - Links categories to songs
- **IsOn** (SongID, AlbumID) - Links songs to albums

## Important Notes

- **IDs are automatic**: You never need to manually enter, view, or manage IDs
- **Names by default**: When creating relationships, you select entities by name, not ID
- **Cascade deletion**: Deleting an entity removes all its relationships
- **Unique constraints**: Artist names and Category names must be unique
- **Many-to-many**: Songs can have multiple artists, be on multiple albums, and belong to multiple categories

## Example Workflow

1. Create some artists: "The Beatles", "Queen", "Pink Floyd"
2. Create some categories: "Rock", "Pop", "Progressive"
3. Create some albums: "Abbey Road" (1969), "A Night at the Opera" (1975)
4. Create songs and link them:
   - "Come Together" → Artist: The Beatles, Album: Abbey Road, Category: Rock
   - "Bohemian Rhapsody" → Artist: Queen, Album: A Night at the Opera, Category: Rock

## License

This project is for educational purposes.