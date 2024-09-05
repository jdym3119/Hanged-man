import random
class HangedMan:
    def __init__(self, words:list):
        self.words=words
        self.secret_word=random.choice(words).lower()
        self.guessed_letters=set()
        self.attempt=7
        self.word=["_"]*len(self.secret_word)
    def getter_attempts(self):
        return self.attempt
    def getter_word(self):
        return self.word
    def show_secret_word(self):
        return self.secret_word
    def show_words(self):
        return self.words
    def guess_letter(self, letter):
        letter=letter.lower()
        if letter in self.secret_word:
            self.guessed_letters.add(letter)
            for i in range(len(self.secret_word)):
                if self.secret_word[i] == letter:
                    self.word[i] = letter
        else:
            self.attempt-=1
        return letter in self.secret_word
    def win(self):
        return self.attempt >0 and set(self.secret_word).issubset(self.word)
    def lose(self):
        return self.attempt == 0 and not self.win()