import random
class NumberGuess:
    def __init__(self):
        self.secret_number = None
        self.difficulty_lvl = int(input("enter the difficulty level(easy-1,medium-2,hard-3):"))
    def generate_secret_num(self):
        for i in range(3):
            print("generating secret number...")
        if self.difficulty_lvl==1:
            self.secret_number = random.randint(0,10)
        elif self.difficulty_lvl==2:
            self.secret_number=random.randint(0,30)
        elif self.difficulty_lvl==3:
            self.secret_number=random.randint(0,150)
        else:
            print("invalid input 🚫")
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
