class AppStore:
    def __init__(self, games, social_media, utility):
        self.games = games
        self.social_media = social_media
        self.utility = utility

    def search_apps(self, category):
        if category.lower() == 'games':
            return self.games
        elif category.lower() == 'social media':
            return self.social_media
        elif category.lower() == 'utility':
            return self.utility
        else:
            return "Invalid category"

# Define app lists
gameList = {
    'Game One': '1.99',
    'Game Two': '9.99',
    'Game Three': '12.99',
    'Game Four': 'Free',
    'Game Five': 'Free'
}

socialMediaList = {
    'Social One': 'Free',
    'Social Two': 'Free',
    'Social Three': 'Free',
    'Social Four': 'Free',
    'Social Five': 'Free'
}

utilityList = {
    'Utility One': '1.00',
    'Utility Two': 'Free',
    'Utility Three': '1.99',
    'Utility Four': 'Free',
    'Utility Five': '2.99',
}

# Create an instance of AppStore
app_store = AppStore(gameList, socialMediaList, utilityList)

# User input
game_search = input('What type of app are you looking for (games/social media/utility)?: ')

# Search and print apps based on user input
search_result = app_store.search_apps(game_search)
if isinstance(search_result, dict):
    for app, price in search_result.items():
        print(f'{app}: ${price}')
else:
    print(search_result)
