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