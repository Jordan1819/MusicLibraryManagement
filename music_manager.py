import os
from database import MusicDatabase

# MusicManager - imports MusicDatabase Module and allows the user
# to interact with the music database
class MusicManager:
    def __init__(self):
        self.db = MusicDatabase()
        self.db.connect()

        # Check if db exists - if not - initialize it
        if not os.path.exists('music.db'):
            print("Initializing Database")
            self.db.initialize_database()

    # ======== Terminal Interactivity & Input Methods ===========

    # Clear the terminal screen
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    # Get user input safely
    def get_input(self, prompt: str, allow_empty: bool = False):
        while True:
            val = input(prompt).strip()
            if val or allow_empty:
                return val
            print("Input cannot be empty. Try again.")

    # Get user integer input safely
    def get_int_input(self, prompt: str, allow_empty: bool = False):
        while True:
            val = input(prompt).strip()
            if not val and allow_empty:
                return None
            try:
                return int(val)
            except ValueError:
                print("Please enter an integer.")

    # Display a list that allows the user to select an item
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

    # =================== Artist Management ================
    
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

            choice = self.get_input()

            if choice == '1':
                self.create_artist()
            elif choice == '2':
                self.view_all_artists()
            elif choice == '3':
                self.update_artist()
            elif choice == '4':
                self.delete_artist()
            elif choice == '5':
                break # Exit loop
            else:
                print("Please enter a valid option.")
                self.pause()

    # Create an artist db entry
    def create_artist(self):
        self.clear_screen()
        print("=" * 50)
        print("Create New Artist")
        print("=" * 50)

        name = self.get_input("Artist Name: ")

        try:
            artist_id = self.db.create_artist(name)
            print(f"\n '{name}' added to your artists. (ID#: {artist_id})")
        except Exception as e:
            print(f"\nError creating artist: {e}")
        self.pause()


    # ================ Main Menu =========================

    # Display the main menu where users can select 
    def main_menu(self):
        while True:
            self.clear_screen()
            print("=" * 50)
            print("Manage You Music Library - Select an Option")
            print("=" * 50)
            print("1. Manage Artists")
            print("2. Manage Categories")
            print("3. Manage Albums")
            print("4. Manage Songs")
            print("5. Generate Reports")
            print("6. Quit")

            choice = self.get_input("\nEnter option #: ")

            #if choice == '1':
                

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