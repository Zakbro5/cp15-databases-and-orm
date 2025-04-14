import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# ===================
# FINAL EXAM PRACTICE
# ===================


# 1. Create a SQLite Database called cats.db through peewee
'''
It should have the following columns:
    - cat_id (the primary key)
    - cat_name
    - owner_name
'''

# 2. Ask the user for inputs for the cat_name and owner_name to create new rows
# in the database


# 3. Override the create function to make sure that every cat_name and
# owner_name gets stored as a capitalized version. Don't stop anything from
# being created, just make it so the first letter is capitalized and that it is
# stored without leading or trailing spaces.


# 4. Make a menu. Option 1 is to add a new cat. Option 2 is to see all cats.
# When option 2 is selected, make it so that the cats print out in reverse
# alphabetica order by cat_name


# 5. Add option 3. Option 3 should ask for an owner's name. If the owner name
# exists, make it show all the cats with that owner_name. If the owner_name
# doesn't exist in the database, display a message that that owner couldn't be
# found, and go back to the menu.


# 6. Add option 4. Enter a cat's id to get it, then enter a new name, and save
# that name. For time's sake you can assume the Id entered will always be valid

# 7. Add option 5. Enter a cat's id to get it, then delete it. Print out a
# message that it was deleted.
