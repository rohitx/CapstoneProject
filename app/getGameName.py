"""
This program is used by model.py to get the name of the game from the user, clean
the name and return a name string that is then used by the model to query a games
data frame.
File(s) used: None
Database(s) uses: None
Created: September 28th, 2015
Creator: Rohit Deshpande
"""

def clean_game_name(game):
    """
    This function takes the user from user
    and modifies it for searching the database
    """
    if "&" in game:
            #game = game.replace(" ", "").replace("&", "-").lower()
        game = game.replace(" ","-").replace("&","").lower()
        game = game.replace(":", "")
        game = game.replace("'", "")
        game = game.replace("(", "").replace(")","").replace(" ", "-")
        game = game.replace(",", "")
        game = game.replace("?", "")
        game = game.replace(".", "")
    elif "(" in game:
        game = game.replace("(", "").replace(")","").replace(" ", "-").lower()
        game = game.replace("'", "")
        game = game.replace(":", "")
    else:
        game = game.replace(":", "")
        game = game.replace(",", "")
        game = game.replace("'", "")
        game = game.strip().replace(".", "")
        game = game.lower().replace(" ", "-")
        game = game.replace("/", "")
        game = game.replace("(", "").replace(")","")
        game = game.replace(";", "")
        game = game.replace("?", "")
    return game

if __name__ == '__main__':
    # Test the program
    clean_game_name("007: Legend")