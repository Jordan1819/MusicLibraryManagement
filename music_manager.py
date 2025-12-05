import os
from database import MusicDatabase

# MusicManager - imports MusicDatabase Module and allows the user
# to interact with the music database
class MusicManager:
    def __init__(self):
        self.db = MusicDatabase()
        self.db.connect()

        # Check if db exists - if not - initialize it
        if not os.path.exists('music.db') or os.path.getsize('music.db') == 0:
            print("Initializing Database")
            self.db.initialize_database()

    # ======== QOL & Input Handling Methods ===========

    # Clear the terminal screen
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Get user input safely
    def get_input(self, prompt: str):
        while True:
            val = input(prompt).strip()
            if val:
                return val
            else:
                print("Input cannot be empty. Try again.")

    # Get user integer input safely
    def get_int_input(self, prompt: str):
        while True:
            val = input(prompt).strip()
            try:
                return int(val)
            except ValueError:
                print("Please enter an integer.")

    # Display lists dynamically & allows the user to select a list item
    def selectable_list(self, items: list, display_field: str, id_field: str, item_type: str):
        if not items:
            print(f"\nNo {item_type}s available")
            return None
        
        print(f"\nAvailable {item_type}s:")
        # Unpack tuple & print numbered list of db rows
        for i, item in enumerate(items, 1):
            print(f"{i}. {item[display_field]}")

        # Loop until user selects a valid option
        while True:
            choice = input(f"\nSelect {item_type}s (1-{len(items)} or 0 to skip: )").strip()
            if choice == '0':
                return None
            try:
                # Convert input into an index
                idx = int(choice) - 1
                # Ensure selection is valid
                if 0 <= idx < len(items):
                    return items[idx][id_field]
                print(f"Please enter a number between 0 and {len(items)}.")
            except ValueError:
                print("Please enter a valid integer.")

    # Pause execution & wait for input
    def pause(self):
        input("\nPress Enter to Continue")

    # =================== Artist Management ====================
    
    # Display artist management menu
    def display_artist_menu(self):
        while True:
            self.clear_screen()
            print("=" * 50)
            print("Manage Artists")
            print("=" * 50)
            print("1. Create Artist")
            print("2. View All Artists")
            print("3. Update an Artist")
            print("4. Delete an Artist")
            print("5. Return to Main Menu")

            choice = self.get_input("\nChoose an option:")
            print("DEBUG: repr(choice) =", repr(choice))
            
            if choice == '1':
                self.create_artist()
            elif choice == '2':
                self.display_all_artists()
            elif choice == '3':
                self.update_artist()
            elif choice == '4':
                self.delete_artist()
            elif choice == '5':
                break
            else:
                print("\nPlease enter a valid option.")
                self.pause()

    # Create an artist db entry
    def create_artist(self):
        self.clear_screen()
        print("=" * 50)
        print("Create New Artist")
        print("=" * 50)

        name = self.get_input("Artist Name: ")

        try:
            self.db.create_artist(name)
            print(f"\n '{name}' added to your artists.")
        except Exception as e:
            print(f"\nError creating artist: {e}")
        self.pause()
    
    # View all artist entries
    def display_all_artists(self):
        self.clear_screen()
        print("=" * 50)
        print("All Artists")
        print("=" * 50)

        artists = self.db.get_all_artists()

        if not artists:
            print("No artists in your library.")
        else:
            for artist in artists:
                print(f"Name: {artist['Name']}")
                print("-" * 50)
        self.pause()

    # Update an artist entry
    def update_artist(self):
        self.clear_screen()
        print("=" * 50)
        print("Update an Artist")
        print("=" * 50)

        # Get the artist to update and the new name for said artist
        old_name = self.get_input("Enter the name of the artist to update:")
        new_name = self.get_input("Enter the new name of the artist:")

        if self.db.update_artist_by_name(old_name, new_name):
            print("Artist updated successfully")
        else:
            print("Error updating artist.")
        self.pause()

    # Delete an artist entry
    def delete_artist(self):
        self.clear_screen()
        print("=" * 50)
        print("Delete an Artist")
        print("=" * 50)

        # Get the name of the artist to delete
        name = self.get_input("Enter the name of the artist to delete (case-sensitive):")
        
        if self.db.delete_artist_by_name(name):
            print("Artist deleted successfully")
        else:
            print("Error deleting artist")
        self.pause()

    # =================== Category Management ==================

    # Display category management menu
    def display_category_menu(self):
        while True:
            self.clear_screen()
            print("=" * 50)
            print("Manage Categories")
            print("=" * 50)
            print("1. Create Category")
            print("2. View All Categories")
            print("3. Update a Category")
            print("4. Delete a Category")
            print("5. Return to Main Menu")

            choice = self.get_input("\nChoose an option:")

            if choice == '1':
                self.create_category()
            elif choice == '2':
                self.display_all_categories()
            elif choice == '3':
                self.update_category()
            elif choice == '4':
                self.delete_category()
            elif choice == '5':
                break
            else:
                print("\nPlease enter a valid option.")
                self.pause()

    # Create a new category entry
    def create_category(self):
        self.clear_screen()
        print("=" * 50)
        print("Create a New Category")
        print("=" * 50)

        name = self.get_input("Enter new category name:")

        try:
            self.db.create_category(name)
            print(f"{name} added to your categories.")
        except:
            print("Error creating category")
        self.pause()

    # Display all categores
    def display_all_categories(self):
        self.clear_screen()
        print("=" * 50)
        print("All Categories")
        print("=" * 50)

        categories = self.db.get_all_categories()

        if not categories:
            print("No categories in your library.")
        else:
            for category in categories:
                print(f"Category: {category['CategoryName']}")
                print("-" * 50)
        self.pause()

    # Update a category entry
    def update_category(self):
        self.clear_screen()
        print("=" * 50)
        print("Update a Category")
        print("=" * 50)

        old_name = self.get_input("Enter the name of the category to update:")
        new_name = self.get_input("Enter the new name for this category:")

        if self.db.update_category_by_name(old_name, new_name):
            print("Category updated successfully.")
        else:
            print("Error updating category.")
        self.pause()

    # Delete a category entry
    def delete_category(self):
        self.clear_screen()
        print("=" * 50)
        print("Delete a Category")
        print("=" * 50)

        name = self.get_input("Enter the name of the category to delete (case-sensitive):")

        if self.db.delete_category_by_name(name):
            print("Category deleted successfully")
        else:
            print("Error deleting category.")
        self.pause()

    
    # =================== Album Management =====================

    # Diplay the album management menu
    def display_album_menu(self):
        while True:
            self.clear_screen()
            print("=" * 50)
            print("Manage Albums")
            print("=" * 50)
            print("1. Create Album")
            print("2. View All Albums")
            print("3. Update an Album")
            print("4. Delete an Album")
            print("5. Return to Main Menu")

            choice = self.get_input("\nChoose an option:")

            if choice == '1':
                self.create_album()
            elif choice == '2':
                self.display_all_albums()
            elif choice == '3':
                self.update_album()
            elif choice == '4':
                self.delete_album()
            elif choice == '5':
                break
            else:
                print("\nPlease enter a valid option.")
                self.pause()

    # Insert an entry into the Album table
    def create_album(self):
        self.clear_screen()
        print("=" * 50)
        print("Create a New Album")
        print("=" * 50)

        title = self.get_input("Enter the album title:")
        year = self.get_input("Enter the album year:")

        try:
            self.db.create_album(title, year)
            print("Album created successfully")
        except:
            print("Error creating album")
        self.pause()

    # Display all albums
    def display_all_albums(self):
        self.clear_screen()
        print("=" * 50)
        print("All Albums")
        print("=" * 50)

        albums = self.db.get_all_albums()

        if not albums:
            print("No albums in your library.")
        else:
            for album in albums:
                print(f"Title: {album['Title']}, Year: {album['Year']}")
                print("-" * 50)
        self.pause()

    # Update an album
    def update_album(self):
        self.clear_screen()
        print("=" * 50)
        print("Update an Album")
        print("=" * 50)

        old_name = self.get_input("Enter the name of the album to update:")
        new_name = self.get_input("Enter the new name for this album:")
        year = self.get_input("Enter the year for this album:")

        if self.db.update_album_by_name(old_name, new_name, year):
            print("Album updated successfully.")
        else:
            print("Error updating album.")
        self.pause()
    
    # Delete an album
    def delete_album(self):
        self.clear_screen()
        print("=" * 50)
        print("Delete an Album")
        print("=" * 50)

        title = self.get_input("Enter the title of the album to delete (case-sensitive):")

        if self.db.delete_album_by_name(title):
            print("Album deleted successfully")
        else:
            print("Error deleting album.")
        self.pause()




    # ===================== Main Menu ===========================

    # Display the main menu where users can select 
    def main_menu(self):
        while True:
            self.clear_screen()
            print("=" * 50)
            print("=== Manage Your Music Library ===")
            print("=" * 50)
            print("1. Manage Artists")
            print("2. Manage Categories")
            print("3. Manage Albums")
            print("4. Manage Songs")
            print("5. Generate Reports")
            print("6. Quit")

            choice = self.get_input("\nChoose an option:")

            if choice == '1':
                self.display_artist_menu()
            elif choice == '2':
                self.display_category_menu()
            elif choice == '3':
                self.display_album_menu()
            elif choice == '4':
                self.display_song_menu()
            elif choice == '5':
                self.generate_reports()
            elif choice == '6':
                break
            else:
                print("Please enter a valid option.")
                self.pause()
                

    # ======= Class Instantiation & Application Entry Point =======

    # Start the application
    def run(self):
        try:
            self.main_menu()
        except Exception as e:
            print(f"\nError: {e}")
            self.db.close()

def main():
    instance = MusicManager()
    instance.run()

if __name__ == "__main__":
    main()