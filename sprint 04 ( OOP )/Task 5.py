class Gallows:
    def __init__(self, words = [], game_over = False):
        self.words = words
        self.game_over = game_over
    def play(self, word):
        if len(self.words):
            if self.words[-1][-1] == word[0]:
                if word in self.words:
                    self.game_over = True
                    return 'game over'
                self.words.append(word)
                return self.words
            else:
                self.game_over = True
                return 'game over'
        else:
            self.words.append(word)
            return self.words
    def restart(self):
        self.game_over = False
        self.words = []
        return 'game restarted'

