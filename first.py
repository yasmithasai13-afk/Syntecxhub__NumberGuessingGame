import random
class NumberGuess:
    def __init__(self):
        self.secret_number = None
        self.range_limit = int(input("enter the range:"))
    def generate_secret_num(self):
        self.secret_number = random.randint(0, self.range_limit)
    def get_user_guess(self):
        self.user_guess = int(input("enter your guess:"))
    def check_guess(self):
        attempts=0
        while True:
            attempts += 1
            self.get_user_guess()
            if self.user_guess == self.secret_number:
                print(f"Hurray Congratulations! You guessed it in {attempts} attempts 🎉")
                break
            elif self.user_guess > self.secret_number:
                print("too high! 🔺")
            else:
                print("too low! 🔻")
    def play_again(self):
        while True:
             opinion=input("would you like to play again? (y/n): ")
             if opinion.lower()=='y':
                self.__init__()
                self.generate_secret_num()
                self.check_guess()
             elif opinion.lower()=='n':
                print("Thanks for playing! 👋")
                break
             else:
                print("invalid input 🚫")
                continue
game=NumberGuess()
game.generate_secret_num()
game.check_guess()
game.play_again()
