class Player:

    def __init__(self, name):
        """Initializes the player's name. The default score is 0"""
        self._name = name
        self._score = 0

    def get_name(self):
        """Return player's name"""
        return self._name

    def get_score(self):
        """Return player's score"""
        return self._score

    def get_name_score(self):
        """Returns the player's name and score as a string, 
        maybe displayable for the high score section if we decide to make one?"""
        print(f'{self._name}:   {self._score}')

    def score_increment(self):
        self._score += 100
