class SteamUser:

    def __init__(self, username, games):
        self.username = username
        self.games = games
        self.played_hours = 0

    def play(self, game, hours):
        pass

    def buy_game(self, game):
        pass
    def status(self):
        pass